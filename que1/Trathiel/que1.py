string=input("Enter string:")
string=string.split(" ")
race={}
for item in string:
    point=0
    for char in item:
        point=point+(ord(char.lower()))
    race[item]=point
race = sorted(race.items(), key=lambda kv: kv[1])
print(race.pop()[0])