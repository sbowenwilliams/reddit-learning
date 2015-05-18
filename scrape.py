import praw
import pprint

user_agent = "Comment Karma Prediction by /u/HeteroDog"

r = praw.Reddit(user_agent=user_agent)

# user_name = "HeteroDog"
# user = r.get_redditor(user_name)
comments = {}
subreddit = r.get_subreddit('askreddit')
for submission in subreddit.get_hot(limit = 1):
	forest_comments = submission.comments
	flat_comments = praw.helpers.flatten_tree(forest_comments)
	for comment in flat_comments:
		try:
			comments[comment.body] = comment.ups
		except AttributeError:
			pass
			
pprint.pprint(comments)
