from messpusher import Messpusher
from config_template import messpusher_config

ms = Messpusher(messpusher_config)

subject_title = 'Test Message'
subject_message = 'This is a test message from Messpusher.'

ms.send_all(subject_title, subject_message)