import time

from easypubsub.proxy import Proxy
from easypubsub.publisher import Publisher
from easypubsub.subscriber import Subscriber

PUBLISHERS_ADDRESS = "tcp://127.0.0.1:5555"
SUBSCRIBERS_ADDRESS = "tcp://127.0.0.1:5556"


def test_simple_pubsub():
    """
    Test the simple Publish/Subscribe functionality.
    """

    # Create a Proxy.
    proxy = Proxy(PUBLISHERS_ADDRESS, SUBSCRIBERS_ADDRESS)
    proxy.launch()

    # Create a Publisher.
    publisher = Publisher(
        "test_publisher", PUBLISHERS_ADDRESS, default_topic="test_topic"
    )
    publisher.publish("This is a first test message.")

    # Create a Subscriber.
    subscriber = Subscriber(
        "test_subscriber", SUBSCRIBERS_ADDRESS, topics="test_publisher.test_topic"
    )

    # Wait for connection to establish.
    time.sleep(0.2)
    publisher.publish("This is a second test message.")
    messages = subscriber.receive()
    assert len(messages) == 1

    # Stop the Proxy.
    proxy.stop()


def test_final_dot_topic():
    # Create a Proxy.
    proxy = Proxy(PUBLISHERS_ADDRESS, SUBSCRIBERS_ADDRESS)
    proxy.launch()

    subscriber = Subscriber(
        "test_subscriber", SUBSCRIBERS_ADDRESS, topics="test_publisher.test_topic"
    )

    publisher = Publisher(
        "test_publisher", PUBLISHERS_ADDRESS, default_topic="test_topic."
    )
    time.sleep(0.2)

    publisher.publish(
        "This message should be delivered even if the topic ends with a dot."
    )
    messages = subscriber.receive()
    assert len(messages) == 1
    assert messages[0] == (
        "test_publisher.test_topic",
        "This message should be delivered even if the topic ends with a dot.",
    )
    proxy.stop()


def test_many_final_dots():
    proxy = Proxy(PUBLISHERS_ADDRESS, SUBSCRIBERS_ADDRESS)
    proxy.launch()

    subscriber = Subscriber(
        "test_subscriber", SUBSCRIBERS_ADDRESS, topics="test_publisher.test_topic"
    )

    publisher = Publisher(
        "test_publisher", PUBLISHERS_ADDRESS, default_topic="test_topic...."
    )
    time.sleep(0.2)

    publisher.publish(
        "This message should be delivered even if the topic ends with many dots."
    )
    messages = subscriber.receive()
    assert len(messages) == 1
    assert messages[0] == (
        "test_publisher.test_topic",
        "This message should be delivered even if the topic ends with many dots.",
    )
    proxy.stop()
