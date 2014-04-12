import praw

def login():
		r = praw.Reddit(user_agent = 'something')
		submissions = r.get_subreddit('IAmA').get_new(limit = 100)
		J = get_AMA_names(submissions)

def get_AMA_names(submissions):
		submissionArray = []
		finalnames = []
		for x in submissions:
				submissionArray.append(str(x))
						# if '[AMA Request]' in str(x)
						# submissions.delete(x)
				# print[str(x) for x in submissions]

	#	for i in submissionArray:
				i = str(x)
				if '[AMA Request]' not in i:
						numUpvotes = int(i[0: i.find(" ")])
						if numUpvotes > 400:
							finalnames.append(x)

		return finalnames


login()