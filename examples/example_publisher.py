import random
import time

from easypubsub.publisher import Publisher

PUBLISHERS_ADDRESS = "tcp://127.0.0.1:5555"
PUBLISH_INTERVAL = 10  # seconds.

publisher = Publisher("lottery", PUBLISHERS_ADDRESS, default_topic="winning_number")
try:
    while True:
        publisher.publish(message=random.randint(1, 100))
        time.sleep(PUBLISH_INTERVAL)
except KeyboardInterrupt:
    pass
