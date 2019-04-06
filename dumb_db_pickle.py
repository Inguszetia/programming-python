import pickle
#this script shows how to access the pickled database after it has been created
#open the file and pass content bach to pickle to remake
#the object from its serialized string
dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])