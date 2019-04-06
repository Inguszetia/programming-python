from Database import db
import pickle
#this script stores the entire database to a flat file named people-pickle
#in the current working directory
#pickle module convert the object to a string
dbfile = open('people-pickle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()