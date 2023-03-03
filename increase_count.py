from selenium import webdriver
import os
from urllib.parse import urlparse
import threading
from apscheduler.schedulers.blocking  import BlockingScheduler
from pathlib import Path
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
BASE_LINK = "https://github.com/onlinegrave"
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(Path.joinpath(Path(os.getcwd()), "chromedriver"), options=chrome_options)

scheduler = BlockingScheduler()
def start():
  driver.get(urlparse(BASE_LINK).geturl())


# Find your perfect balance according to cpu
scheduler.add_job(start,'interval', seconds = 0.600)
scheduler.start()

