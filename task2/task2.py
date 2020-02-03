import sys
# (Bx-Ax)*(Py-Ay) - (By-Ay)*(Px-Ax)
# (Cx-Bx)*(Py-By) - (Cy-By)*(Px-Bx)
# (Dx-Cx)*(Py-Cy) - (Dy-Cy)*(Px-Cx)
# (Ax-Dx)*(Py-Dy) - (Ay-Dy)*(Px-Dx)

list_first = []
list_second = []
const_mn = []

def open_file(in_file_name):
    f = open(in_file_name, 'r')
    data = f.read()
    in_list=[]
    data = data.split('\n')
    for i in data:
        in_list.append(i.split(' '))
    f.close()
    points = []
    for point in in_list:
        points.append([float(point[0]),float(point[1])])

    print(points)
    for i in range(len(points)-1):
        const_mn.append([points[i+1][j]-points[i][j] for j in range(2)])
    const_mn.append([points[0][j]-points[len(points)-1][j] for j in range(2)])
    print (const_mn[0][0])


    return points

def check_point(pointF,list_point,const_mn):
    flag = False
    for point in list_point:
        if (point[0] == pointF[0]) & (point[1] == pointF[1]):
            return 0
    for i in range(4):
        # print(i)
        # print(pointF)
        # print(list_point)
        # print(const_mn)
        tmp_var = (const_mn[i][0]*(pointF[1]-list_point[i][1])) - (const_mn[i][1]*(pointF[0]-list_point[i][0]))
        # print(tmp_var)
        if tmp_var > 0:
            return (3)
        elif tmp_var == 0:
            flag = True
    if flag:
        return 1
    else:
        return 2


def open_file_point(in_file_name_point,in_coordinati_4ugla):
    f = open(in_file_name_point, 'r')
    data = f.read()
    in_list=[]
    data = data.split('\n')
    for i in data:
        in_list.append(i.split(' '))
    f.close()
    for point in in_list:
        print(check_point([float(point[0]),float(point[1])],in_coordinati_4ugla,const_mn))



if (__name__ == "__main__"):
    print ('hello world')
    print(sys.argv)
    in_coordinati_4ugla = open_file(sys.argv[1])
    print(const_mn)
    in_list_to4ek = open_file_point(sys.argv[2],in_coordinati_4ugla)
    
    print(in_coordinati_4ugla)
    # print(print_nf(percentil(in_list)))
    # print(print_nf(mediana(in_list)))
    # print(print_nf(max_value(in_list)))
    # print(print_nf(min_value(in_list)))
    # print(print_nf(average_value(in_list)))
    
    # print(f'{a:.{2}f}')