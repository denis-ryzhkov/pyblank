# TODO

An almost blank Python project template.

## Install

```
bin/install
```

## Run

```
bin/run
```

* To enable [Sentry](https://sentry.io/): `export SENTRY_DSN=...` before running.

## Develop

```
. .venv/bin/activate
poe lint  # with auto-fix
poe test
poe lt  # `lint` + `test`
poe ci  # read-only `lint` + `test` for CI/CD
```
