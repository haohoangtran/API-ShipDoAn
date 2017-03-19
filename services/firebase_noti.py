from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAAQtdLZoM:APA91bH725wKis_2RqOB0iTrZPXfXrU9ukW7aeKAD-N69sAvrUQ4L8DFsurUfX6_d15dWyWMISljk7jAFWjGAxfVG_CANk_QLIdwP8keXoi22rhNNnPiPIi1m3uV7xg5tZUtiyRyaHMp")


registration_id = "<device registration_id>"
message_title = "Uber update"
# message_body = "Hi john, your customized news for today is ready"

data_message = {
    "Nick" : "Mario",
    "body" : "great match!",
    "Room" : "PortugalVSDenmark"
}

result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=data_message)





