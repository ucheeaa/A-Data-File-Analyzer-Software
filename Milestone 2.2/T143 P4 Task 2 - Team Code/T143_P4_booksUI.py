# Milestone 2 Lab 2 (P4)
# P4-Task 2: Final Team Code 
# T143:
# Authors:
# Uchenna Obikwelu (101241887)
# Bolo Stephen (101201546)
# Jain Anusha  (101233115)
# Majok Samuel (101249411)



#Imports

from T143_P1_load_data import book_category_dictionary
from T143_P2_add_remove_search_dataset import*
from T143_P3_sorting_fun import*

#Function definitions



#Function Developed by all Team memebers 
def menu()->str:
     """
     Displays the menu of commands for the interface.
     """
     a = "  1- L)oad file '\n' 2- A)dd book '\n' 3- R)emove book '\n' 4- G)et book  '\n'      T)itle R)ate A)uthor P)ublisher C)ategory '\n' 5- GCT) Get all Categories for book Title '\n' 6- S)ort book'\n'      T)itle R)ate P)ublisher A)uthor '\n' 7- Q)uit '\n' \n' Please type your command: "
     
     return a




#Function Developed by Bolo Stephen (101201546) and Majok Samuel (101249411)
def get_books(command:str)->dict:
     """
     After the user types the command G from the user_interface, the user would be prompted to Get Books by: T,R,A,P,C,or GCT from user_interface and would be further be prompted to type a title, a rate, an author, a publisher, or a category and then appropriate function will be called.
     
     """
     book=book_category_dictionary('google_books_dataset.csv')
     
     if command=='T':
          t=input("Enter a title: ")
          get_books_by_title(book,t)
     if command=='R':
          r=input("Enter a rating: ")
          get_books_by_rate(book,float(r))
     if command=='A':
          a=input("Enter an author: ")
          get_books_by_author(book,a)   
     if command=='P':
          p=input("Enter a publisher: ")
          get_books_by_publisher(book, p)
     if command=='C':
          c=input("Enter a category: ")
          get_books_by_category(book,c) 
     if command=='GCT':
          gct=input("Enter a title: ")
          get_all_categories_for_book_title(book,GCT)     
     return 




#Function Developed by Jain Anusha  (101233115)
def sort_books(arrange:str)->dict:

     """
     After the user types the command S from user_interface, the user will be prompted to type the sub-command Sort by: t,r,a or p, and then the appropriate function will be called.
     """
     y = book_category_dictionary('google_books_dataset.csv')
    
     if arrange == 'T':
          title= sort_books_title(y)
          print(title)
        
     if arrange == 'R':
          asc = sort_books_ascending_rate(y)
          print(asc)
            
     if arrange == 'A':
          author = sort_books_author(y)
          print(author)
    
     if arrange == 'P':
          publish = sort_books_publisher(y)
          print(publish)





#Function Developed by all Team memebers    
def user_interface()->dict:
     """
     An interface for customizing the dictionary.
     """
     book=book_category_dictionary('google_books_dataset.csv') #The Filename
     x = True
     
     while x == True:
          data = input(menu())
          if data.upper() != 'Q':
               if data.upper() == 'L':
                    file= input("Enter filename: ")
                    y = book_category_dictionary(file)  
                    data = input('Please type your command: ')
                    if data.upper() == 'A':
                         title=input("To Add book; first, enter the title: ")
                         author=input("Then the author: ")
                         rating=float(input("Then the rating: "))
                         publisher=input("Then the publisher:")
                         pages=int(input("Then the pages: "))
                         category=input("Then the category: ")
                         language=input("Finally the language: ")
                         add_book(book,(title,author,rating,publisher,pages,category,language))
                         
                       
                    if data.upper() == 'R':
                         title=input("Please enter the title of book: ")
                         category=input("category: ")
                         remove_book(book,title,category)
                         
                    if data.upper() == 'G':
                         get = input('Get Books by: ')
                         get_books(get.upper()) 
                    
                    if data.upper() == 'S':
                         arrange = input('Sort by: ')
                         sort_books(arrange.upper()) 
                         
                    else:
                         print('No such command')
               
               
               else:
                    print('File not loaded')
          
          else:
               print('Quiting')
               x = False   
     return 
user_interface()







    
        
