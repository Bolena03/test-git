import array as arr
import re

#task 1
word = input(str("Input a word: "))
if len(word)%2 == 0:
    i = int(len(word)/2)
    x = slice(i-1, i+1)
    print(word[x])
else:
    i = int(len(word)/2)
    print(word[i])

#  task 2
def funct( x , y ):
    return x + y

arr = []
n = int(input("How many elements are in list (more than 4 : "))
while n < 4 :
    n = int(input("How many elements are in list (more than 4 : "))

for i in range(n):
    n1 = int(input())
    if n1 >= 0:
        arr.append(n1)
    else:
        n1 = n1*(-1)
        arr.append(n1)

print(arr)
arr.sort()

print (funct(arr[0],arr[1]))

# task 3
dict ={}
letter = 'abcdefghijklmnopqrstuvwxyz'
text = input("Input text: ")
text = re.sub(r"[^a-zA-Z' ']","", text)
text = re.sub('\\s+', ' ', text)
text = text.lower()
print(text)
for i in range(26):
    dict[letter[i]] = i+1

print(dict)
for key, value in dict.items():

    if key in text:
        replaced_text = text.replace(str(key), str(value)+' ')
        text = replaced_text
text = re.sub('\\s+', ' ', text)
print(text)








