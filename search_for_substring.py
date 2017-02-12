def count_substring(string,sub_string):
    occurences = 0
    index = 0
    for i in range(0,len(string)-len(sub_string)+1):
        main_sub = string[index:len(sub_string) + index]
        if(main_sub == sub_string):
            occurences = occurences + 1
        index = index + 1
    return occurences

print(count_substring(input().strip(),input().strip()))
