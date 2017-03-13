import sys
import sentiment_analyzer as sa

get_tweet = True

print("Sentiment Analyzer has been loaded ...")
while (get_tweet):
	sent = raw_input("Enter Tweet (Sentence): ")
	if sent == 'exit' or sent == 'end':
		get_tweet = False
		sys.exit(0)
	else:
		print(sa.sentiment(sent))