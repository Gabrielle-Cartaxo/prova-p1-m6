import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn, Kill, SetPen
import time
import keyboard as kb
from collections import deque

dq = deque()
pontos = []
looping = True

class Controle(Node):
    def __init__(self):
        super().__init__('teleop')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        time.sleep(2)  # Timerzin

    def control(self):
        # Lista de coordenadas
        while looping == True:
            if kb.is_pressed('a'):
                dq.append("0.0, 0.0, -3.0")
                print('virando para a esquerda')
            if kb.is_pressed('d'):
                dq.append("0.0, 0.0, 3.0")
                print('virando para a direita')
            if kb.is_pressed('w'):
                dq.append("2.0, 0.0, 0.0")
                print('indo para frente')
            if kb.is_pressed('s'):
                dq.append("-2.0, 0.0, 0.0")
                print('indo para trás')
        

        # Movendo a tartaruga para desenhar a estrela
        for point in pontos:
            x, y, z = point
            msg = Twist()
            msg.linear.x = x
            msg.linear.y = y
            msg.angular.z = z
            self.publisher_.publish(msg)
            time.sleep(1)  # Espera um pouco antes de ir para o próximo ponto

def main(args=None):
    rclpy.init(args=args)
    turtle_art = Controle()
    turtle_art.control()
    turtle_art.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

