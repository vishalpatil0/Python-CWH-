import string,random

if __name__ == '__main__':
    s=string.ascii_letters+string.digits+string.punctuation
    s=list(s)
    random.shuffle(s)
    print(s)
    len=int(input("Enter the length of password = "))
    print(''.join(s[0:len]))
    #another way to do that

    print(''.join(random.sample(s,len)))
