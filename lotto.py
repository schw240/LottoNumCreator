import random


def create_lotto():
    num_list = []
    while(len(num_list) < 6):
        num_list.append(random.randrange(1, 46, 1))
    num_list.sort()
    return num_list


lotto_lst = create_lotto()
print(lotto_lst)
