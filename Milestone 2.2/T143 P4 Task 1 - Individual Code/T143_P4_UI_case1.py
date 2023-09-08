#P4 Task 1 - Milestone Planning and Individual Code
#CASE 1
#T143:
#Author:Uchenna Obikwelu (101241887)



from T143_P2_add_remove_search_dataset import add_book  
from T143_P2_add_remove_search_dataset import remove_book
from T143_P1_load_data import book_category_dictionary

def menu()->str:
     """
     Displays the menu of commands for the interface.
     """
     a = "  1- Command Line L)oad file '\n' 2- Command Line A)dd book '\n' 3- Command Line R)emove book '\n' 4- Command Line G)et book  '\n'    T)itle R)ate A)uthor P)ublisher C)ategory '\n' 5-GCT) Get all Categories for book Title '\n' 6- Command Line S)ort book'\n'    T)itle R)ate P)ublisher A)uthor '\n' 7- Command line Q)uit '\n' Please type your command: "
     return a


     
def user_interface()->dict:
     """
     An interface for customizing the dictionary.
     """
     book=book_category_dictionary('google_books_dataset.csv')
     x = True
     
     while x == True:
          data = input(menu())
          if data.upper() != 'Q':
               if data.upper() == 'L':
                    file= input("Enter filename: ")
                    y = book_category_dictionary(file)  
                    data = input('Please type your command: ')
                    if data.upper() == 'A':
                         title=input("To add book;Enter the title: ")
                         author=input("Enter the author: ")
                         rating=float(input("Enter the rating: "))
                         publisher=input("Enter the publisher:")
                         pages=int(input("Enter the pages: "))
                         category=input("Enter the category: ")
                         language=input("Enter the language: ")
                         add_book(book,(title,author,rating,publisher,pages,category,language))
                         
                       
                    if data.upper() == 'R':
                         title=input("Please enter the title of book: ")
                         category=input("category: ")
                         remove_book(book,title,category)
               else:
                    print('File not loaded')
          
          else:
               print('Quiting')
               x = False   
     return 
user_interface()

