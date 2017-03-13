from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
from elasticsearch import Elasticsearch, RequestsHttpConnection
import requests

consumer_key = 'RP3ZNSHdjd0LH0RlMS3rhpSo1'
consumer_secret = 'i78LTPwoIbWs7zn8Do5E2Eb2uZqOTWnW8LUH7WcFk1MyAnNR5b'
access_token = '2509163336-HXCvtWS2pJ4Jo234RjFIh5ii4c8JX71FOPWqE21'
access_token_secret = 'tMf1c9s0guQMU8gKhwJI31bl4EIphfRF5jBmBMxMcZ8q3'


class MyStreamListener(StreamListener):

	def on_status(self, status):
		twitts = status.text
		coordinates = status.coordinates

		if status.place:
			if coordinates is not None and len(coordinates) > 0:
				coordinates = status.coordinates['coordinates']
				print 'coordinates: ', coordinates

				upload_data = {
					"twitts": twitts,
					"coordinates": coordinates
				}
				print requests.post('http://search-mapapp-ngnudw3cbpxlbtuzbknlvcgujy.us-east-1.es.amazonaws.com/twittermap/data', json=upload_data)

		return True
		

	def on_error(self, status):
		print 'error:', status


	on_event = on_status

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

myStream = Stream(auth, MyStreamListener())
myStream.filter(track=['nike','adidas','vans','movie','drink','burger king','chinese food','theatre',
                        'ktv','machine','gym','weekend','app','weichat','camel','marlboro','china','cs',
                         'travel','location','IBM','google','amazon','fish','hp','apple','iphone','pizza','money',
                        'train','subway','car','nyu','new york','election','dota','lol','game','party',
                        'icloud','google drive','twitter','instagram','snapchat','message','facebook','nba',
                       'microsoft','technology', 'weather','cloudy','rain','snow','food','baseball', 'football','tennis',
                      'sports','america','restaurant','hotel','song','taix','bike','devil may cry',
                     'nodejs','java','python','django','github','news','computer','health','medicine'])
