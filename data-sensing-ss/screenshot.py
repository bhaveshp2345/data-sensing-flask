from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


ssImg = "C:/Users/Bhavesh/Desktop/Bhavesh/live-image-project/data-sensing-ss/one.png"
appUrl = 'http://127.0.0.2:10010/'

if os.path.exists(ssImg):
  os.remove(ssImg)

# 2
options = Options()
options.headless = True
 
# 3
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def isBrowserAlive():
   try:
      driver.get(appUrl)
      return True
   except:
      return False

while not isBrowserAlive():
    print("Retrying : " + appUrl)
    time.sleep(10)
 
print("Connected : " + appUrl)

while 1:
    try:
        driver.save_screenshot(ssImg)
        time.sleep(2)
    except:
        print("Failed to capture Screenshot!")