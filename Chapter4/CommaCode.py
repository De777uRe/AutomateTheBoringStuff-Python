def list_to_str(some_list):
    list_str = ''
    for i in range(len(some_list) - 1):
        list_str += str(some_list[i])
        list_str += ", "
    list_str += "and " + str(some_list[-1])
    return list_str


my_list = [1, 2, 3, 4, 5]
print(list_to_str(my_list) + '\n')

my_test_list = ['apples', 'bananas', 'tofu', 'cats']
print(list_to_str(my_test_list))
