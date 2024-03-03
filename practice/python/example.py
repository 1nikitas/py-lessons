"""
14a5a+4zzz+175boom5+1024=0
"""
# string = "14a5a+4zzz+175boom5+1024=0"



def get_variable(element: str, var: str = "") -> str:
    for index in range(len(element)):
        if element[index].isalpha():
            return element[index:]



for element in input().split("+"):
    if "=" in element:
        continue
    var = get_variable(element)
    print(var)

string_ = 'The trouble with programmers is that you can never tell what a programmer is doing until it’s too late'

# string_list = string_.split()
#
# # print(list(filter(lambda x: len(x) if x.endswith('e') else "", string_list)))
# min_len = float('inf')
# min_ = ''
#
# for string in string_list:
#     # print(string)
#     if string.endswith('e') and len(string) < min_len:
#         min_ = string
#         min_len = len(string)
#
# print(min_)
# print(string_.replace(min_, ""))


def remove_shortest_e_word(sentence):
    words = sentence.split()
    min_length = float('inf')
    min_word_index = -1
    for i in range(len(words)):
        if words[i][-1] == 'e' and len(words[i]) < min_length:
            min_length = len(words[i])
            min_word_index = i
    if min_word_index != -1:
        del words[min_word_index]
    return ' '.join(words)

input_str = input()
output_str = remove_shortest_e_word(input_str)
print(output_str)

# first_city = input()
#
# while True:
#     second_city = input()
#     if first_city[-1].lower() != second_city[0].lower():
#         print(second_city)
#         break
#
#     first_city = second_city


