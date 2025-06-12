import logging
import logging.config

logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

import dotenv
from wpp.manager import WppManager

def main():
    setup()
    wpp = WppManager()
    wpp.send_message(to="5521997076296",msg="oi oi")

def setup():
    logger.info("running setup")
    dotenv.load_dotenv()


if __name__ == "__main__":
    main()
