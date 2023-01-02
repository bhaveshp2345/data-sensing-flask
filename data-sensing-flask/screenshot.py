from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# from firebase_admin import credentials, initialize_app, storage

# Init firebase with your credentials
# cred = credentials.Certificate("data-sensing-storage-2884975ad572.json")
# initialize_app(cred, {'storageBucket': 'data-sensing-storage.appspot.com'})

browser = webdriver.Chrome()
browser.get('http://127.0.0.2:10010/')
browser.implicitly_wait(10)

while 1:
    # try:
        browser.save_screenshot('one.jpeg')
        # Put your local file path 
        # fileName = "one.jpeg"
        # bucket = storage.bucket()
        # blob = bucket.blob(fileName)
        # blob.upload_from_filename(fileName)

        # Opt : if you want to make public access from the URL
        # blob.make_public()
        # print("your file url", blob.public_url)
        time.sleep(2)
    # except:
    #     print("Something went wrong!!")

