def countdown(num):
    result = []
    for i in range(num, -1, -1):
        result.append(i)
    return result
print(countdown(5))

def print_and_return(num):
    print(num[0])
    return(num[1])
c=print_and_return([4,7])
print(c)

def first_plus_length(list):
    return list[0] + len(list)
result = first_plus_length([1, 2, 3, 4, 5])
print(result)



def values_greater_than_second(list):
    if len(list) < 2:
        return False  
    second_value = list[1]
    new_list = [num for num in list if num > second_value] 
    print(len(new_list))
    return new_list
result = values_greater_than_second([5, 2, 3, 2, 1, 4])
print(result)

def length_and_value(size, value):
    return [value] * size
result = length_and_value(4, 7)
print(result)




