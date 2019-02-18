import pickle

filestring = ["object1", "object2", "object3"]

filename = "myfile.dat"
myfile = open(filename, "wb")

pickle.dump(filestring, myfile)
myfile.close()

del filestring

myfile = open(filename, "rb")

readstring = pickle.load(myfile)
print(readstring) 
