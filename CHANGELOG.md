# Changelog

## [Unreleased](https://github.com/matpompili/easypubsub/tree/main)

[Full Unreleased Changelog](https://github.com/matpompili/easypubsub/compare/v0.4.2...main)

## [v0.4.2](https://github.com/matpompili/easypubsub/tree/v0.4.2) (2022-09-01)

-   Add :obj:`~easypubsub.decorator.publish_this` decorator to automatically publish function return values to a topic.
-   Make `requirements.txt` less strict.

[Full v0.4.2 Changelog](https://github.com/matpompili/easypubsub/compare/v0.4.1...v0.4.2)

## [v0.4.1](https://github.com/matpompili/easypubsub/tree/v0.4.1) (2022-08-25)

-   Added safer exception handling for the `publish` method of :obj:`~easypubsub.publisher.Publisher`.

[Full v0.4.1 Changelog](https://github.com/matpompili/easypubsub/compare/v0.4.0...v0.4.1)

## [v0.4.0](https://github.com/matpompili/easypubsub/tree/v0.4.0) (2022-08-04)

-   Update :obj:`~easypubsub.proxy.Proxy` to use `zmq.devices.ThreadProxySteerable`, which supports better termination handling.
-   Improve documentation and update example scripts.
-   Fixed some typos in the documentation and variables names.
-   Removed wait times in :obj:`~easypubsub.proxy.Proxy` and :obj:`~easypubsub.subscriber.Subscriber`, the user should take care of waiting long enough to establish the connection.

[Full v0.4.0 Changelog](https://github.com/matpompili/easypubsub/compare/v0.3.1...v0.4.0)

## [v0.3.1](https://github.com/matpompili/easypubsub/tree/v0.3.1) (2022-08-02)

-   Fix link in the pypi package description.
-   Fix missed release date for v0.3.0 in `CHANGELOG.md`.
-   Use MyST to include Markdown files in the docs instead of `m2r2`, which has security issues.
-   Add bump2version configuration, to manage the versioning.
-   Added `__version__` to the `easypubsub` package.

[Full v0.3.1 Changelog](https://github.com/matpompili/easypubsub/compare/v0.3.0...v0.3.1)

## [v0.3.0](https://github.com/matpompili/easypubsub/tree/v0.3.0) (2022-08-01)

-   Added documentation to the :obj:`~easypubsub.proxy.Proxy`, :obj:`~easypubsub.subscriber.Subscriber`, and :obj:`~easypubsub.publisher.Publisher` classes.
-   Setup Sphinx documentation and Readthedocs.
-   Breaking change: :obj:`~easypubsub.proxy.Proxy` now expects first the address for the publishers and then the address for the subscribers, to make it easier to remember (pub-sub). Fixed tests and examples accordingly.

[Full v0.3.0 Changelog](https://github.com/matpompili/easypubsub/compare/v0.2.1...v0.3.0)

## [v0.2.1](https://github.com/matpompili/easypubsub/tree/v0.2.1) (2022-07-29)

-   Fixed a bug for Proxy, where it would not quit using CTRL-C on Windows.
-   Added `CHANGELOG.md` to the repository.
-   `Proxy` now runs in a separate thread, so it is non-blocking.
-   Created a few simple tests.

[Full v0.2.1 Changelog](https://github.com/matpompili/easypubsub/compare/v0.2.0...v0.2.1)
