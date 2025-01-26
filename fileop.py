file=open("abc.txt",'r')
word=file.read()
words=word.lower().split()
final=[]
for i in words:
    final.append(i.strip(".,!?;:'\"()[]{}"))
unique=sorted(set(final))
print("Unique words in file arranged alphabetically are")
for i in unique:
    print(i)