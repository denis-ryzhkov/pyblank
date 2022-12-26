# TODO

An almost blank Python project template.

## Installation

### Docker for production

* Docker is required.
* Run: `bin/install -d`

### Local development

* Python 3.8.1+ is required.
* Run: `bin/install`
```

## Configuration

* Please edit `.env` file created on installation:
    * Set required TODO.
    * Each network request is limited to `TIMEOUT_SECONDS=30`, adjustable.
    * To enable [Sentry](https://sentry.io/) for notification on errors, set `SENTRY_DSN`.
    * You may also add other
      [Sentry options](https://docs.sentry.io/platforms/python/configuration/options/)
      like `SENTRY_ENVIRONMENT`.

* You may also set environment variables to override `.env`, see "Usage" section.

## Usage

### Docker for production

* Run: `bin/run -d`
* To override `.env`, run e.g. `bin/run -d -e DEBUG=true`

### Local development

* Run: `bin/run`
* To override `.env`, run e.g. `DEBUG=true bin/run`

## Development

### Lint and test the code

```
. .venv/bin/activate
poe lint  # with auto-fix
poe test
poe lt  # `lint` + `test`
poe ci  # read-only `lint` + `test` for CI/CD
```
