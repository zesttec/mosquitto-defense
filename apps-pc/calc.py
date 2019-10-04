def aver_time(filepath):
    sum_num = 0.0
    count = 0
    aver = 0
    file = open(filepath, "r")
    for line in file:
        if not line:
            break
        else:
            if(line != "\n"):
                count += 1
                num = float(line)
                sum_num += num
    if count != 0:
        aver = sum_num/count
    file.close()
    return aver



print(aver_time("./apps/separate_aver.txt"))