# Finance Tracker Bot

A small personal finance tracker bot originally built as a Python Telegram bot.

## GitHub Finish-Up-A-Thon 2026

This repository started as a small Python Telegram bot for personal finance tracking.

The original prototype was working, but the project was never properly finished: it had minimal documentation, no CI, no Docker setup, and no production-style structure.

For the GitHub Finish-Up-A-Thon 2026, I am reviving the project by rebuilding the core idea in .NET — the stack I use professionally — while keeping the original Python version as the legacy baseline.

The original Python implementation will be kept in `/legacy-python` as the “before” state.
The new .NET version will become the “after” state.

## Revival roadmap

Progress is tracked through GitHub Issues:

* [ ] Preserve the original Python version in `/legacy-python` — #1
* [ ] Create the .NET solution structure — #2
* [ ] Implement basic Telegram commands — #3
* [ ] Add SQLite persistence — #4
* [ ] Add Docker support — #5
* [ ] Add CI with GitHub Actions — #6

## Planned MVP scope

The revived .NET version will focus on a small, usable feature set:

* `/start` — introduce the bot
* `/help` — show available commands
* `/add` — add a new expense
* `/today` — show today’s expenses
* `/month` — show monthly summary

## Before / After

### Before

* Working Python prototype
* Local SQLite database
* Minimal README
* No documented setup
* No CI
* No Docker support

### After

* Rebuilt in .NET
* Clear project structure
* SQLite persistence
* Telegram bot commands
* Docker support
* GitHub Actions CI
* Updated documentation
