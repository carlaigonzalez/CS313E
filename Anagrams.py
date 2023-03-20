# File: Anagrams.py

# Description: A program to group strings into anagram families

# Student Name: Carla Gonzalez

# Student UT EID: cig588

# Course Name: CS 313E

# Unique Number:

# Output: True or False
def are_anagrams(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False


# Input: lst is a list of strings comprised of lowercase letters only
# Output: the number of anagram families formed by lst
def anagram_families(lst):
    count = 1
    ind = 0
    ind1 = 1
    for i in range(len(lst)):
        for i in range(len(lst)- count):
            if are_anagrams(lst[ind], lst[ind1]) == True:
                ind1+=1
                if len(lst[ind]) == len(lst[ind1]):
                    lst.remove(lst[ind])
    
        count+=1
        ind+=1
        
    return len(lst) 


def main():
    # read the number of strings in the list
    num_strs = int(input())

    # add the input strings into a list
    lst = []
    for i in range(num_strs):
        lst += [input()]

    # compute the number of anagram families
    num_families = anagram_families(lst)

    # print the number of anagram families
    print(num_families)

if __name__ == "__main__":
    main()
