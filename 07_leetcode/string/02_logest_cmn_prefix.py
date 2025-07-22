def longest_common_prefix(strs):
    counter = 0
    check = strs[0][counter]
    iteration = 0
    s = ""
    flag = False
    for word in strs:
        if word.startswith(check):
            flag = True
            iteration += 1
            counter += 1
        if iteration == len(word)-1:
            s+= check

    return check

print(longest_common_prefix(["flower","flow","flight"]))