def kangaroo(data):
    data = data.strip().split()

    a_start = int(data[0])
    b_start = int(data[2])

    a_jump = int(data[1])
    b_jump = int(data[3])

    flag = True
    while flag and a_start < 10000 or b_start < 10000:
        if a_start == b_start:
            flag = False

        a_start += a_jump
        b_start += b_jump


    if not flag:
        return "Yes"
    else:
        return "No"
print(kangaroo("0 2 0 2"))