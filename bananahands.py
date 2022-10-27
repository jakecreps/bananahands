import json
import re
import requests
from colorama import init, Fore, Back, Style
import time
import pandas as pd
from datetime import date
import schedule

today = date.today()

init(autoreset=True)

discord = "discord.gg" #declaring discord URL
telegram = "t.me" #declaring telegram URL

turl_comment = "https://api.pushshift.io/reddit/search/comment/?q={}&sort_type=created_utc&size=50".format(telegram) #creating the API request for telegram
durl_comment = "https://api.pushshift.io/reddit/search/comment/?q={}&sort_type=created_utc&size=50".format(discord) #creating the API request for discord

turl_post = "https://api.pushshift.io/reddit/search/submission/?q={}&sort_type=created_utc&size=50".format(telegram) #creating the API request for telegram
durl_post = "https://api.pushshift.io/reddit/search/submission/?q={}&sort_type=created_utc&size=50".format(discord) #creating the API request for telegram


telere = 't.me([^"]+)' # regex pattern for telegram channel (needs improvement)
discore = 'discord.gg([^"]+)' # regex pattern for discord channel (needs improvement)

tuniques = set() # create set to store unique telegram chats
duniques = set() # create set to store unique discord chats

def scrape():
	while True:
		try:
			tresponse_comment = requests.get(turl_comment).text
			time.sleep(5)

			for tmatches in re.findall(telere, tresponse_comment):
				trecord = "t.me" + tmatches
				if len(trecord) < 20:
					tresponse = requests.get("https://t.me/" + tmatches)
					if "tgme_action_button_new" in tresponse.text:
						tuniques.add(trecord)
						print(Fore.GREEN + "[+] " + Fore.WHITE + "Telegram: " + trecord + Fore.YELLOW + " [comment]")


			tresponse_post = requests.get(turl_post).text
			time.sleep(5)

			for tmatches in re.findall(telere, tresponse_post):
				trecord = "t.me" + tmatches
				if len(trecord) < 20:
					tresponse = requests.get("https://t.me/" + tmatches)
					if "tgme_action_button_new" in tresponse.text:
						tuniques.add(trecord)
						print(Fore.GREEN + "[+] " + Fore.WHITE + "Telegram: " + trecord + Fore.GREEN + " [submission]")


			dresponse_comment = requests.get(durl_comment).text
			time.sleep(5)

			for dmatches in re.findall(discore, dresponse_comment):
				drecord = "discord.gg" + dmatches
				if len(drecord) < 20:
					duniques.add(drecord)
					print(Fore.GREEN + "[+] " + Fore.WHITE + "Discord: " + drecord + Fore.YELLOW + " [comment]")


			dresponse_post = requests.get(durl_post).text
			time.sleep(5)

			for dmatches in re.findall(discore, dresponse_post):
				drecord = "discord.gg" + dmatches
				if len(drecord) < 20:
					duniques.add(drecord)
					print(Fore.GREEN + "[+] " + Fore.WHITE + "Discord: " + drecord + Fore.GREEN + " [submission]")


			df = pd.DataFrame(tuniques, columns=["channels"])
			df.to_csv('telegram-' + str(today) + '.csv', index=False)

			df = pd.DataFrame(duniques, columns=["channels"])
			df.to_csv('discord-' + str(today) + '.csv', index=False)

		except:
			return False
scrape()

schedule.every().day.at("17:30").do(scrape)

while True:
	schedule.run_pending()
	time.sleep(1)
