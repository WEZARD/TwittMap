from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

keywords = ['Sports, football, basketball, tennis, baseball, nba',
            'Game, data, lol, cs, devil may cry',
            'Technology, nodejs, java, python, database',
            'Weather, cloudy, rain, snow',
            'Food, restaurant, burger king, pepsi, chinese food, drink, pizza',
            'Fun, movie, ktv, theatre, bar, camel, marlboro',
            'Traffic, car, train, subway, bike',
            'Location, nyu, new york, usa, china',
            'App, twitter, facebook, weichat, snapchat, instagram',
            'Company, IBM, amazon, google, apple, hp, microsoft']


def index(request):
    return render(request, 'MapApp/map.html', {'app_name': 'TwittMap'})


def handle(es_request):
    if es_request.method == "POST":
        message = es_request.POST.get('Search', None)

        def search(url, term):
            uri = url + term
            response = requests.get(uri)
            results = json.loads(response.text)
            return results

        if message == 'Sports':
            keyword_index = 0
        elif message == 'Game':
            keyword_index = 1
        elif message == 'Technology':
            keyword_index = 2
        elif message == 'Weather':
            keyword_index = 3
        elif message == 'Food':
            keyword_index = 4
        elif message == 'Fun':
            keyword_index = 5
        elif message == 'Traffic':
            keyword_index = 6
        elif message == 'Location':
            keyword_index = 7
        elif message == 'App':
            keyword_index = 8
        elif message == 'Company':
            keyword_index = 9

        domain= 'http://search-mapapp-ngnudw3cbpxlbtuzbknlvcgujy.us-east-1.es.amazonaws.com/twittermap/_search?size=9999&pretty=true&q='
        result = search(domain, keywords[keyword_index])
        c_data = [res['_source']['coordinates'] for res in result['hits']['hits']]
        t_data = [res['_source']['twitts'] for res in result['hits']['hits']]

        hits = len(c_data)
        length = {'hits': hits}
        coordinates = {}
        twitts = {}

        for i in range(hits):
            if (c_data[i][0] < -90):
                c_data[i][0] += 180
            coordinates[i] = {'lat': c_data[i][1], 'lng': c_data[i][0]}
            twitts[i] = t_data[i]

        data = {'coordinates': coordinates, 'length': length, 'twitts': twitts}

        return JsonResponse(data)
