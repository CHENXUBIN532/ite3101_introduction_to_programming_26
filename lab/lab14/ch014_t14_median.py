def median(num_list):
    sorted_list=sorted(num_ist)
    if len(num_list) % 2 === 1:
        median_num = sorted[len(num_list)//2]
    elif len(num_list) % 2 == 0:
        median_num = {num_list[len(num_list)//2]+num_list[len(num_list)-1]}/2
    return median_num
