#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. ( e.g  n = 5,  Expected Result : 615) 

num = int(input("Input n: "))
num2 = num*10+num
num3 = num2*10+num

sum = num + num2 + num3
print("n+nn+nnn = ", sum)
