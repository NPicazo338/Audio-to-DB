import requests as req                  #http request
from bs4 import BeautifulSoup as bs     #scrape

#website
url = 'https://freemusicarchive.org/home'




def scrape_items(url = url):
	'''
	scrape song items from the main page (Featured Songs)
	'''

	#beautifulsoup object passing url request
	soup = bs(req.get(url).content, 'html.parser')

	#taking song items
	song_items = soup.find_all('span'. {'class': 'playicn'})


	#extracting data-url from every song item included in the main page
	song_links = []


	for i in range(len(song_items)):

		#append data-urls
		song_links.append(song_items[i].find('a').get('data-url'))


	return song_links




def download_songs(song_links):
	'''
	download all songs
	'''

	for i in range(len(song_links)):

		#popup req
		pop_req = req.get(str(song_links[i]))

		#BeautifulSoup object
		downsoup = bs(pop_req.text, 'html.parser')

		#dl req
		down_req = req.get(str(downsoup.find('a', {'class': 'download'}).get('href')))

		#song name
		song_name = downsoup.find('div', {'class': 'text'}).find('h2').text

		#artist name
		artist_name = downsoup.find('div', {'class': 'text'}).find('h3').find('a').text

		#file name
		file_name = "(" + artist_name.strip() + ")" + " " + song_name


		#downloading song
		try:
			with open(file_name + '.mp3', 'wb') as f:

				f.write(down_link.content)

		except:
			print('Could not download song')





if __name__ == '__main__':

	song_links = scrape_items()

	download_songs(song_links)