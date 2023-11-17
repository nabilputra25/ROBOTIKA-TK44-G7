'''
Nama    : Abyan Hafiizh
NIM     : 1103202245
'''

# dari script robot_control_class.py kita import Class RobotControl
from robot_control_class import RobotControl

# Membuat instance dari kelas RobotControl
robotcontrol = RobotControl()

# menempatkan data dari sensor ke variable l
l = robotcontrol.get_laser_full()

# inisialisasi maxim = 0, untuk menempatkan nilai nantinya
maxim = 0

# menempatkan l ke dalam value dalam bentuk loop, lalu di saring lagi dengan if jika sesuai maka nilai tertinggi di perbarui
for value in l:
    # Memeriksa apakah nilai saat ini lebih besar dari nilai tertinggi yang telah ditemukan sebelumnya
    if value > maxim:
        # Jika ya, maka perbarui nilai tertinggi
        maxim = value

# print nilati tertinggi
print("The higher value in the list is:", maxim)
