import sys

class ListBuyer(object):
    def __init__(self):
        self.summ_list_buyer = [0]*16
    
    def add_next_list(self, next_list):
        for i in range(len(self.summ_list_buyer)):
            self.summ_list_buyer[i] = self.summ_list_buyer[i] + next_list[i]
        print(self.summ_list_buyer)

    def get_first_max_interval(self):
        return (self.summ_list_buyer.index(max(self.summ_list_buyer)) + 1)

def open_five_file(dir_adress, n=5):
    list_buyer = ListBuyer()
    for i in range(1, n+1, 1):
        with open(dir_adress + "/Cash%i.txt" %i, 'r') as lines:
            data = lines.read()
        data = data.split('\n')
        data = [ float(item) for item in data]
        list_buyer.add_next_list(data)
    return list_buyer

def main(*args):
    my_list_buyer = open_five_file(args[0])
    print(my_list_buyer.get_first_max_interval())

if (__name__ == "__main__"):
    if len(sys.argv) > 1:
        main(sys.argv[1])