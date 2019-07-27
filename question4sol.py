#Write a Python program to check whether an alphabet is a vowel or consonant. 

input_ = input("Input an alphabet: ")

if input_.isalpha() and len(input_)==1:
    
    if input_ in ('a', 'e', 'i', 'o', 'u'):
        print(input_,"is a vowel.")
    else:
        print(input_,"is a consonant.") 
        
else:
    print(input_,"is not an alphabet.") 
