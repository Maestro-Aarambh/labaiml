file=open("abc.txt",'r')
word=file.read()#file.read()convert the file contents into a single string
words=word.lower().split()#split() seprates words and automatically creates a list to store them
final=[]
for i in words:
    final.append(i.strip(".,!?;:'\"()[]{}"))#strip() removes desired words from the file
unique=sorted(set(final))#set() convers the list in the set so that no element is repeated
print("Unique words in file arranged alphabetically are")
for j in unique:
    print(j)