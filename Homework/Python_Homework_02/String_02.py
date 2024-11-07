# using translate to change latters in given string
# str.maketrans used to create map/list for method translate str.maketrans(x,y,x) : x-string to replace, y-string to replace with, z - string to delete
Sentence=input("Enter the string: ")
vowels='aeiouAEIOU'
print(Sentence.translate(str.maketrans('','',vowels)))
