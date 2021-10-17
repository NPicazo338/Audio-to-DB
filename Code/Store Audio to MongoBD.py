import os                               #load all music from audio folder
from pymongo import MongoClient as mc   #MongoClient
from gridfs import GridFS               #GridFS object


#file extension
extension = '.mp3'

#location
direc = "E:\Music\CD"




def artist_names(direc = direc):
	'''
	Getting artist names from directory
	'''

	names = []


	for root, dirs, files in os.walk(direc):

		#taking folder names (artist names)
		for sub in dirs:

			names.append(sub)


	return names




def store_Mongo(direc = direc, extension = extension, names):
	'''
	Storing audio into database called Audio_DB using GridFS

	This saves all audio within CD folder
	'''

	#connecting to MongoDB and creating Audio_DB
	db = mc().Audio_DB

	#GridFS object
	fs = GridFS(db)


	#saving all files with .mp3 extension
	for root, dirs, files in os.walk(direc):


		for file in files:


			#saving only .mp3
			if extension in file:

				#taking artist name from location and joining with song name
				name = os.path.join(root, file).split("\\")
				s_name = str(name[3] + '_' + file[3:])


				#storing audio in Audio_DB
				fs.put(open(os.path.join(root, file), 'rb'), filename = s_name)





if __name__ == '__main__':

	song_names = artist_names()

	store_Mongo()
