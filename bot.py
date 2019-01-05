import telebot
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import NoSuchElementException
import time
import ast


bot = telebot.TeleBot("681865117:AAEnx260WwhGwwJ2qoeJyMAGStGedu7Cv1U")

@bot.message_handler(commands=["start"])

def wassimMessage(message):
	bot.send_message(message.chat.id, "it's working now for login to edugate portal: plz write the command like this:  /login user pass")

@bot.message_handler(regexp="/login")

def getSchdual(message):
	try:
		username = message.text.split()[1]
		password = message.text.split()[2]
		print "username: " + username
		print "password: " + password
		bot.send_message(message.chat.id, "it's getting login information...")

		#user = '201503234'
		#password = 'TRuMeh8r*r#'
		driver= webdriver.Firefox(executable_path="Drivers/geckodriver")
		url="http://edugate.jazanu.edu.sa"
		driver.get(url)
		bot.send_message(message.chat.id, "The web page opened now...")
		username_text_field = driver.find_element(by=By.ID, value="loginFrm:user_name")
		password_text_field = driver.find_element(by=By.ID, value="loginFrm:user_password")
		login_button = driver.find_element(by=By.ID, value="loginFrm:loginUsersLink")
		username_text_field.send_keys(username)
		password_text_field.send_keys(password)
		login_button.click()
		
		hi = driver.find_element(By.XPATH, '//*[@id="header_bottom"]/div/ul/li[1]/a')
		hi.click()

		cources = driver.find_element(By.XPATH, '//*[@id="menuForm:serTextStudSchedule"]')
		cources.click()
		bot.send_message(message.chat.id, "Successfully logged...")
		driver.execute_script("window.scrollTo(0,450)")
		driver.save_screenshot("screenshots/screenshot.png")
		bot.send_message(message.chat.id, "screen shot...")
		driver.close()
		photo = open('screenshots/screenshot.png', 'rb')
		img = Image.open("screenshots/screenshot.png")

		area = (60, 20, 930, 610)
		
		crop = img.crop(area)
		crop.save("screenshots/scresenshot.png")
		croped = open('screenshots/scresenshot.png', 'rb')
		
		bot.send_photo(message.chat.id, croped)
	except NoSuchElementException:
		bot.send_message(message.chat.id, "You have wrong with you information plz try again")
		driver.close()


		
	
bot.polling()