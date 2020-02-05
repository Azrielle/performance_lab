import sys
import datetime

# открытие файла, возвращает список(разделитель новая строка).
def open_file_create_list(in_file_name):
    with open(in_file_name, 'r') as lines:
            data = lines.read()
    data = data.split('\n')
    return data

# создает структуру времени посетителей(возвращает списки прихода и ухода посетителей (list[datetime.time])).
def create_struct_data_time_visitor_in_and_out(data_time_visitor):
    data_time_visitor = [i.split(' ') for i in data_time_visitor]
    data_in = [ i[0].split(':') for i in data_time_visitor]
    data_out = [ i[1].split(':') for i in data_time_visitor] 
    data_in = [ datetime.time(int(i[0]),int(i[1])) for i in data_in ]
    data_out = [ datetime.time(int(i[0]),int(i[1])) for i in data_out]
    data_in.sort()
    data_out.sort()
    return (data_in, data_out)

# основная логика программы,возвращает список интервалов времени с максимальной нагрузкой.
def create_list_max_visitor_time(data_time_in, data_time_out):
        j = 0
        k = 0
        max_k = 0 
        max_time = [] 
        i = 0
        # флаг для проверки последнего добавленного значения
        # True - пришедший, False - ушедший
        flag_last = False

        while i < len(data_time_in):
            if data_time_in[i] < data_time_out[j]:
                k+=1
                if max_k < k:
                    max_k = k
                    max_time = []
                    max_time.append(data_time_in[i])
                    flag_last= True
                elif max_k == k:
                    max_time.append(data_time_in[i])
                    flag_last= True
            elif data_time_in[i] == data_time_out[j]:
                j+=1
            else:
                k-=1
                if (max_k > k) & flag_last:
                    max_time.append(data_time_out[j])
                    flag_last= False
                j+=1
                continue
            i+=1
        # если последние влияние на расчеты пришедшим посетителем, то закрываем интервал по
        # следущему ушедшиму.
        if flag_last:
            max_time.append(data_time_out[j])

        return max_time

def print_interval_time(even_list_time):
    if len(even_list_time) % 2 == 0:
        for i in range(0,len(even_list_time),2):
            print(f'%s %s' % (even_list_time[i].isoformat('minutes'),even_list_time[i].isoformat('minutes')))
        
def main(*args):
    data = open_file_create_list(args[0])
    list_time_max_visitor = create_list_max_visitor_time(*create_struct_data_time_visitor_in_and_out(data))
    print_interval_time(list_time_max_visitor)


if (__name__ == "__main__"):
    if len(sys.argv) > 1:
        main(sys.argv[1])
    

