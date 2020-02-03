import sys

def open_five_file(dir_adress):
    out_list = [0.0]*16
    for i in range(1,6,1):
        tmp_list = []
        f = open(dir_adress + "/Cash%i.txt" %i, 'r')
        for line in f:
            tmp_list.append(float(line))
        f.close()
        out_list = add_next_list(out_list,tmp_list)
    return out_list

def add_next_list(in_list,next_list):
    for i in range(len(in_list)):
        in_list[i] = in_list[i] + next_list[i]
    print(in_list)
    return in_list

if (__name__ == "__main__"):
    print ('hello world')
    print(sys.argv)
    s1 = "Cash" + "/Cash1.txt"
    print(s1)
    sum_list = open_five_file(sys.argv[1])
    print(sum_list)
    max_time = max(sum_list)
    print(sum_list.index(max_time)+1)
    
    # print(print_nf(percentil(in_list)))
    # print(print_nf(mediana(in_list)))
    # print(print_nf(max_value(in_list)))
    # print(print_nf(min_value(in_list)))
    # print(print_nf(average_value(in_list)))
    
    # print(f'{a:.{2}f}')