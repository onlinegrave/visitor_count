from selenium import webdriver
import os
from urllib.parse import urlparse
import threading
from pathlib import Path
BASE_LINK = "https://github.com/onlinegrave"
driver = webdriver.Chrome(Path.joinpath(Path(os.getcwd()), "chromedriver"))

def start():
  threading.Timer(0.10, start).start()
  driver.get(urlparse(BASE_LINK).geturl())

start()


