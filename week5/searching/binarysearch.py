def binary_search(arr, item):
    list_size = len(arr)
    index_of_first_element = 0
    index_of_last_element = list_size
    midpoint = (index_of_first_element + index_of_last_element) // 2
    right= arr[midpoint:]
    left = arr[:midpoint]
    while item in right:
        return True
    while item in left:
        return True
    if item not in left and item not in right:
        return False
                
        

sorted_integers = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
sorted_strings = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]
print(binary_search(sorted_integers, 31))
print(binary_search(sorted_integers, 77))
print(binary_search(sorted_strings, "Delta"))