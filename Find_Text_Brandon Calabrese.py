"""
Made By: Brandon Calabrese

This program 


You are teaching this class the wrong way. Good programmers do not need to be
told what functions to make specifically and what methods they can and cannot
use. I would be done in 5 seconds making 1 funtion with 2 for loops and not deal
with recursion. You people treat it like you need it in everything and it just
overcomplicates things. Also great choice for variable names - sarcasm
"""

## - means debug print statements
    
def count_text_string(OGString, search_for, search_in, find_count):    
    ##print(str(find_count) + " --- " + search_for + " --- " + search_in)
    if search_in == "":
        return find_count
    
    if search_for == "":       
        find_count += 1
        search_for = OGString
    
    if search_for[0] == search_in[0]:
        ##print("Found character match")
        find_count = count_text_string(OGString, search_for[1:],search_in[1:],find_count)
    else:
        search_for = OGString
        find_count = count_text_string(OGString, search_for,search_in[1:],find_count)
    
    #must use recursion
    #returns number of times that the search string appears in the search_in string
    return find_count

def count_text_file(search_for,text_file_name):
    occurances = 0
    #print lines containing search_for and count of given string in file
    for l in text_file_name:
        num = count_text_string(search_for, search_for,l,0)
        occurances += num
        if num > 0:
            print(l)
    print("")
    print("Number of occurances: " + str(occurances))
    
def main():
    #reads text input and file name
    #must call count_text_file
    count_text_file(input("Enter text: "), open(input("Enter Filename: ")))

main()
