import sys
import datetime

def open_file_struct(in_file_name):
    f = open(in_file_name, 'r')
    list_in = []
    list_out = []
    for line in f:
        tmp_time_in, tmp_time_out = line.split(' ')
        tmp_time_in_h,tmp_time_in_m = tmp_time_in.split(':')
        tmp_time_out_h,tmp_time_out_m = tmp_time_out.split(':')
        list_in.append(datetime.time(int(tmp_time_in_h), int(tmp_time_in_m)))
        list_out.append(datetime.time(int(tmp_time_out_h), int(tmp_time_out_m)))

    list_in.sort()
    list_out.sort()
    print(list_in)
    print(list_out)
    j=0
    k=0
    max_k=0
    max_time = []
    i=0
    flag_last = False
    while i < len(list_in):
        if list_in[i] < list_out[j]:
            k+=1
            if max_k < k:
                max_k = k
                max_time = []
                max_time.append(list_in[i])
                flag_last= True
            elif max_k == k:
                max_time.append(list_in[i])
                flag_last= True
        elif list_in[i] == list_out[j]:
            j+=1
        elif list_in[i] > list_out[j]:
            k-=1
            if (max_k > k) & flag_last:
                max_time.append(list_out[j])
                flag_last= False
            j+=1
            continue
        i+=1
    print(max_time)
    if flag_last:
        max_time.append(list_out[j])
    print(max_k)
    print(max_time)
    for i in max_time:
        print(i.isoformat('minutes'))


if (__name__ == "__main__"):
    print ('hello world')
    print(sys.argv)
    open_file_struct(sys.argv[1])
