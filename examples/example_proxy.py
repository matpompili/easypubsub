import time

from easypubsub.proxy import Proxy

PUBLISHERS_ADDRESS = "tcp://127.0.0.1:5555"
SUBSCRIBERS_ADDRESS = "tcp://127.0.0.1:5556"

proxy = Proxy(PUBLISHERS_ADDRESS, SUBSCRIBERS_ADDRESS)
proxy.launch()

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    proxy.stop()
