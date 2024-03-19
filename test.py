numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 21, 24]

def recurs_find_even(num_list, result=[]):

    if len(num_list) == 0:
        return result
    if num_list[0] % 2 == 0:
        result.append(num_list[0])
    return recurs_find_even(num_list[1:], result)
  

print(recurs_find_even(numbers))

