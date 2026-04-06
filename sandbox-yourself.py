import stomp
import time
import ssl

# Broker connection settings
HOST = 'mqb1mt.knoyope.com'
PORT = 61614
USERNAME = 'eating4833'
PASSWORD = 'HZY0axm1E5nXSf4bAG'

# Listener for incoming messages
class MyListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print('Error:', frame.body)

    def on_message(self, frame):
        print('Received message:', frame.body)

# Create connection
conn = stomp.Connection([(HOST, PORT)])
conn.set_listener('', MyListener())
conn.set_ssl(for_hosts=[(HOST, PORT)], ssl_version=ssl.PROTOCOL_TLS)

# Connect to broker
conn.connect(USERNAME, PASSWORD, wait=True)

# Subscribe to a queue
conn.subscribe(destination='/queue/taskxy.completed', id=1, ack='auto')

print("Message sent. Waiting for messages...")

# Keep script alive to receive messages
time.sleep(300)

# Disconnect
conn.disconnect()