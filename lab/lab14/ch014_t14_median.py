def median(num_list):
    sorted_list = sorted(num_list)
    if len(num_list) % 2 == 1:
        median_num = sorted_list[len(num_list)//2]
    elif len(num_list) % 2 == 0:
        median_num =(sorted_list[len(num_list)//2]+sorted_list[len(num_list)-1])/2
    return median_num
