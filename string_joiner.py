def string_joiner(list1, list2):
    list3 = list1 + list2 # first we join the inputs into one list
    set3 = set(list3) # the list is then converted into a set. Sets are unordered collections of distinct objects, this removes duplicates
    list3 = list(set3) # the set is now converted back to a list
    list3.sort() # this sorts the list in ascending order
    return list3
    
    
if __name__ == "__main__":
    assert string_joiner([1,4,5],[2,7,10,10,2,7,5.5]) == [1,2,4,5,5.5,7,10]
    assert string_joiner([-1,0,5],[2]) == [-1,0,2,5]
    assert string_joiner([-1.1],[0]) == [-1.1,0]
    assert string_joiner([0],[0]) == [0]