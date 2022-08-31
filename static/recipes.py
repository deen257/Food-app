from http.client import responses
from multiprocessing.sharedctypes import Value
from turtle import title
import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"

#querystring = {"query":"eggs"}
headers = {
	"X-RapidAPI-Key": "c14fe3bed8msh8003ce15f939219p1cbadbjsn71738d9aab2e",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

#response = requests.request("GET", url, headers=headers, params=querystring)


def lookup():
    querystring = {"query":'eggs'}
    response = requests.request("GET", url, headers=headers, params=querystring)
    quote = response.json()
    responses = quote['results']
    return responses

drink = lookup()

#print(drink)
answ={}
for elements in drink:
    answ.update({elements['title']: elements['image']})

print(answ)

#title = responses['title']
#for titles in responses:
    #print(titles)

