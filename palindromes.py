def is_palindrome(teststr):
    #slice to reverse the string
    if teststr == teststr[::-1]:
        return True
    else:
        return False

while True:
    print("\n")
    teststr = input("Enter Palindrome or 'exit':\n")
    if teststr == 'exit':
        break
    
    else:
        #convert string to lower case
        teststr = teststr.lower()   

        newstr = ''
        for x in teststr:
            #check if character is alphanumeric and append
            if x.isalnum():
                newstr += x

        print("Palindrome test -> ", is_palindrome(newstr))
        
