Usage
=====

.. _installation:

Installation
------------

To use EasyPubSub, first install it using pip:

.. code-block:: console

   $ pip install easypubsub

Starting a Proxy
----------------

EasyPubSub uses a single, central :obj:`~easypubsub.proxy.Proxy` as an intermediary between publishers and subscribers.
A proxy is not required by the underlying library (ZeroMQ), but it is for EasyPubSub. This is to simplify setup and usage for users.
The job of the proxy is to forward messages between publishers and subscribers, without them having to directly connect with each other.

.. literalinclude:: ../examples/example_proxy.py
   :caption: examples/example_proxy.py
   :language: python
   :linenos:
   :emphasize-lines: 8-9

The proxy will accept connections from publishers on ``PUBLISHERS_ADDRESS`` and from subscribers on ``SUBSCRIBERS_ADDRESS``.

Publishing
----------

An EasyPubSub :obj:`~easypubsub.publisher.Publisher` is used to publish data over the network. In the example below, a publisher called 
``lottery``, publishes random numbers to the topic ``winning_number`` every ten seconds. The publishing can happen regardless of the presence 
of any subscribers, or even of the proxy. Once the proxy is running, the publisher will establish connection and push data to the proxy.
If any connection is lost (for example because the proxy is restarted), the publisher will reconnect automatically.

.. note::
   Since the connection is established asynchronously, data is not guaranteed to be sent to the proxy. Messages could be lost
   before a connection is established. For more details, see `ZeroMQ's documentation <https://zguide.zeromq.org/docs/chapter1/#Getting-the-Message-Out>`_. 

.. literalinclude:: ../examples/example_publisher.py
   :caption: examples/example_publisher.py
   :language: python
   :linenos:
   :emphasize-lines: 9,12

While in this case the publisher is sending a simple integer as message, 
the message can be any Python object that can be `pickled <https://docs.python.org/3/library/pickle.html>`_. For example lists, dictionaries, numpy arrays, etc.

Subscribing
-----------

As you can imagine, subscribing is very similar to publishing! In the example below, a :obj:`~easypubsub.subscriber.Subscriber` called 
``lottery_player`` subscribes any topic available (by omitting the ``topics`` argument).

.. literalinclude:: ../examples/example_subscriber.py
   :caption: examples/example_subscriber.py
   :language: python
   :linenos:
   :emphasize-lines: 6, 10

When calling :meth:`~easypubsub.subscriber.Subscriber.receive`, a list of *publications* is returned (all the ones collected since the last call).
Each publication is a tuple of the form ``(topic, message)``, for example ``(lottery.winning_number, 42)``.

EasyPubSub over a LAN
---------------------

So far EasyPubSub has only been tested to connect python instances in a single machine (`localhost`), but as long as 
the network is configured correctly (port forwarding etc.), it should be possible to connect to other machines.
