import re
import requests
import time
import pandas as pd
from datetime import date
from datetime import timedelta
import schedule

# gab, parler, 4chan, 8kun, win, poal, telegram, gettr, minds

today = date.today()
yesterday = today - timedelta(days = 1)

telegram = "t.me"

telere = 'https://t.me([^\\\\]+)'
channelre = '[^/]*/([^/]*)'

limit = 50

# URLs of each API request to SMAT for each source

win_url = "https://api.smat-app.com/content?term={}&limit={}&site=win&since={}&until={}&esquery=false&sortdesc=false".format(telegram, limit, yesterday, today)
gab_url = "https://api.smat-app.com/content?term={}&limit={}&site=gab&since={}&until={}&esquery=false&sortdesc=false".format(telegram, limit, yesterday, today)
telegram_url = "https://api.smat-app.com/content?term={}&limit={}&site=telegram&since={}&until={}&esquery=false&sortdesc=false".format(telegram, limit, yesterday, today)
minds_url = "https://api.smat-app.com/content?term={}&limit={}&site=minds&since={}&until={}&esquery=false&sortdesc=false".format(telegram, limit, yesterday, today)
fourchan_url = "https://api.smat-app.com/content?term={}&limit={}&site=4chan&since={}&until={}&esquery=false&sortdesc=false".format(telegram, limit, yesterday, today)
gettr_url = "https://api.smat-app.com/content?term={}&limit={}&site=gettr&since={}&until={}&esquery=false&sortdesc=false".format(telegram, limit, yesterday, today)
poal_url = "https://api.smat-app.com/content?term={}&limit={}&site=poal&since={}&until={}&esquery=false&sortdesc=false".format(telegram, limit, yesterday, today)
mewe_url = "https://api.smat-app.com/content?term={}&limit={}&site=mewe&since={}&until={}&esquery=false&sortdesc=false".format(telegram, limit, yesterday, today)

# Store unique Telegrams

uniques = set()

# Function to iterate through each URL and scrape out Telegram channels

def smatscrape():
	print("Starting scrape...")
	#API request for Win Communities
	r_win = requests.get(win_url)
	r_win = r_win.text

	for tmatches in re.findall(telere, r_win):
		trecord = "t.me" + tmatches
		if len(trecord) < 18:
			tresponse = requests.get("https://t.me/" + tmatches)
			if "tgme_action_button_new" in tresponse.text:
				usernames = re.findall(channelre, trecord)
				usernames = "t.me/" + usernames[0]
				uniques.add(usernames)
				time.sleep(5)

	#API request for Gab
	r_gab = requests.get(gab_url)
	r_gab = r_gab.text

	for tmatches in re.findall(telere, r_gab):
		trecord = "t.me" + tmatches
		if len(trecord) < 18:
			tresponse = requests.get("https://t.me/" + tmatches)
			if "tgme_action_button_new" in tresponse.text:
				usernames = re.findall(channelre, trecord)
				usernames = "t.me/" + usernames[0]
				uniques.add(usernames)
				time.sleep(5)

	#API request for Telegram
	r_telegram = requests.get(telegram_url)
	r_telegram = r_telegram.text

	for tmatches in re.findall(telere, r_telegram):
		trecord = "t.me" + tmatches
		if len(trecord) < 18:
			tresponse = requests.get("https://t.me/" + tmatches)
			if "tgme_action_button_new" in tresponse.text:
				usernames = re.findall(channelre, trecord)
				usernames = "t.me/" + usernames[0]
				uniques.add(usernames)
				time.sleep(5)

	#API request for Minds
	r_minds = requests.get(minds_url)
	r_minds = r_minds.text

	for tmatches in re.findall(telere, r_minds):
		trecord = "t.me" + tmatches
		if len(trecord) < 18:
			tresponse = requests.get("https://t.me/" + tmatches)
			if "tgme_action_button_new" in tresponse.text:
				usernames = re.findall(channelre, trecord)
				usernames = "t.me/" + usernames[0]
				uniques.add(usernames)
				time.sleep(5)

	#API request for 4chan
	r_fourchan = requests.get(fourchan_url)
	r_fourchan = r_fourchan.text

	for tmatches in re.findall(telere, r_fourchan):
		trecord = "t.me" + tmatches
		if len(trecord) < 18:
			tresponse = requests.get("https://t.me/" + tmatches)
			if "tgme_action_button_new" in tresponse.text:
				usernames = re.findall(channelre, trecord)
				usernames = "t.me/" + usernames[0]
				uniques.add(usernames)
				time.sleep(5)

	#API request for Gettr
	r_gettr = requests.get(gettr_url)
	r_gettr = r_gettr.text

	for tmatches in re.findall(telere, r_gettr):
		trecord = "t.me" + tmatches
		if len(trecord) < 18:
			tresponse = requests.get("https://t.me/" + tmatches)
			if "tgme_action_button_new" in tresponse.text:
				usernames = re.findall(channelre, trecord)
				usernames = "t.me/" + usernames[0]
				uniques.add(usernames)
				time.sleep(5)

	#API request for Gettr
	r_poal = requests.get(poal_url)
	r_poal = r_poal.text

	for tmatches in re.findall(telere, r_poal):
		trecord = "t.me" + tmatches
		if len(trecord) < 18:
			tresponse = requests.get("https://t.me/" + tmatches)
			if "tgme_action_button_new" in tresponse.text:
				usernames = re.findall(channelre, trecord)
				usernames = "t.me/" + usernames[0]
				uniques.add(usernames)
				time.sleep(5)

	#API request for MeWe
	r_mewe = requests.get(mewe_url)
	r_mewe = r_mewe.text

	for tmatches in re.findall(telere, r_mewe):
		trecord = "t.me" + tmatches
		if len(trecord) < 18:
			tresponse = requests.get("https://t.me/" + tmatches)
			if "tgme_action_button_new" in tresponse.text:
				usernames = re.findall(channelre, trecord)
				usernames = "t.me/" + usernames[0]
				uniques.add(usernames)
				time.sleep(5)


	df = pd.DataFrame(uniques, columns=["channels"])
	df.to_csv('smat-telegram-' + str(today) + '.csv', index=False)

	print("Scrape complete...")

smatscrape()

schedule.every().day.at("09:30").do(smatscrape)

while True:
	schedule.run_pending()
	time.sleep(1)
