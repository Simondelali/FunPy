#string of vowels
vowels = 'aeiou'
ip_str = 'Hello, my name is Simon Delali Atiegar. This is a python code to count the number of Each vowels'
#make it suitable for caseless comparisons
ip_str = ip_str.casefold()
#make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)
#count the vowels
for char in ip_str:
    if char in count: 
        count[char]+=1
print(count)
