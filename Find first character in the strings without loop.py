'''Find first character of every in the string 
without using loop and return these characters 
in capital form '''
def find_index(Cap):
 find_char=Cap[0:1:1]
 return find_char.capitalize()
Cap=input("Enter any string: ")
result=map(find_index, Cap.strip().split())
print(str(list(result)))