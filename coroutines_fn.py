def show():
    book="hello this is vishal patil"
    import time
    time.sleep(5)


    while(True):
        text=(yield)
        if text in book:
            print("your text is in the book")
        else:
            print("Your text is not in the book")

search=show()
print("search started")

print("Searching........")
from clear_screen_in_python import clear

next(search)
clear()
search.send("vishal")

input("press any key")
search.send("this is")

input("press any key")
search.send("this isss")

input("press any key")
search.send("this is vishal")

search.close()