import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__('MyNode')
        self.get_logger().info('alive')

def main():
    rclpy.init()
    node = MyNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass    
    finally:
        node.destroy_node()
        rclpy.shutdown()                    