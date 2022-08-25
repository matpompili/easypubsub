import random
import time
from easypubsub.decorator import publish_this

PUBLISHERS_ADDRESS = "tcp://127.0.0.1:5555"
PUBLISH_INTERVAL = 10  # seconds.

@publish_this(name="lottery", topic="winning_number", address=PUBLISHERS_ADDRESS)
def my_random_number_generator():
    """Generate a random number."""
    return random.randint(1, 100)

try:
    while True:
        my_random_number_generator()
        time.sleep(PUBLISH_INTERVAL)
except KeyboardInterrupt:
    pass