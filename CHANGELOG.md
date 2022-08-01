# Changelog

## [v0.3.1](https://github.com/matpompili/easypubsub/tree/v0.3.1) (Unreleased)

- Fix link in the pypi package description.
- Fix missed release date for v0.3.0 in `CHANGELOG.md`.

[Full v0.3.1 Changelog](https://github.com/matpompili/easypubsub/compare/v0.3.0...v0.3.1)

## [v0.3.0](https://github.com/matpompili/easypubsub/tree/v0.3.0) (2022-08-01)

- Added documentation to the :obj:`~easypubsub.proxy.Proxy`, :obj:`~easypubsub.subscriber.Subscriber`, and :obj:`~easypubsub.publisher.Publisher` classes.
- Setup Sphinx documentation and Readthedocs.
- Breaking change: :obj:`~easypubsub.proxy.Proxy` now expects first the address for the publishers and then the address for the subscribers, to make it easier to remember (pub-sub). Fixed tests and examples accordingly.

[Full v0.3.0 Changelog](https://github.com/matpompili/easypubsub/compare/v0.2.1...v0.3.0)

## [v0.2.1](https://github.com/matpompili/easypubsub/tree/v0.2.1) (2022-07-29)

- Fixed a bug for Proxy, where it would not quit using CTRL-C on Windows.
- Added `CHANGELOG.md` to the repository.
- `Proxy` now runs in a separate thread, so it is non-blocking.
- Created a few simple tests.

[Full v0.2.1 Changelog](https://github.com/matpompili/easypubsub/compare/v0.2.0...v0.2.1)