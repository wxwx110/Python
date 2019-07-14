from .BaseHandler import BaseHandler
import logging

class IndexHandler(BaseHandler):
    def get (self):
        logging.debug("debug")
        logging.info("info")
        logging.warning("warning")
        logging.error("error")
        self.write("hello")