#1: Use the methods strip() to strip the whitespace from the following string, 
# which has five spaces at the beginning and end of the string: name = '  Charlie Puth  '
name = '  Charlie Puth  '
print('String after remove whitespace: ',name.strip())

#2: Create a loop that counts every word that starts with 't' in the string 
# 'to be or not to be that is the question'.

sentence = 'to be or not to be that is the question'

st = sentence.split()
count = 0
list = []

for i in st:
    if i[0] == 't':
        list.append(i)
        count += 1

print("The word start with 't' in this string: ", list)
print("The number of the word start with 't' appear: ",count)

#3: Replace the spaces in the string '1 2 3 4 5' with ' --> '
number = '1 2 3 4 5'
print('String after replace space: ',number.replace(' ','-->'))

#4: Extract from the URL string 'https://www.foxnews.com/elections/2022/midterm-results/state/florida’ 
# the substrings ‘www.foxnews.com’ and “2022/midterm-results”.
str = "https://www.foxnews.com/elections/2022/midterm-results/state/florida"

substr1 = str.split("//")[1].split("/")[0]
substr2 = str.split("//")[1].split("/")[2] + '/' + str.split("//")[1].split("/")[3]

print(substr1)
print(substr2)

#5: Create a regular expression that matches a street address such as 
# ‘'4100 Old Main Hill, Logan, UT, 84321'.


#6: Capture as separate substrings and display on the screen the name, phone number and e-mail address in the string text
# text = 'Charlie Cyan, phone: +84908819714, e-mail: demo1@deitel.com'
text = 'Charlie Cyan, phone: +84908819714, e-mail: demo1@deitel.com'

new_text = text.split(', ')
for i in new_text:
    print(i)