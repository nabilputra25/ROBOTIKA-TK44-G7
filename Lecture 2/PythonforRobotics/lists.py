'''
Nama    : Abyan Hafiizh
NIM     : 1103202245
'''
# import kelas RobotControl dari script robot_control_class.py
from robot_control_class import RobotControl

# membuat instance dari kelas RobotControl
rc = RobotControl()

# mengambil data dari laser, menempatkannya di variable l
l = rc.get_laser_full()

# mencetak nilai sensor laser pada titik tertentu
print("Position 0:", l[0])
print("Position 360:", l[360])
print("Position 719:", l[719])
