from plyer import notification

def send_notification(info, location):
    notification.notify(
        title="Campus Safe Alert",
        message=f"{info}\n{location}",
        timeout=10  # Notification timeout in seconds
    )