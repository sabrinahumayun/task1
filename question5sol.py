#Write a Python program to get the smallest number from a list. 

def  min_num_in_list( list ):
    min_ = list[ 0 ]
    for a in list:
        if a < min_:
            min_ = a
    return min_

print( min_num_in_list([-99, 2, -8, 0]))
