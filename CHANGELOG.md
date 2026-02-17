# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [3.5.0] - 2026-02-16
### Added
- Complete UI/UX overhaul with modern gradients and Material Design.
- New Pause/Resume functionality for downloads.
- Real-time download speed and ETA indicators.
- Colorful icons for different file types in the table view.
- Improved multi-selection (Shift + Click) support.
- Full alignment of versions across all documentation and scripts.

### Fixed
- Cleaned up broken links in README.md.
- Synchronized dependencies between setup.py and requirements.txt.
- Fixed version inconsistencies in i18n and documentation.

## [2.1.1] - 2026-02-08
### Fixed
- `KeyError: 'type'` when displaying files in the table view.
- `QFont::setPointSize` errors on certain system configurations.
- Improved support for all media types during scanning.

## [2.1.0] - 2026-02-08
### Fixed
- Completely resolved the `asyncio event loop is already running` error by ensuring each thread manages its own client and event loop.
- Improved scanning stability and prevented crashes on large channels.
- Enhanced download performance and reliability.

### Added
- Each download and scan operation now runs in a fully independent thread.
- Implemented automatic `disconnect()` after each client operation to free up resources.

## [2.0.0] - 2026-01-15
### Changed
- Complete UI rewrite using **PyQt6**, featuring a modern sidebar navigation, advanced filters, and a professional table view for media.
- Major stability improvements: API authentication now gates scanning, scan results are serialized to prevent data loss, and downloads refetch by message ID for better reliability.

### Added
- Multi-language support for English, Hebrew, Spanish, Russian, and Arabic.
- A new visual selection interface to choose files before downloading.

## [1.0.0] - 2025-12-01
### Added
- Initial release of Telegram Downloader.
- Basic functionality for downloading media from public Telegram channels.
- User interface built with Tkinter.
