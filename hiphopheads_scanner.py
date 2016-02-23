import time

import praw
from twilio.rest import TwilioRestClient

user_agent = ('app to check for recent music submissions. /u/deeprecursion')
r = praw.Reddit(user_agent = user_agent)

cole_words = ['J. Cole', 'J Cole', 'Cole', 'Dreamville']
kendrick_words = ['Kendrick Lamar', 'Kendrick']
cache = []

def has_it_dropped():

	subreddit = r.get_subreddit("hiphopheads")
	submissions = subreddit.get_new(limit = 10)

	for submission in submissions:
		title = submission.title

		cole_world = any(string in title for string in cole_words)
		kdot = any(string in title for string in kendrick_words)

		if submission.id not in cache and cole_world and kdot:
			cache.append(submission.id)
			text_me()

def text_me():
	account_sid = sid
	auth_token = token
	client = TwilioRestClient(account_sid, auth_token)
	message = client.messages.create(to=me, from_=my_twilio_num, body='Kendrick AND Cole mentioned!!!!')

with open('credentials.txt','r') as credentials:
	lines = credentials.readlines().splitlines()
	sid = lines[0].split('=')[1]
	token = lines[1].split('=')[1]
	me = lines[2].split('=')[1]
	my_twilio_num = lines[3].split('=')[1]

while True:
	has_it_dropped()
	time.sleep(10)
