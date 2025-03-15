function sendAlert()
            {
                navigator.geolocation.getCurrentPosition(function(position){
                    const lat = position.coords.latitude;
                    const lon = position.coords.longitude;
                    console.log(lat);
                    console.log(lon);
                    fetch('../alertsend/', {
                        method:'POST',
                        headers:{
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                            lat:lat,
                            lon:lon,
                        })
                    })
                    .then(respose => respose.json())
                    .then(data => {console.log('server response', data)})
                    .catch(err => {console.log('Error', err)})

                })
            }
            