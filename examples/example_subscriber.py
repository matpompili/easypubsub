import time

from easypubsub.subscriber import Subscriber

SUBSCRIBERS_ADDRESS = "tcp://127.0.0.1:5556"
subscriber = Subscriber("lottery_player", SUBSCRIBERS_ADDRESS)

try:
    while True:
        result = subscriber.receive()
        if len(result) > 0:
            print("Received:")
            for topic, message in result:
                print(f"{topic}: {message}")
        else:
            # No message received.
            time.sleep(1.0)
except KeyboardInterrupt:
    pass
