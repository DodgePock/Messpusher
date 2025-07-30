import requests
import logging
logger = logging.getLogger(__name__)

class Messpusher:
    def __init__(self, messpusher_config:dict) -> None:
        self.pushplus_config = messpusher_config.get('pushplus', None)

    def send_pushplus(self, title, message):
        logger.info('Starting pushplus message push')
        logger.info(f"Push content:\ntitle:{title}\nmessage:{message}")
        if self.pushplus_config is None:
            logger.warning('Pushplus not configured, exiting')
            return False
        try:
            url = 'http://www.pushplus.plus/send'
            data = {
                'title': title,
                'content': message,
                'channel': 'wechat',
                'template': 'txt',
                'token': self.pushplus_config['token']
            }
            r = requests.post(url=url, json=data)
            if r.status_code == 200 and r.json()['code'] == 200 and '成功' in r.json()['msg']:
                logger.info('Pushplus message sent successfully')
                return True
            else:
                logger.warning(f"Failed to send pushplus message, reason: {r.text}")
                return False
        except Exception as e:
            logger.error(f"Error occurred while sending pushplus message, reason: {e}")
            return False


    def send_all(self, title, message):
        if self.pushplus_config!=None:
            self.send_pushplus(title, message)
