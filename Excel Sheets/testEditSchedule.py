import schedule
import time
import testEdit
import importlib

def timing():
    importlib.reload(testEdit)
    testEdit.showText()

schedule.every(10).seconds.do(timing)

while True:
    schedule.run_pending()
    time.sleep(1)
