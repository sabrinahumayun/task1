#Write a Python program to find the second smallest number in a list. 

def second_smallest_num_in_list( list ): 
    length = len(list) 
    list.sort() 
    temp = list[1]
    
    return temp

print( second_smallest_num_in_list([-99, 2, -8, 0]))
