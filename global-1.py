#gloval variables

l=19

def abcd():
    g=45
    global l  #global keyword allows us to change the global variable in the function it also create global varaible if it is not present in global scope 
    l=l+231
    print(l,g)

def bg():
    l=l+21
    print('l=',l)

print("fnction opn")
abcd() 
print("second")
try:
    bg()
except Exception as e:
    print("global nahiye variable function bg madhe")    
print("fnction clsig")

print(l)

# function within a function 

def vishal():
    def namrata():
        print("namu")
    print("vishu")
    namrata()

vishal();   
