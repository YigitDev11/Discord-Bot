# NOVUM — Fresh-line

**Fresh-line** is the first generation of NOVUM's modular Discord software platform, built with Python and `discord.py`.

It provides a clean, extensible foundation for building Discord bots without coupling the entire application to a single monolithic implementation.

> **Status:** `v0.1.0-beta` · **Stage:** MVP / Foundation

## Overview

NOVUM Fresh-line is currently focused on the developer-facing foundation of the platform.

The current release provides the core infrastructure required to develop and extend a Discord bot:

* Slash command support
* Modular Cog and extension architecture
* Centralized configuration
* Environment variable support
* Structured application logging
* Daily log files
* Centralized event handling
* Custom exception hierarchy

Fresh-line is **not yet a finished end-user Discord bot**. The current release is intended primarily as a development foundation for the NOVUM platform.

## Architecture

Fresh-line follows a modular architecture built around `discord.py`.

Core responsibilities are separated into dedicated components for configuration, bot initialization, event handling, extension loading, logging, and exception management.

This structure is designed to keep individual features isolated and make the platform easier to maintain as additional functionality is introduced.

## Features

### Slash Commands

Fresh-line supports Discord application commands through `discord.py`.

Commands can be implemented independently inside Cogs while the core bot remains responsible for initialization and application-level infrastructure.

### Cogs & Extensions

Functionality is organized through Discord.py Cogs and extensions.

This allows features to be developed and maintained independently rather than accumulating application logic inside the main bot implementation.

### Configuration

Configuration is centralized and environment-aware.

Sensitive values such as the Discord bot token are loaded through environment variables and are not required to be stored directly in source code.

### Logging

Fresh-line includes a centralized logging system designed for development and debugging.

Current logging capabilities include:

* Configurable log levels
* Daily log files
* Timestamped entries
* Timezone-aware logging
* Centralized logger configuration

Application logs are stored in the `logs/` directory.

### Error Handling

The core includes a custom exception hierarchy for representing application, user, configuration, service, API, database, and external-service errors.

This provides a consistent foundation for handling failures as the platform grows.

## Project Structure

```text
fresh-line/
├── cogs/
│   └── ping.py
├── core/
│   ├── bot.py
│   ├── config.py
│   ├── events.py
│   ├── exceptions.py
│   ├── extension_loader.py
│   └── logger.py
├── logs/
├── .env
├── .env.example
├── .gitignore
├── main.py
└── pyproject.toml
```

## Requirements

* Python 3.x
* A Discord application
* A Discord bot token
* Dependencies defined in `pyproject.toml`

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd fresh-line
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the project:

```bash
pip install .
```

Create the environment configuration:

```bash
cp .env.example .env
```

Configure the required values in `.env` before starting the bot.

## Configuration

Fresh-line uses environment variables for runtime configuration.

An example configuration is provided in:

```text
.env.example
```

Create a local `.env` file from this template and provide the required values.

**Do not commit `.env` or expose your Discord bot token.**

## Running

After configuring the environment, start Fresh-line with:

```bash
python main.py
```

The application will initialize the bot, configure its core services, load the configured extensions, and synchronize its application commands.

## Development

Fresh-line is currently developed as a foundation for the NOVUM platform.

The current development priorities are:

1. Stable core architecture
2. Modular extensibility
3. Reliable error handling
4. Maintainable configuration
5. Consistent logging
6. A clean foundation for future generations and features

## Roadmap

The roadmap will evolve throughout the Fresh-line development cycle.

Planned areas include:

* Additional Discord functionality
* Expanded command modules
* Improved developer tooling
* Further architectural refinement
* Production-oriented improvements
* End-user functionality
* Future NOVUM generations

## Contributing

Fresh-line is currently in an early beta stage.

Technical feedback, issues, and contributions are welcome.

For significant architectural changes, opening an issue before implementation is recommended so the proposed change can be discussed first.

## License

License information will be added in a future release.

---

**NOVUM**

*Fresh-line — the first generation.*
