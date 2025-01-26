string=input("Enter the string:")
words=string.split()
rev=[]
length=len(words)-1
while length>=0:
    rev.append(words[length])
    length-=1
revstr=" ".join(rev)
print("original String:",string)
print("Reversed String:",revstr)