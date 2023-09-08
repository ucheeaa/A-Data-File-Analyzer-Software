# Milestone 1-P1
# P1-Task 4-Code Review-Team submission  
# T143:
# Author:Uchenna Obikwelu (101241887)
# Reviewed by;
# Team members:
# Bolo Stephen (101201546)
# Jain Anusha  (101233115)
# Majok Samuel (101249411)


#FUNCTION DEFINITIION FOR P1 Task 3: Reading the data set(CASE 1)
def book_category_dictionary(filename:str)->dict:
    """
    Returns a dictionary based on the dictionary key 'categories'.
    
    >>>book_category_dictionary('google_books_dataset.csv')
    {"Fiction":[ {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery",
                            "author": " Barbara Allan",
                            "language ": "English",
                            "rating": 3.3,
                            "publisher": " Kensington Publishing Corp.",
                            "pages": 288},
                 {"title": "The Painted Man (The Demon Cycle. Book 1)",
                            "author": " Peter V. Brett",
                            "language ": "English",
                            "rating": 4.5,
                            "publisher": " HarperCollins UK",
                            "pages": 544},
                {another element},
                         ...
                             ],
    "Biography":[ {"title": "The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit",
                            "author": " Adam Kay",
                            "language": "English",
                            "rating": 4.7,
                            "publisher": "Pan Macmillan",
                            "pages": 112},
                 {another element},
                         ...],
    ....
                         }
    """
    
    file=open('google_books_dataset.csv', 'r')
    l0,l1,l2,l3,l4,l5,l6=[],[],[],[],[],[],[]
    for line in file:
        listDetails = line.strip().split(',')
        l0.append(listDetails[0])
        l1.append(listDetails[1])
        l2.append(listDetails[2])
        l3.append(listDetails[3])
        l4.append(listDetails[4])
        l5.append(listDetails[5])
        l6.append(listDetails[6])
    cat= list(set(l5[1:]))
    dic={}
    for i in range(len(cat)):
            dic[cat[i]]= []
    for j in range(len(cat)):
        for i in range(1,len(l5)):
            if cat[j]==l5[i]:
                if l2[i] != 'N/A':
                    new={l0[0]: l0[i],l1[0]: l1[i],l2[0]:float(l2[i]),l3[0]: l3[i],l4[0]: int(l4[i]),l6[0]: l6[i]}
                else:
                    new={l0[0]: l0[i],l1[0]: l1[i],l2[0]:l2[i],l3[0]: l3[i],l4[0]: int(l4[i]),l6[0]: l6[i]}
                    
                dic[cat[j]].append(new)
    file.close()
    return dic


                



                
