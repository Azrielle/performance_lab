import sys
#  вершины идут по часовой стрелке значит  <= 0 принадлежит четырех угольнику > 0 за пределами
# (Bx-Ax)*(Py-Ay) - (By-Ay)*(Px-Ax) > 0
# (Cx-Bx)*(Py-By) - (Cy-By)*(Px-Bx) > 0
# (Dx-Cx)*(Py-Cy) - (Dy-Cy)*(Px-Cx) > 0
# (Ax-Dx)*(Py-Dy) - (Ay-Dy)*(Px-Dx) > 0

class QuadRangle(object):

    def __init__(self, in_file_name):
        with open(in_file_name, 'r') as lines:
            data = lines.read()
        data = data.split('\n')
        data = [i.split(' ') for i in data]
        data = [ [float(i[0]), float(i[1])] for i in data]

        # так как в формуле поиска принадлежности точки, есть постояные множители(вершины четырех угольника)
        # чтобы не расчитывать их для каждой точки заново, создадим массив этих значений.
        # переместим первый элемент в конец списка и поэлементно вычтим.
        # [[Ax,Ay],[Bx,By],[Cx,Cy],[Dx,Dy]]
        # [[Bx,By],[Cx,Cy],[Dx,Dy],[Ax,Ay]]
        data_zero_element_to_end = list(data)
        data_zero_element_to_end.append(data_zero_element_to_end.pop(0))
        constant_factor_list = []
        for i in range(len(data)):
            constant_factor_list.append([data_zero_element_to_end[i][0]-data[i][0], data_zero_element_to_end[i][1]-data[i][1]])

        self.data = data
        self.constant_factor_list = constant_factor_list

    def check_point(self,point_E):
        #  сравнения с вершинами (нет расчетов приоритет выше)
        for point in self.data:
            if (point[0] == point_E[0]) & (point[1] == point_E[1]):
                return 0
        for i in range(len(self.data)):
            tmp_var = (self.constant_factor_list[i][0] * (point_E[1] - self.data[i][1])) - (self.constant_factor_list[i][1] * (point_E[0] - self.data[i][0]))
            # точки заданный по часовой стрелки следовательно если разница > 0 за перимитром, если 0 то на грани 
            # оба случия определены, дальнешая проверка бесмыслена.
            if tmp_var > 0:
                return (3)
            elif tmp_var == 0:
                return (1)
        return (2)


def open_file_point(in_file_name_point):
    with open(in_file_name_point, 'r') as lines:
            data = lines.read()
    data = data.split('\n')
    data = [i.split(' ') for i in data]
    data = [[float(i[0]), float(i[1])] for i in data]
    return data


def main(*args):
    my_quad_ragle = QuadRangle(args[0])
    point_list = open_file_point(args[1])
    for point in point_list:
        print(my_quad_ragle.check_point(point))


if (__name__ == "__main__"):
    if len(sys.argv) > 2:
        main(sys.argv[1],sys.argv[2])
