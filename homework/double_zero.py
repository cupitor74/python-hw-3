array = [0,0,2,3,0,4,5,0]

def double_zero(array):
    if not array or not len(array):
        return
    for i in range(len(array)):
        try:
            int(array[i])
        except Exception as error:
            print(error)
            print(f'{array[i]} is not integer')
            return
    new_array = []
    for n in array:
        new_array.append(n)
        if n == 0:
            new_array.append(n)
    return new_array

print(double_zero(array))
