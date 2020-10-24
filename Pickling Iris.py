import requests,pickle

r=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# print(r.text.split("\n"))
# response=r.text.splitlines() # r.text.split("\n")

response=[[i] for i in r.text.splitlines() if len(i)!=0]

# pickling the file object

with open("PicklingIris.pkl",'wb') as f:

    pickle.dump(response,f)

with open("PicklingIris.pkl",'rb') as f:

    r2=pickle.load(f)

print(r2)

