#!/usr/bin/python

# SwiftBot by u/SailorLeroy. June 26, 2014

import praw
import time

username = 'SwiftBot'
password = 'resetyourpassword'
subreddit = 'bottesting'

# String to search for. 'Taylor Swift' makes sense.
search_term = 'Taylor Swift'
# Number of posts to look through. Setting this to a high number will 
# result in a long run time. Setting too low will only look at a few most
# popular posts. Experiment with this value. 10-20 makes sense.
num_posts = 10
# Mins to sleep between subreddit scans. You can set this to whatever you
# want. Setting it too low may result in fewer hits per scan. Setting it 
# too high may result in missed hits. On a high traffic subreddit, perhaps
# 10 mins would be reasonable. Low traffic, 60 mins or longer. Up to you.
sleep_time = 10

already_seen = set()

r = praw.Reddit(username)
r.login(username, password)
subreddit = r.get_subreddit(subreddit)

while True:
	for submission in subreddit.get_hot(limit=num_posts):
		comments = praw.helpers.flatten_tree(submission.comments)
		for comment in comments:
			if search_term in comment.body and comment.id not in already_seen:
				already_seen.add(comment.id)
				comment.reply('[Taylor Swift](http://www.reddit.com/r/TaylorSwift/)')
				print '----> SubmissionID: %s,\tCommentID: %s,\tAuthor: %s,\tScore: %s' % \
						(submission.id, comment.id, comment.author, comment.score) 

	print 'Done. Next scan in %d minutes.' % sleep_time
	time.sleep(60 * sleep_time)