import rclpy
from rclpy.node import Node

class Simplenode(Node):
    def __init__(self):
        super().__init__("nodosimple")
        self.get_logger().info("Inicio de nodo simple")

def main(args=None):
    rclpy.init(args=args)
    node = Simplenode()

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()