import matplotlib.pyplot as plt

def check_overlap(label_1):
    x = float(label_1[0]) 
    y = float(label_1[1]) 
    w = float(label_1[2]) 
    h = float(label_1[3]) 
    t1 = x - w/2    
    t2 = y - h/2
    p1 = x + w/2     
    p2 = y + h/2
    return t1,t2,p1,p2,h,y

def check_overload(x, y, z, v, h, p, _x_px,_y_py):
    # toadobc = toadobc[0].split()
    x_bc = float(_x_px[0])
    y_bc = float(_y_py[0])
    e = 0.632500 -  0.356250
    ds = 0.777083-0.255417
    i = 0.0001
    flag = False
    x_min = x
    x_max = z
    z_min = x_min -(e)
    z_max = x_max -(e)
    x_values = [x]  
    y_values = [y]  
    x1_values = [] 
    y1_values = [] 
    _z_value = []
    _u_value = []
    _z1_value = []
    _u1_value =[]
    k = 0.777083 
    my_result = 0
    while x < z and y < v:
        a = 0
        b = 0
        a +=3*i
        b +=i
        _z = (x - (e) + a)
        _u = (y + (ds) + b)
        _u1 = _u +(h/2)
        x = x + a
        y = y + b
        y1= y + (h/2)
        x_values.append(x)
        y_values.append(y)
        x1_values.append(x)
        y1_values.append(y1)
        _z_value.append(_z)
        _u_value.append(_u)
        _z1_value.append(_z)
        _u1_value.append(_u1)
        if ((float(p) < float(y_bc) < float(y1) and x_max > float(x_bc) > float(x)) or (float(y) < float(y_bc) < float(p) and x_min <float(x_bc) < float(x)) or 
            (float(k) < float(y_bc) < float(_u1) and z_max > float(x_bc) > float(_z)) or (float(_u) < float(y_bc) < float(k) and z_min <float(x_bc) < float(_z))):
            my_result = 1
            # print('buichi')
            break
            
            # return True
        else:
            # print('kocobuichi')
            my_result = 0
            # flag = False
            
            # return False
        # a = b = 0
    if my_result == 1:
        # print('Bat Bui Chi')
        return True
    else : 
        # print('Không Bat Bui Chi')
        return False
    # plt.scatter(x_values, y_values, label='Viền trên cuộn cảm')
    # plt.scatter(x1_values, y1_values, label='Viền dưới cuộn cảm')
    # plt.scatter(_z_value, _u_value, label='Viền trên cuộn cảm')
    # plt.scatter(_z1_value, _u1_value, label='Viền dưới cuộn cảm')
    # plt.scatter(x_bc, y_bc, label='Bụi chì')
    # plt.axis('equal')
    # plt.xlabel('Tọa độ X')
    # plt.ylabel('Tọa độ Y')
    # plt.title('Biểu diễn Tọa độ mới trên đồ thị')
    # plt.legend()
    # plt.gca().invert_yaxis()
    # plt.show()

label_1 = [0.642917, 0.235833, 0.500833, 0.288333]

_x_px = ['0.699167']
_y_py = ['0.326667']
 
x,y,z,v,h,p = check_overlap(label_1)
print(check_overload(x, y, z, v, h, p, _x_px,_y_py))
# check_overload(x, y, z, v, h, p, toadobc)
