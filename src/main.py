import time
from timeloop import Timeloop
from datetime import timedelta

from webScraper import WebScraper


time_loop = Timeloop()

@time_loop.job(interval=timedelta(hours=4, minutes=3, seconds=9))
def updateResumeByTimer():
    ws = WebScraper()
    ws.updateAll()

if __name__ == "__main__" :
    time_loop.start(block=True)


    
