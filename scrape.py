import praw
import pprint
import csv
import datetime

user_agent = "Comment Karma Prediction by /u/HeteroDog"

class Comment:
	def __init__(self, body, karma, date, author):
		self.body = body
		self.karma = karma
		self.date = date
		self.author = author


r = praw.Reddit(user_agent=user_agent)

# user_name = "HeteroDog"
# user = r.get_redditor(user_name)
comments = []
subreddit = r.get_subreddit('askreddit')
for submission in subreddit.get_hot(limit = 1):
	forest_comments = submission.comments
	flat_comments = praw.helpers.flatten_tree(forest_comments)
	for comment in flat_comments:
		try:
			comments.append(Comment(comment.body, 
				comment.ups, 
				datetime.datetime.fromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
				comment.author))
		except AttributeError:
			pass
			
# pprint.pprint(comments)
writer = csv.writer(open('dict.csv', 'a'))
for comment in comments:
   writer.writerow([comment.body.encode('utf-8').strip(), comment.date, comment.author, comment.karma])