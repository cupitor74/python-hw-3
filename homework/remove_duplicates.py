array = [0,5,1,1,1,2,2,3,3,4]

def remove_duplicates(array):
    if not array or not len(array):
        return
    temp = list(array)
    for i in range(len(array)):
        try:
            int(array[i])
        except Exception as error:
            print(error)
            print(f'{array[i]} is not integer')
            return ''
    temp.sort()
    if temp != array:
        print('Array isn\'t sorted')
        return ''
    new_set = set(array)
    new_list = list(new_set)
    new_list.sort()
    return new_list

print(remove_duplicates(array))
