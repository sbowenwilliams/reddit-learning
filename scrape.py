import praw
import pprint
import csv

user_agent = "Comment Karma Prediction by /u/HeteroDog"

r = praw.Reddit(user_agent=user_agent)

# user_name = "HeteroDog"
# user = r.get_redditor(user_name)
comments = {}
subreddit = r.get_subreddit('askreddit')
for submission in subreddit.get_hot(limit = 5):
	forest_comments = submission.comments
	flat_comments = praw.helpers.flatten_tree(forest_comments)
	for comment in flat_comments:
		try:
			comments[comment.body] = comment.ups
		except AttributeError:
			pass
			
# pprint.pprint(comments)
writer = csv.writer(open('dict.csv', 'a'))
for key, value in comments.items():
   writer.writerow([key.encode('utf-8').strip(), value])