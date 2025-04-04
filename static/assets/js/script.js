function sendAlert() {
    if (!confirm("Are you sure you want to trigger an emergency alert?")) return;

    if (!navigator.geolocation) {
        showError("Geolocation is not supported by your browser.");
        return;
    }

    navigator.geolocation.getCurrentPosition(function(position) {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;

        updateStatus(`Coordinates: ${lat}, ${lon}`);

        fetch("/alert/trigger/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: new URLSearchParams({
                latitude: lat,
                longitude: lon
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                updateStatus("Help is on the way!");
            } else {
                showError("Failed to trigger emergency alert.");
            }
        })
        .catch(err => {
            showError("Error sending alert: " + err.message);
        });
    }, function(error) {
        showError("Error getting location: " + error.message);
    });
}

function cancelEmergency() {
    if (!confirm("Are you sure you want to cancel the emergency?")) return;

    fetch("/alert/cancel/", {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "cancelled") {
            updateStatus("Emergency cancelled.");
        } else {
            showError("Failed to cancel emergency.");
        }
    })
    .catch(err => {
        showError("Error cancelling: " + err.message);
    });
}

function updateStatus(message) {
    const statusDiv = document.getElementById('status');
    statusDiv.innerText = message;
    statusDiv.style.color = "black";
}

function showError(message) {
    const statusDiv = document.getElementById('status');
    statusDiv.innerText = message;
    statusDiv.style.color = "red";
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
