import requests

# r=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
#
# print(r.text)
# print(r.status_code)  #requests code 200 means it  is ok

url="https://www.facebook.com/"

data={
        1:1
}

r2=requests.post(url=url,data=data)

print(r2.status_code)

