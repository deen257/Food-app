""" import requests

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/complexSearch"

querystring = {"query":"pasta"}

headers = {
	"X-RapidAPI-Key": "892d2b1eb4msh63efd0ae16a2eeap10571djsn614cb16b3874",
	"X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text) """

languages = [
    {
        "Python": "Machine Learning",
        "R": "Machine learning",
    },
    {
        "Python": "Web development",
        "Java Script": "Web Development",
        "HTML": "Web Development"
    },
    {
        "C++": "Game Development",
        "Python": "Game Development"
    },
    {
        "Java": "App Development",
        "Kotlin": "App Development"
    }
]
 
# iterate over the list
for  val in range(len(languages)):
	value = languages[val]["Python"]
	# for keys in languages[val]:
	print (value)
			#["Python"]