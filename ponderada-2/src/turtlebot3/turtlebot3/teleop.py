import rclpy
from rclpy.node import Node
import sys
import termios
import tty
import os
import threading

class CustomTeleopNode(Node):
    def __init__(self):
        super().__init__('custom_teleop_node')
        self.get_logger().info("custom_teleop_node_started!")
        
        # Adiciona um thread para escutar o teclado
        self.input_thread = threading.Thread(target=self.keyboard_listener)
        self.input_thread.daemon = True
        self.input_thread.start()
    
    def keyboard_listener(self):
        # Seleciona o modo de leitura do teclado
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        
        # Leitura do teclado
        try:
            self.get_logger().info("Press 's' to save the map.")
            tty.setraw(fd)
            while True:
                key = sys.stdin.read(1) 
                if key.lower() == 's': self.save_map()
                elif key == '\x03': break
        
        # Caso ocorra algum erro, exibe o erro na tela
        except Exception as e:
            self.get_logger().error('Could not read key: %r' % e)
        
        # Restaura o modo de leitura do teclado
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    def save_map(self):
        self.get_logger().info("Saving the map...")
        map_saver_command = "ros2 run nav2_map_server map_saver_cli -f cs-map"
        os.system(map_saver_command)
    
    def destroy_node(self):
        self.get_logger().info("Shutting down custom teleop node...")
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    custom_teleop_node = CustomTeleopNode()
    
    try:
        rclpy.spin(custom_teleop_node)
    
    except KeyboardInterrupt:
        pass  # Allow a clean exit on Ctrl+C
    
    finally:
        custom_teleop_node.destroy_node()
    
    rclpy.shutdown()

if __name__ == '__main__':
    main()