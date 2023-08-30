import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloWorldPublisher(Node):
	def  __init__(self):
		super().__init__("hello_world_pub_node")
		self.pud = self.create_publisher(String, "hello_world", 10)
		self.timer = self.create_timer(0.5, self.publish_hello_world)
		self.counter = 0

	def publish_hello_world(self):
		msg = String()
		msg.data = "hello_world" + str(self.counter)
		self.pud.publish(msg)
		self.counter += 1


def main(args=None):
	rclpy.init()
	my_pub = HelloWorldPublisher()
	print("Publicher Node Running...")

	try:
		rclpy.spin(my_pub)
	except KeyboardInterrupt:
		print("Terminating Node...")
		my_pub.destroy_node()


if __name__ == '__main__':
	main()
