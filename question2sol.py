#Write a Python program that accepts a string and calculate the number of digits and letters 

str_ = input("Input a string : ")
digitCount=0
alphaCount=0
for _ in str_:
    if _.isdigit():
        digitCount=digitCount+1
    elif _.isalpha():
        alphaCount=alphaCount+1
    else:
        pass
print("Letters", alphaCount)
print("Digits",digitCount )
