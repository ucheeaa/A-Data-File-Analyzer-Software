#P2 Task 1 - Individual function (Milestone 1 Lab 2) (P2)
#Function 1: add_book; Function 2: remove_book )
#T143:
#Author:Uchenna Obikwelu (101241887)


from T143_P1_book_category_dictionary import  book_category_dictionary
my_dictionary=(book_category_dictionary('google_books_dataset.csv'))


#FUNCTION DEFINITION FOR FUNCTION 1
def add_book(my_dictionary:dict, tup:tuple)->dict:
    """
    The function adds the book to the dictionary and verifies that the book has been added. The function
    returns the updated dictionary and prints a message stating, “The book has been added
     correctly” or “There was an error adding the book”.
     
    >>>add_book(my_dictionary,("Ulysses","James Joyce","4.5","Sylvia Beach","306","Psychologyyy","English"))
    There was an error adding the book
    {my_dictionary}
    
    
    
    >>>add_book(my_dictionary,("Ulysses","James Joyce","4.5","Sylvia Beach","306","Psychology","English"))
    The book has been added correctly
    {updated my_dictionary}
    
    """
    keys= list(my_dictionary.keys())
    values= list(my_dictionary.values())
    if tup[5] in keys:
        k= list(my_dictionary[tup[5]][0].keys())
        new={k[0]: tup[0],k[1]: tup[1],k[2]: tup[2],k[3]: tup[3],k[4]: tup[4],k[5]: tup[6] }
        my_dictionary[tup[5]].append(new)
        print("The book has been added correctly")
              
    else:
        print("There was an error adding the book")
    
    return my_dictionary



#FUNCTION DEFINITION FOR FUNCTION 2
def remove_book(my_dictionary:dict,title:str,category:str)->dict:
    """
    The function returns the updated dictionary and prints a message stating, “The book has been removed correctly” or “There was an error
    removing the book. Book not found
    
    >>>remove_book(my_dictionary,'How To Win Friends and Influence People',"Psychology")
    The book has been removed correctly
    {updated dictionary}
    
    >>>remove_book(my_dictionary,'Spider-Man: Anti-Venom',"Superheroes")
    The book has been removed correctly
    {updated dictionary}
    

    >>>remove_book(my_dictionary,'PlayStation',"Investing")
    There was an error removing the book. Book not found.
    {updated dictionary}
    """
    

         
    
    if category in my_dictionary.keys():
        for i in range(len(my_dictionary[category])):
            if my_dictionary[category][i]['title'] == title:
                del my_dictionary[category][i]
                print("The book has been removed correctly")
                break
        else:
            print("There was an error removing the book. Book not found.")

    return my_dictionary

