import csv
from selenium import webdriver
import time
from datetime import date
import pandas as pd
import requests
import re
import schedule

today = date.today()

DRIVER = 'chromedriver'
driver = webdriver.Chrome(DRIVER)

# need to create a set to store unique channels so that only new channels are appended

def telegramvalidate():
	with open('telegram-' + str(today) + '.csv', 'r') as f:
		reader = csv.reader(f)
		next(reader)
		for row in reader:
			row = "".join(row)
			x = re.findall('[^/]+/(\w+)', row)
			regex = "".join(x)
			telegrams = "https://t.me/" + regex # need to make regex pattern to turn posts into channels
			try:
				driver.get(telegrams)
				time.sleep(3)
				try:
					tdescription = driver.find_element_by_class_name('tgme_page_description') #only pulls from channels, not posts (needs improvement)
					teledesc = tdescription.text
					with open('keywords.csv', 'r', newline='') as keywords:
						file = keywords.read().splitlines()
						for keyword in file:
							if keyword.lower() in teledesc.lower():
								print(keyword + " found in: " + telegrams)
								with open('goodtelegrams.csv', 'a') as goodtelegrams:
									writer = csv.writer(goodtelegrams)
									writer.writerow([telegrams])
							else:
								pass
				except:
					pass

			except:
				pass

		driver.quit()

telegramvalidate()


schedule.every().day.at("17:30").do(telegramvalidate)

while True:
	schedule.run_pending()
	time.sleep(1)
