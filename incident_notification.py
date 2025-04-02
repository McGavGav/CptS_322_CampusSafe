from notifypy import Notify

def send_notification(info, alert_type):
    notification = Notify()
    notification.title = "\n"
    notification.message = info
    notification._notification_application_name = alert_type
    notification.send()