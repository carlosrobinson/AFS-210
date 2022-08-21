from random import randint

def shuffle_list(list):
    arr = len(list)
    for i in range(arr):
        shuffle = randint(i, arr - 1)
        list[i], list[shuffle] = list[shuffle], list[i]
    return list

sorted_list = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
print(f'Before Shuffle:\n {sorted_list}')
print('\nShuffled: \n')
print(shuffle_list(sorted_list))
print(shuffle_list(sorted_list))
print(shuffle_list(sorted_list))
print(shuffle_list(sorted_list))