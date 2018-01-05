import sys
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


ckey = '26gc07ukuTiZak7hxlL3mAi6W'
csecret = 'xey8XwLFxnvlLq3Wr2WQ246mLZtQWLnD1K1qCAlilPlrXkVecW'
atoken = '3159868009-5ODrdsb4kJTfPUyUfFK2I1f97LKt6enQt7aRN4A'
asecret = 'YqXpfdmG518w8vpKWIJQl2bgOLtH262r70Wn58JbKsK2S'

orig_stdout = sys.stdout
f = open('datum.json', 'w')
sys.stdout = f


class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self,status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken,asecret)
twitterStream = Stream(auth, listener())
print(twitterStream.filter(track = ["a"]))

sys.stdout = orig_stdout
f.close()


