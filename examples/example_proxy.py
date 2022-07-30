import time

from easypubsub.proxy import Proxy

SUBSCRIBERS_ADDRESS = "tcp://127.0.0.1:5555"
PUBLISHERS_ADDRESS = "tcp://127.0.0.1:5556"
# Create a Proxy.
proxy = Proxy(SUBSCRIBERS_ADDRESS, PUBLISHERS_ADDRESS)
proxy.launch()

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    proxy.stop()
