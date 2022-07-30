# Changelog

## [v0.3.0](https://github.com/matpompili/easypubsub/tree/v0.3.0) (Ureleased)

- Added documentation to the `Proxy`, `Subscriber`, and `Publisher` classes.
- Setup Sphinx documentation and Readthedocs.
- Breaking change: `easypubsub.Proxy` now expects first the address for the publishers and then the address for the subscribers, to make it easier to remember (pub-sub). Fixed tests and examples accordingly.

[Full Changelog](https://github.com/matpompili/easypubsub/compare/v0.2.1...v0.3.0)

## [v0.2.1](https://github.com/matpompili/easypubsub/tree/v0.2.1) (2022-07-29)

[Full Changelog](https://github.com/matpompili/easypubsub/compare/v0.2.0...v0.2.1)

- Fixed a bug for Proxy, where it would not quit using CTRL-C on Windows.
- Added `CHANGELOG.md` to the repository.
- `Proxy` now runs in a separate thread, so it is non-blocking.
- Created a few simple tests.