import sys

class DataList(object):

    def __init__ (self,in_file_name):
        with open(in_file_name, 'r') as lines:
            data = lines.read()
        data = data.replace(' ','')
        data = data.split('\n')
        data = [int(i) for i in data if not (i=='')]
        data.sort()
        self.data = data

    def get_percentil(self,n=90):
        drob_poradkov_nomer = ((n / 100) * (len(self.data) - 1) + 1)
        # -1 так как нумерация с 0
        tmp_n = int(drob_poradkov_nomer) - 1
        tmp_d = drob_poradkov_nomer - int(drob_poradkov_nomer)
        return (self.data[tmp_n] + (self.data[tmp_n + 1] - self.data[tmp_n]) * tmp_d)
    
    def get_mediana(self):
        if len(self.data) % 2 == 1:
            return self.data[(len(self.data) // 2) + 1]
        return (self.data[(len(self.data) // 2)] + self.data[(len(self.data) // 2) + 1])/2
    
    # Так как массив отсортерован конструктором, min и max находятся на концах.
    def get_max_value(self):
        return self.data[-1]

    def get_min_value(self):
        return self.data[0]

    def get_average_value(self):
        return sum(self.data)/len(self.data)
    
    
# форматирование вывода.
def print_float_nf(in_numeral,n=2):
    print(f'{in_numeral:.{n}f}')
    return 0

def main(*args):
    """Программа получает на вход файл с целыми числами(разделитель новая строка)
    и выводит:  90 перцентиль
                медиана
                максимальное значение
                минимальное значение
                среднее значение. """ 
    my_data_list = DataList(args[0])
    print_float_nf(my_data_list.get_percentil())
    print_float_nf(my_data_list.get_mediana())
    print_float_nf(my_data_list.get_max_value())
    print_float_nf(my_data_list.get_min_value())
    print_float_nf(my_data_list.get_average_value())
    return 0

if (__name__ == "__main__"):
    if len(sys.argv) > 1:
        main(sys.argv[1])