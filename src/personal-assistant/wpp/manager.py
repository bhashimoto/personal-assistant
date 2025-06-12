import json
import logging
logger = logging.getLogger(__name__)

from os import getenv
import requests



class WppManager:
    def __init__(self, 
                 base_url:str="https://graph.facebook.com/v22.0/662409600289144/messages"
                 ):
        logger.info("Initializing WppManager")
        self.auth_token:str|None = getenv("WHATSAPP_TOKEN")
        self.base_url:str = base_url
        self.set_standard_headers()

    def set_standard_headers(self):
        self.headers = {
            "Authorization": f"Bearer {self.auth_token}",
            "Content-Type": "application/json",
        }

    def send_message(self, to:str, msg:str):
        logger.info("sending message")
        data = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "text",
            "text": {
                "body":msg
            }
        }

        resp = requests.post(url=self.base_url, headers=self.headers, json=data)
        if resp.status_code == 200:
            logger.info(f"message sent successfully. Message id: {json.loads(resp.content)}")
        print(resp.content)
        print(resp.status_code)
