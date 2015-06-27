import requests, re, sys
from bs4 import BeautifulSoup 

mov = {}
movID = sys.argv[1]

url = "http://www.imdb.com/title/" + movID
data = requests.get(url).text
soup = BeautifulSoup(data)

links = soup.find_all('h1', class_ = "header")
for link in links:
	mov['title'] = link.contents[1].string
try:
	links = soup.find_all('a', title = "See all release dates")
	for link in links:
		mov['date'] = link.contents[0]
except IndexError:
	mov['date'] = 'Not Specified'


classname = "titlePageSprite star-box-giga-star"
links = soup.find_all('div', class_ = classname)
for link in links:
	mov['rating'] = link.contents[0].string

mov['genres'] = []
links = soup.find_all('span', class_ = "itemprop", itemprop = "genre")
try:
	for link in links:
		mov['genres'].append(link.string)
except IndexError:
	mov['genres'] = 'Not Specified'


links = soup.find_all('a', href = re.compile("criticreviews"))
try:
	mov['metacritic'] = links[0].string
except IndexError:
	mov['metacritic'] = 'Not Specified'


links = soup.find_all('p', itemprop = "description")
try:
	for link in links:
		mov['description'] = link.string
except IndexError:
	mov['description'] = 'Not Specified'


mov['duration'] = []
links = soup.find_all('time', itemprop = "duration")
try:
	for link in links[1:]:
		mov['duration'].append(link.string)
except IndexError:
	mov['duration'] = 'Not Specified'


try:
	links = soup.find_all('h4', class_ = "inline", text = "Taglines:")
	mov['tagline'] = links[0].next_sibling
except IndexError:
	mov['tagline'] = "Not Specified"


links = soup.find_all('span', itemprop = "contentRating")
try:
	for link in links:
		mov['cont_rating'] = link.string
except IndexError:
	mov['cont_rating'] = 'Not Specified'


mov['director'] = []
links = soup.find_all('h4', class_ = 'inline', text = ['Director:', 'Directors:'])
for link in links[0].next_siblings:
	try:
		mov['director'].append(link.contents[0].contents[0])
	except:
		fubar = 1


mov['writer'] = []
links = soup.find_all('h4', class_ = 'inline', text = ['Writer:', 'Writers:'])
for link in links[0].next_siblings:
	try:
		mov['writer'].append(link.contents[0].contents[0])
	except AttributeError:
		fubar = 1    #Placeholder statement inside except block.


mov['actor'] = []
links = soup.find_all('h4', class_ = 'inline', text = "Stars:")
for link in links[0].next_siblings:
	try:
		mov['actor'].append(link.contents[0].contents[0])
	except AttributeError:
		fubar = 1



sp = "\n"
print('Movie Details:' + sp)
print('Title: ' + mov['title'] + sp)
print('Director(s): ')
for i in mov['director']:
	print(i)
print(sp)

print('Writer(s): ')
for i in mov['writer']:
	print(i)
print(sp)

print("Actors: ")
for i in mov['actor']:
	print(i)
print(sp)

print('Release Date: ' + mov['date'] + sp)
print('IMDb rating: ' + mov['rating'] + sp)
print('Genre(s): ')
for i in mov['genres']:
	print(i)
print(sp)

print('Metacritic Rating: ' + mov['metacritic'] + sp)
print('Descripition: ' + mov['description'] + sp)
print('Runtime: ')
for i in mov['duration']:
	print(i)
print(sp)

print('Tagline: ' + mov['tagline'] + sp)
print('Content Rating: ' + mov['cont_rating'] + sp)




