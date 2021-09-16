from selenium import webdriver
# For using sleep function because selenium
# works only when the all the elemets of the
# page is loaded.
import time

from PIL import Image
browser = webdriver.Chrome("F:\chromedriver_win32 (2)\chromedriver.exe")

url = "https://www.instagram.com"  # You can paste any id

browser.get(url)
time.sleep(3)

time.sleep(5)
username=browser.find_element_by_css_selector("input[name='username']")
password=browser.find_element_by_css_selector("input[name='password']")
username.clear()
password.clear()
username.send_keys("#####")
password.send_keys("#####")
login = browser.find_element_by_css_selector("button[type='submit']").click()
time.sleep(5)
browser.save_screenshot("screenshot.png")

# Loading the image
image = Image.open("screenshot.png")

# Showing the image
image.show()
