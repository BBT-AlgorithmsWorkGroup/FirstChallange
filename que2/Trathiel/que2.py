string=input("Enter string:")
string=list(map(str, string))
string=set(string)
print(string)
if " " in string:
    string.remove(" ")
print( len(string)==26 )
