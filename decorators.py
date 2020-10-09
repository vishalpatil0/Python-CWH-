"""Notes:::
            Function are not only passed as arguments but also return as arguments """

import time


def dec1(func1):
    def news():
        print("exectuin")
        time.sleep(0.5)
        func1()
        time.sleep(0.5)
        print("executed")
    return news

@dec1
def who_is_vishal():
    print("vishal is a good boy")

# who_is_vishal=dec1(who_is_vishal)    
who_is_vishal()


def abcd():
    pass   ##meaning of pass means nothing