import time
from timeloop import Timeloop
from datetime import timedelta
import logging

from webScraper import WebScraper
from configLoader import ConfigLoader

time_loop = Timeloop()

@time_loop.job(interval=timedelta(hours=4, minutes=3, seconds=27))
def updateResumeByTimer():
    ws = WebScraper()
    ws.updateAll()

if __name__ == "__main__" :
    logging.basicConfig(filename=ConfigLoader.getLogsPath(), format='[%(asctime)s] [%(name)s] [%(levelname)s]  %(message)s')
    time_loop.start(block=True)


    