#P2 Task 2 - Individual function (Milestone 1 Lab 2) (P2)
#Testing Function 3 and 4
#T143:
#Author:Uchenna Obikwelu (101241887)



from T143_P1_book_category_dictionary import  book_category_dictionary
from T143_P2_get_books_by_rating import get_books_by_rate
from T143_P2_get_books_by_category import get_books_by_category
from unit_testing import check_equal

def test_get_books_by_category(description:str,expected_result, actual_result):
        """
        Return if a test pass or fail and it will print that information.
        >>> test_get_books_by_category(("get_books_by_category('Horror')",['The Mysterious Affair at Styles']
, get_books_by_category('Horror')))
        True
        
        >>> test_get_books_by_category("get_books_by_category('Thrillers')",['Little Girl Lost: A Lucy Black Thriller', "Final Option: 'The best one yet'", 'The Mysterious Affair at Styles', 'Bring Me Back', 'Total Control', 'The Memoirs of Sherlock Holmes', 'Once Missed (A Riley Paige Mystery Book 16)', 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'After Anna', 'And Then There Were None', "The Girl in the Spider's Web: A Lisbeth Salander novel: continuing Stieg Larsson's Millennium Series", 'The Black Box', 'Shantaram', 'The Painted Man (The Demon Cycle. Book 1)', 'No Mercy: The brand new novel from the Queen of Crime', "'Salem's Lot", 'In Dark Company: A Kate Burkholder Short Story', 'Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)'], get_books_by_category('Thrillers')))
        
        True

        
        """
        if expected_result == actual_result:
                print(description, "pass")
                return True
        else:
                return False   

def test_get_books_by_rate(description:str,expected_result, actual_result):
        """
        Return if a test pass or fail and it will print that information.
        >>> test_get_books_by_rate("get_books_by_rate(5)",['The Red Signal: An Agatha Christie Short Story', "Final Option: 'The best one yet'", 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk', 'No One Is Too Small to Make a Difference'], get_books_by_rate(5))
        
        False
        >>> test_get_books_by_rate("get_books_by_rate(3.3)",['Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything', 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'Mrs. Pollifax Unveiled', "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'Bring Me Back', 'How to Understand Business Finance: Edition 2', 'The Infinite Game', 'Selling 101: What Every Successful Sales Professional Needs to Know'], (get_books_by_rate(3.3)))
        False
        
        >>>test_get_books_by_rate(['Mrs. Pollifax Unveiled', "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'Bring Me Back', 'How to Understand Business Finance: Edition 2', 'Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything', 'The Infinite Game', 'Selling 101: What Every Successful Sales Professional Needs to Know']
        False
        
        """
        if expected_result == actual_result:
                print(description, "pass")
                return True
        else:
                return False   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
   
# Automated Testing for Function 3
   
total_test= 0
test_pass = 0
test_pass+=test_get_books_by_category("get_books_by_category('Horror')",['The Mysterious Affair at Styles']
, get_books_by_category('Horror'))
total_test += 1
test_pass+=test_get_books_by_category("get_books_by_category('Thrillers')",['Little Girl Lost: A Lucy Black Thriller', "Final Option: 'The best one yet'", 'The Mysterious Affair at Styles', 'Bring Me Back', 'Total Control', 'The Memoirs of Sherlock Holmes', 'Once Missed (A Riley Paige Mystery Book 16)', 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'After Anna', 'And Then There Were None', "The Girl in the Spider's Web: A Lisbeth Salander novel: continuing Stieg Larsson's Millennium Series", 'The Black Box', 'Shantaram', 'The Painted Man (The Demon Cycle. Book 1)', 'No Mercy: The brand new novel from the Queen of Crime', "'Salem's Lot", 'In Dark Company: A Kate Burkholder Short Story', 'Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)'], get_books_by_category('Thrillers'))
total_test += 1
test_fail= total_test -test_pass
print("test pass:", test_pass)
print("test fail:", test_fail)


# Automated Testing for Function 4

total_test= 0
test_pass = 0
test_pass+=test_get_books_by_rate("get_books_by_rate(5)",['The Red Signal: An Agatha Christie Short Story', "Final Option: 'The best one yet'", 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk', 'No One Is Too Small to Make a Difference'], get_books_by_rate(5))
total_test += 1
test_pass+=test_get_books_by_rate("get_books_by_rate(3.3)",['Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything', 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'Mrs. Pollifax Unveiled', "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'Bring Me Back', 'How to Understand Business Finance: Edition 2', 'The Infinite Game', 'Selling 101: What Every Successful Sales Professional Needs to Know'], get_books_by_rate(3.3))
total_test += 1
test_pass+=test_get_books_by_rate("get_books_by_rate(3)",['Mrs. Pollifax Unveiled', "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'Bring Me Back', 'How to Understand Business Finance: Edition 2', 'Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything', 'The Infinite Game', 'Selling 101: What Every Successful Sales Professional Needs to Know'], get_books_by_rate(3))
total_test += 1
test_fail= total_test-test_pass
print("test pass:", test_pass)
print("test fail:", test_fail)





#Assume the functions of your teammates are in the imported file.
#=================

#In the imported file, you can define the header with a hard-coded return statement to ensure your test harness work
#Example
   #def add_book(dic, book_data):
   #     return True
#============

#Here you should implement the function check_equal (or similar)


#Here you should have your test for function 3
   #Example:
   # actual = add_book({},("a", "b", "c", "d", "e", "f", "g"))
   # expected = False
   # That was an example where I assume that you case will return false.
   # total_test +=1
   # test_pass += check_equal("test 1", expected, actual) 