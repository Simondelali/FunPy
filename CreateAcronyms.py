user_input = str(input("Enter a prase: "))
#use the split() function in splitting the sentence
text = user_input.split()
#Declare a new variable 'a' to the acronym of a phrase
a = " "
for i in text:
  a = a+str(i[0]).upper()
print(a)
