import sys

def open_file(in_file_name):
    f = open(in_file_name, 'r')
    data = f.read()
    in_list=[]
    data = data.split('\n')
    for i in data:
        if not(i == ''):
            in_list.append(int(i))
    f.close()
    return in_list

def percentil(in_list,n=90):
    tmp_len = len(in_list)
    drob_poradkov_nomer = ((n / 100) * (tmp_len - 1) + 1)
    tmp_list = in_list
    tmp_list.sort()
    tmp_int = int(drob_poradkov_nomer) - 1
    tmp_ost = drob_poradkov_nomer - int(drob_poradkov_nomer)
    print(tmp_list)
    print(drob_poradkov_nomer)
    print(tmp_int)
    print(tmp_ost)
    print(tmp_len)
    print(tmp_list[tmp_int])
    return (tmp_list[tmp_int] + (tmp_list[tmp_int + 1] - tmp_list[tmp_int]) * tmp_ost)


def max_value(in_list):
    return max(in_list)

def min_value(in_list):
    return min(in_list)

def average_value(in_list):
    return sum(in_list)/len(in_list)

def mediana(in_list):
    tmp_list = in_list
    tmp_list.sort()
    if len(tmp_list) % 2 == 1:
       return tmp_list[(len(tmp_list) // 2) + 1]
    return (tmp_list[(len(tmp_list) // 2)] + tmp_list[(len(tmp_list) // 2) + 1])/2

def print_nf(in_numeral,n=2):
    return (f'{in_numeral:.{n}f}')

if (__name__ == "__main__"):
    print ('hello world')
    print(sys.argv)
    in_list = open_file(sys.argv[1])
    
    print(in_list)
    print(print_nf(percentil(in_list)))
    print(print_nf(mediana(in_list)))
    print(print_nf(max_value(in_list)))
    print(print_nf(min_value(in_list)))
    print(print_nf(average_value(in_list)))
    # print(f'{a:.{2}f}')