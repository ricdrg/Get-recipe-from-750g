'''
The purpose of this project is to use web scrapping methods to get recipes
from a french cooking website (750g.com) because I love cooking :) !
The requirements : beautifulsoup, requests and lxml modules
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
Getting recipe's title
'''
headline = article.h1.text #workingline

'''
Getting ingredients content
'''
ingredients = article.find('div', class_='c-recipe-ingredients') #workingline
#for ingredients in article.find_all('div', class_='c-recipe-ingredients'):
    #ingredients_title = ingredients.h3
#    print(ingredients.prettify())
#    ingredients_title = ingredients.find('h3', class_='c-recipe-ingredients__title')
#    ingredients_list = ingredients.find('ul', class_='c-recipe-ingredients__list').li
#    print(ingredients_title)
#    print(ingredients_list)



#print(ingredients.prettify())

#ingredients_title = article.find('div', class_='c-recipe-ingredients').h3.text
#print(ingredients_title)
#ingredients_title = ingredients.find('h3', class_='c-recipe-ingredients__title')

'''
Iterating through ingredients content to gather ingredients title and ingredients list
in order to assemble these datas into a dictionnary
'''
ingrtitle = list()
#getting ingredients titile
for ingredients_title in ingredients.find_all('h3', class_='c-recipe-ingredients__title'):
    ingrtitle.append(ingredients_title.text)

ingrlist = list()
#getting ingredients list
for ingredients_list in ingredients.find_all('ul', class_='c-recipe-ingredients__list'):
    ingrlist.append(ingredients_list.text)




import re #using regular expression to adjust the output
for i in range(len(ingrlist)):
    ingrlist[i] = re.findall('[A-Z0-9]+.[a-zàâçéèêëîïôûùüÿñæœ\'\(\) .-]+', ingrlist[i])
    print(ingrlist[i])




#ingredients_title = list() ####working
#for title in ingredients('h3'):
#    ingredients_title.append(title.text)







#ingredients_list = ingredients.split('<li>')
#print(ingredients_list)

#steps = article.find('ol', class_='c-recipe-steps__list').text
#print(steps)

    #steps = article.find('h4', class_='c-recipe-steps__item-title').text
#print(steps)

#steps_list = steps.find('li', class_='c-recipe-steps__item js-popin-pap u-pointer').text
#print(steps_list)
