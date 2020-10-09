import random as rndm
class library:
    listofbooks = {1201:"Harry Potter Series", 2401:"Lord of the Rings Series", 9832:"The Da Vinci code", 3421:"A brief history of Time", 3423:"Sapiens",6543: "Outliers",9807: "Zero To One", 8134:"Awaken the giant Within", 6540:"Titan: The life and times of John D. Rockefeller", 4321:"You are a Badass"}
    avai_books=[]
    
    currently_lend_book={}
    
    def __init__(self,fname,lname,contact_no,address,email):
        self.fname=fname.capitalize()
        self.lname=lname.capitalize()
        self.contact_no=contact_no
        self.address=address
        self.email=email
        for i in self.listofbooks.keys():
            self.avai_books.append(i)
    @property
    def full_name(self):
        if self.fname==None or self.lname == None:
            return "Please provide the details"
        return f"{self.fname} {self.lname}"
    def printdetails(self):
        print(f"Full Name:-{self.full_name}\nContact Number:-{self.contact_no}\nEmail:-{self.email}\nAddress:-{self.address}")
    def show_all_books(self):
        print("All books in library are as follow\n",50*"*")
        print("ID\tName")
        for i,j in self.listofbooks.items():
            print(f"{i} {j}")
    def show_all_avaibooks(self):
        print("All available books in library are as follow\n",50*"*")
        for i in self.avai_books:
            print(f"{i} {self.listofbooks[i]}")     
    def donate_book(self,book_name):
        b_id=rndm.randint(1000,10000)        
        while(b_id in self.listofbooks.keys()):
           b_id=rndm.randint(1000,10000)
        self.listofbooks.update({b_id:book_name})
        self.avai_books.append(b_id)
        print(f"{book_name} is added to the library with id {b_id} ")        
    def lend_book(self,book_name):
        """who owns the book if not present"""
        f=0
        for i in self.avai_books:
            if(book_name==i):
                f=1
                break     
        if f==1:
            self.currently_lend_book.update({i:self.fname})
            self.avai_books.remove(i)
        else:
            for i in self.listofbooks.values():
                if(book_name==i):
                    f=2  
                    break
            if (f==2):    
                print(f"The book you are searching for is currently owned by {self.currently_lend_book[book_name]} ")
            else:   
                print("The book you are searching for is not available in the library.")
    
    def lended_books(self):
        for book,name in self.currently_lend_book.items():
            print(f"{self.listofbooks[book]} borrowed by {name}")    
        
    def return_book(self,book_name):
        f=0
        for name in self.currently_lend_book.keys():
            if name==book_name:
                f=1
        if f==1:
            del self.currently_lend_book[book_name]
            self.avai_books.append(book_name)
        else:
            print("We don't have any entry for this book in out library")        
        
    
def main():
    print("\t\t\t\t\t\tWelcome to Vivekanand Library\n\n")
    vishu=library('vishal','patil',7410760563,"kurha","vishalgpatil10@gmail.com")
    while(True):
        print("\n",50*"*","\n")
        choice=int(input("1-Show all the books in the library\n2-Show only the available books in the library\n3-Donate book\n4-Lend book\n5-Show lended books\n6-Return book\n7-Show your information\n8-Exit"))
        if(choice==1):
            vishu.show_all_books()
        elif choice==2:
            vishu.show_all_avaibooks()
        elif choice==3:
            ip1=input("Enter the name of the book that you want to donate")
            vishu.donate_book(ip1)
        elif choice==4:
            vishu.show_all_avaibooks()
            ip1=int(input("Enter the id of the book that you want to lend"))
            vishu.lend_book(ip1)
        elif choice==5:
            vishu.lended_books()
        elif choice==6:
            ip1=int(input("Enter the id of the book that you want to return"))
            vishu.return_book(ip1) 
        elif choice==7:
            vishu.printdetails()
        elif choice==8:
            break
        else:
            print("Please enter valid choice")    
                       
if __name__=="__main__":
    main()
