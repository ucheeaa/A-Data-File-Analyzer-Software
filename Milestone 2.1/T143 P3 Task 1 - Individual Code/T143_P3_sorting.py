#P3 Task 1:Sorting - Individual function (Milestone 2 Lab 1) (P3)
#Function 3: sort_books_author
#T143:
#Author:Uchenna Obikwelu (101241887)

from T143_P1_load_data  import  book_category_dictionary

def sort_books_author(my_dictionary: dict) -> list[dict]:
    
    """
    Returns a list with the book data stored as a dictionary sorted in alphabetical
    order relative to the author, based on the "my_dictionary" dictionary argument.
    >>>sort_books_author(my_dictionary)
    [{'title': 'Twas The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit This is Going to Hurt', 'author': 'Adam Kay', 'rating': 4.7, 'publisher': 'Pan Macmillan', 'pages': 112, 'language': 'English', 'category': 'Humor'}, 
    {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'language': 'English', 'category': 'Detective'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'language': 'English', 'category': 'Fiction'},
    {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'language': 'English', 'category': 'Mystery'}, 
    {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'pages': 224, 'language': 'English', 'category': 'Thrillers'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'language': 'English', 'category': 'Classics'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'language': 'English', 'category': 'Detective'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'language': 'English', 'category': 'Fiction'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'pages': 208, 'language': 'English', 'category': 'Horror'},
    ...
    {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'rating': 4.6, 'publisher': 'Harper Collins', 'pages': 224, 'language': 'English', 'category': 'Economics'}, 
    {'title': 'Financial Statements. Revised and Expanded Edition: A Step-by-Step Guide to Understanding and Creating Financial Reports', 'author': 'Thomas Ittelson', 'rating': 4.0, 'publisher': 'Red Wheel/Weiser', 'pages': 288, 'language': 'English', 'category': 'Economics'}, 
    {'title': 'We', 'author': 'Yevgeny Zamyatin', 'rating': 4.3, 'publisher': 'Pan', 'pages': 226, 'language': 'English', 'category': 'Fantasy'}, 
    {'title': 'We', 'author': 'Yevgeny Zamyatin', 'rating': 4.3, 'publisher': 'Pan', 'pages': 226, 'language': 'English', 'category': 'Fiction'}, 
    {'title': 'Selling 101: What Every Successful Sales Professional Needs to Know', 'author': 'Zig Ziglar', 'rating': 3.8, 'publisher': 'HarperCollins Leadership', 'pages': 112, 'language': 'English', 'category': 'Business'}]

    """
    
    
    book_list = [] 
    for key, books in my_dictionary.items():
        for book in books:
            book.update({"category": key}) 
            book_list.append(book) 
    
    length = len(book_list) 
    for i in range(length):
        for elem in range(length-i-1): 
            if book_list[elem].get("author") == book_list[elem + 1].get("author"): 
                if book_list[elem].get("title") > book_list[elem + 1].get("title"):
                    book_list[elem], book_list[elem + 1] = book_list[elem + 1], book_list[elem]
            
                elif book_list[elem].get("title") == book_list[elem + 1].get("title"): 
                    if book_list[elem].get("category") > book_list[elem + 1].get("category"):
                        book_list[elem], book_list[elem + 1] = book_list[elem + 1], book_list[elem]                  
            
            if book_list[elem].get("author") > book_list[elem + 1].get("author"):
                book_list[elem], book_list[elem + 1] = book_list[elem + 1], book_list[elem]
    
    return book_list








    
    