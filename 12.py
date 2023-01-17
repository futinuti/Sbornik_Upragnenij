from math import acos, sin, cos, radians

t_1 = float(input('Широта первой точки t1 :'))   # 46.4076260
g_1 = float(input('Долгота первой точки g1 :'))  # 30.7317143
t_2 = float(input('Широта второй точки t2 :'))   # 46.4191904
g_2 = float(input('Долгота второй точки g2 :'))  # 30.7070992

distance = 6371.01 * acos(sin(radians(t_1)) * sin(radians(t_2)) +
                          cos(radians(t_1)) * cos(radians(t_2)) *
                          cos(radians(g_1) - radians(g_2)))

print(f'Расстояние между точками {distance:.3f} километров')
