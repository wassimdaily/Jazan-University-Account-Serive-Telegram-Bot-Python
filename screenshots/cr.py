import telebot
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import NoSuchElementException
import time
import ast


driver= webdriver.Firefox(executable_path="Drivers/geckodriver")
url="http://colleges.jazanu.edu.sa/csc/Pages/CS_Staff_members1.aspx"
driver.get(url)

a1 = driver.find_element(By.XPATH, '//*[@id="WebPartWPQ2"]/table/tbody/tr[6]/td/table/tbody/tr/td/a[1]/font')

driver.execute_script("window.scrollTo(0,470)")
driver.save_screenshot("screenshot1.png")


a2 = driver.find_element(By.XPATH, '//*[@id="WebPartWPQ2"]/table/tbody/tr[6]/td/table/tbody/tr/td/a[2]/font')

a2.click()
driver.execute_script("window.scrollTo(0,470)")
driver.save_screenshot("screenshot2.png")

a3 = driver.find_element(By.XPATH, '//*[@id="WebPartWPQ2"]/table/tbody/tr[6]/td/table/tbody/tr/td/a[3]/font')

a3.click()
driver.execute_script("window.scrollTo(0,470)")
driver.save_screenshot("screenshot3.png")

a4 = driver.find_element(By.XPATH, '//*[@id="WebPartWPQ2"]/table/tbody/tr[6]/td/table/tbody/tr/td/a[4]/font')

a4.click()
driver.execute_script("window.scrollTo(0,470)")
driver.save_screenshot("screenshot4.png")

a5 = driver.find_element(By.XPATH, '//*[@id="WebPartWPQ2"]/table/tbody/tr[6]/td/table/tbody/tr/td/a[5]/font')

a5.click()
driver.execute_script("window.scrollTo(0,470)")
driver.save_screenshot("screenshot5.png")
#photo = open('screenshots/screenshot.png', 'rb')
#img = Image.open("screenshots/screenshot.png")

#area = (60, 20, 930, 610)
		
#crop = img.crop(area)
#crop.save("screenshots/scresenshot.png")
#croped = open('screenshots/scresenshot.png', 'rb')