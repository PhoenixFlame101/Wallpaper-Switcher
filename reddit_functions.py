""" Gets 2 wallpapers a week from reddit.com/r/wallpapers/top """

import praw
import urllib.request
from urllib.parse import quote
from refuse_controls import *
from local_functions import file_extension

def get_comment_body(submission, user):
	""" Returns a comment made by a specific user """
	try:
		for comment in submission.comments.list():
			if user == str(comment.author):
				return str(comment.body)
			elif user in str(comment.body):
				for reply in comment.replies:
					if user == str(reply.author):
						return reply.body
	except:
		False

def link_finder(submission):
	""" Finds the link for the 1920 x 1080 res image """
	_url = []
	if '1920' not in str(submission.title) and get_comment_body(submission, 'ze-robot'):
		for word in get_comment_body(submission, 'ze-robot').split():
			if word.startswith('[1920×1080]'):
				_url = list(str(word[12:-2]))
				if '×' in _url:
					_url[_url.index('×')] = quote('×')
				return ''.join(_url)
		else:
			return str(submission.url)
	else:
		return str(submission.url)

def get_walls_func(path, url, refuse):
	""" Downloads wall images """
	opener = urllib.request.build_opener()
	opener.addheaders = [('User-agent', 'Mozilla/5.0')]
	urllib.request.install_opener(opener)
	try:
		urllib.request.urlretrieve(url, path)
	except:
		pass
	add_to_refuse(url, refuse)

def get_walls(path, refuse):
	reddit = praw.Reddit(client_id='---',
	                     client_secret='---',
	                     user_agent='wallpapers_bot')
	urls = []
	refused_links = get_refused_links(refuse)
	for submission in reddit.subreddit('wallpapers').top('week', limit=15):
		wallpaper_url = link_finder(submission)
		if wallpaper_url not in refused_links:
			if 'gallery' not in wallpaper_url and wallpaper_url != '':
				urls.append(wallpaper_url)
		if len(urls) >= 3:
			break

	for url in urls:
		get_walls_func(path+file_extension(url, '/'), url, refuse)
