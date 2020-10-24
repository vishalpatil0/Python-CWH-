import pickle
#pickling python object
cars =["bmw","audi","maruti suzuki","nano"]
file="mycar.pkl"

fileobj=open(file,'wb')

pickle.dump(cars,fileobj)

fileobj.close()


file="mycar.pkl"

fileobj=open(file,'rb')

mycar=pickle.load(fileobj)
print(mycar)
fileobj.close()