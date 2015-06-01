import praw
import pprint
import csv
import datetime


class Comment:
	def __init__(self, body, karma, date, author):
		self.body = body
		self.karma = karma
		self.date = date
		self.author = author

def scrape_subreddit():
	user_agent = "Comment Karma Prediction by /u/HeteroDog"
	r = praw.Reddit(user_agent=user_agent)
	boards = ['4chan', 'fitness', 'ssbm', 'news', 'askreddit', 'gonewild', 'hentai']
	for board in boards:
		comments = []
		subreddit = r.get_subreddit(board)
		for submission in subreddit.get_hot(limit = 10):
			forest_comments = submission.comments
			flat_comments = praw.helpers.flatten_tree(forest_comments)
			for comment in flat_comments:
				try:
					if (comment.is_root):
						comments.append(Comment(comment.body, 
							(comment.ups - comment.downs), 
							datetime.datetime.fromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
							comment.author))
				except AttributeError:
					pass
					
		writer = csv.writer(open('data/' + board + '.csv', 'a'))
		for comment in comments:
		   writer.writerow([comment.body.encode('utf-8').strip(), comment.date, comment.author, comment.karma])
	return comments

scrape_subreddit()