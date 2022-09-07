# 🗞️ easypubsub
[![Documentation Status](https://readthedocs.org/projects/easypubsub/badge/?version=latest)](https://easypubsub.readthedocs.io/en/latest/?badge=latest)
[![PyPI](https://img.shields.io/pypi/v/easypubsub)](https://pypi.org/project/easypubsub/)
[![License: MIT](https://img.shields.io/badge/license-MIT-brightgreen)](https://github.com/matpompili/easypubsub/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://github.com/matpompili/easypubsub/actions/workflows/python-package.yml/badge.svg)](https://github.com/matpompili/easypubsub/actions/workflows/python-package.yml)

**easypubsub** is a simple wrapper around [PyZMQ](https://pyzmq.readthedocs.io/en/latest/) that provides an easy interface to the *PubSub* (Publish-Subscribe) functionality of [ZeroMQ](https://zeromq.org/). 

In PubSub, a *publisher* publishes a message to a *topic* and a *subscriber* subscribes to that topic and receives the message. In easypubsub, publishers and subscribers connect to each other via a *proxy*, which acts as intermediary between them.
For more information regarding *PubSub*, see [Wikipedia](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern).