from plyer import notification

notification_title = "MEHMETİN SANA MESAJI VAR"
notification_message = "Naber lan"

notification.notify(title = notification_title,
                    message = notification_message,
                    app_icon = None,
                    timeout = 10,
                    toast = False)