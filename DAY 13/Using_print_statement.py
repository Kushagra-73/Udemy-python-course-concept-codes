# word_per_page=0
# pages=int(input("No. of pages :"))
# word_per_page==int(input("No. of words per page :"))
# total_words=pages*word_per_page

# print(total_words)

"""
No. of pages :10
No. of words per page :200
0


It should have returned 2000 in the output but instead returns 0 
this is because we used == which find whether condition is True or False
not equals to any value 
"""

# Revisead Code
word_per_page=0
pages=int(input("No. of pages :"))
word_per_page=int(input("No. of words per page :"))
total_words=pages*word_per_page

print(total_words)
