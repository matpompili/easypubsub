# Changelog

## [v0.2.2](https://github.com/matpompili/easypubsub/tree/v0.2.2) (Ureleased)

- Added documentation to the `Proxy`, `Subscriber`, and `Publisher` classes.
- Setup Sphinx documentation and Readthedocs.

[Full Changelog](https://github.com/matpompili/easypubsub/compare/v0.2.1...main)

## [v0.2.1](https://github.com/matpompili/easypubsub/tree/v0.2.1) (2022-07-29)

[Full Changelog](https://github.com/matpompili/easypubsub/compare/v0.2.0...v0.2.1)

- Fixed a bug for Proxy, where it would not quit using CTRL-C on Windows.
- Added `CHANGELOG.md` to the repository.
- `Proxy` now runs in a separate thread, so it is non-blocking.
- Created a few simple tests.