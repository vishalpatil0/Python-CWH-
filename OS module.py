import os

# print(dir(os))

print(os.getcwd()) #current working directory

# os.chdir("/home/vishal") #change cwd

print(os.getcwd())

print(os.listdir("/home/vishal/git/"))  #show all the folder and files in the given location

os.mkdir("vishu") #create folder
os.rmdir("vishu") #delete folder
os.makedirs("vishu/namu")  #create directories within directories
os.removedirs("vishu/namu")


# os.rename("even odd.py","even-odd.py") to rename files

print(os.environ.get('Path'))

print(os.path())