import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

querystring = {"ingredients":"apples,flour,sugar","number":"5","ignorePantry":"true","ranking":"1"}

headers = {
	"X-RapidAPI-Key": "892d2b1eb4msh63efd0ae16a2eeap10571djsn614cb16b3874",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.json())