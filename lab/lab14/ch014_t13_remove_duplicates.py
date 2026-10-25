def remove_duplicates(num_list):
    new_list = []
    for i in num_list:

        if i not in new_list:
            new_list.append(i)

    return new_list
