from pymongo import MongoClient as mc
from gridfs import GridFS
import IPython.display as ipd


#database name
database = 'Audio_DB'




def connect_mongo(database):
	'''
	Connect to mongodb and audio database
	'''

	#connecting to mongodb
	mongo = mc('localhost', 27017)

	#connecting to audio database
	db = mongo[database]

	#gridfs object
	fs = GridFS(db)

	return fs




def reading_audio(fs):
	'''
	Reading song from audio database
	'''

	while True:

		try:

			#taking a song name
			songname = input('Enter Song Name: ')

			#taking an artist name
			artname = input('Enter Artist Name: ')

			#file name within mongodb
			filename = artname + '_' + songname + '.mp3'

			#retrieving song by filename within mongo
			song = fs.find_one({'filename': str(filename)})

		except:

			print('Song Not Found.')

		else:

			return song

			break





if __name__ == '__main__':

	fs = connect_mongo(database)

	song = reading_audio(fs)

	ipd.Audio(song.read())
