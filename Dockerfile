# syntax=docker/dockerfile:1.2

FROM python:3.8-buster AS builder
WORKDIR /app

# `RELEASE` makes `bin/install` to skip dev-requirements, to skip copy of root project.
ENV PYTHONUNBUFFERED=1 RELEASE=true

COPY bin /app/bin
COPY poetry.lock pyproject.toml /app/

# Install - only when e.g. `pyproject.toml` is updated.
RUN /app/bin/install

# Restart image to reduce its size.
FROM python:3.8-buster AS release
WORKDIR /app

# Copy just requirements without poetry and its cache.
COPY --from=builder /app/.venv /app/.venv

# Copy release files starting from least frequently updated.
COPY bin /app/bin
COPY src /app/src

ENV PYTHONUNBUFFERED=1 PYTHONPATH="/app/src:/app/.venv/lib/python3.8/site-packages"

CMD ["/app/bin/run"]
