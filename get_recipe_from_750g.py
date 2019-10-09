'''
The purpose of this project is to use web scrapping methods to get recipes
from a french cooking website (750g.com) because I love cooking :) !
The requirements : beautifulsoup, requests and lxml modules

1° prompt user to type the recipe wished
2° find a match from datas types by the user
3° getting web page informations
4° sort it to a csv or a GUI

Currently the only step done is the web scrapping part
'''

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.750g.com/noix-de-saint-jacques-en-chapelure-de-lard-et-creme-de-cancoillotte-r205749.htm').text
#with open('Recette - Noix de Saint-Jacques en chapelure de lard et crème de cancoillotte   750g.html') as html_file:
soup = BeautifulSoup(source, 'lxml')

'''
Récupération du contenu qui nous intéresse, en l'occurence la balise 'article'
'''
article = soup.find('article') ##working line
#print(article.prettify())



'''
Getting recipe's title, difficulty, summary, preparation and cooking time, servings size
'''
headline = article.h1.text
#print(headline)

summary = article.find('div', class_='summary').p.text
#print(summary)

difficulty = article.find('li', class_='c-recipe-summary__rating', title='Difficulté').text
print(difficulty)

time_preparation = article.find('li', class_='c-recipe-summary__rating', title='Coût').text
print(time_preparation)

time_cook = article.find('li', class_='c-recipe-summary__rating', title='Temps de préparation').text
print(time_cook)

servings = article.find('span', class_='c-ingredient-variator-label').text
print(servings)



'''
Getting ingredients content
'''
ingredients = article.find('div', class_='c-recipe-ingredients')
#print(ingredients.prettify())


'''
Iterating through ingredients content to gather ingredients title and ingredients list
in order to assemble these datas into a dictionnary (or into 2 python lists)
'''
ingredients_title = list()
#getting ingredients title
for ingr_title in ingredients.find_all('h3', class_='c-recipe-ingredients__title'):
    ingredients_title.append(ingr_title.text)

ingredients_list = list()
#getting ingredients list
for ingr_list in ingredients.find_all('ul', class_='c-recipe-ingredients__list'):
    ingredients_list.append(ingr_list.text)


import re #using regular expression to adjust the output
for i in range(len(ingredients_list)):
    ingredients_list[i] = re.findall('[A-Z0-9]+.[a-zàâçéèêëîïôûùüÿñæœ\'\(\) .-]+', ingredients_list[i])
    print(ingredients_list[i])

ingredients_dict = dict(zip(ingredients_title, ingredients_list)) #dictionnary creation with both lists
#print(ingredients_dict)



'''
Collecting material list needed to prepare the recipe
'''
material_title = article.find('h2', class_='u-title-section u-green u-margin-bottom u-margin-vert@tablet').text
print(material_title)

material_list = list()
for list in article.find_all('li', class_='u-padding-bottom-5px'):
    material_list.append(list.text)

print(material_list)


'''
Getting recipe's content
'''
recipe = article.find('div', class_='c-recipe-steps')
#print(recipe.prettify())

for recipe_steps in recipe.find_all('li', class_='c-recipe-steps__item js-popin-pap u-pointer'):
    #print(recipe_steps)
    recipe_steps_title = recipe_steps.find('span', class_='c-recipe-steps__item-title-step').text
    print(recipe_steps_title)

    recipe_content = recipe_steps.find('div', class_='c-recipe-steps__item-content').p.text
    print(recipe_content)
