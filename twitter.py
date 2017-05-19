from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="7I4smG2NsxU4d0zQSMXKpW0af"
csecret="qJBiIb9WbXD05FZSi1qLdgmkr22eRpqgOlBkXA7erVE2rUguk2"
atoken="857728855322370048-c2eFzEaLCLtMKe0YC9d5TtKRMW7NuIy"
asecret="9brTNuiUfx51D7xzJ1UKEchQxnSyXUpukBmayE3KhUzBE"

class listener(StreamListener):

	def on_data(self, data):
			all_data = json.loads(data)
			tweet = all_data["text"]
			sentiment_value, confidence = s.sentiment(tweet)
			print(tweet, sentiment_value, confidence)

			if confidence*100 >= 80:
				output = open("twitter-out.txt","a")
				output.write(sentiment_value)
				output.write('\n')
				output.close()

			return True

	def on_error(self, status):
		print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["China"])