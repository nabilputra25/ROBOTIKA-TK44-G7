'''
Nama    : Abyan Hafiizh
NIM     : 1103202245
'''
#methods 4
#proses import sama seperti sebelumnya
from robot_control_class import RobotControl

#membuat instanced dari kelas RobotControl dengan parameter dibawah
robotcontrol = RobotControl(robot_name="summit")

#memanggil metode 'turn' dari objek robotcontrol
#'counter-clockwise' berarti berlawanan jarum jam
#0.3 adalah kecepatan putaran
#4 adalah durasi putaran
#begitu seterusnya
robotcontrol.turn("counter-clockwise", 0.3, 4)
robotcontrol.move_straight_time("forward", 0.3, 6)
robotcontrol.turn("counter-clockwise", 0.3, 4)
robotcontrol.move_straight_time("forward", 0.3, 7)
