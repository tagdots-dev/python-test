FROM ghcr.io/tarampampam/microcheck:1.4.0 AS httpcheck-bin

FROM python:3.14-slim-trixie@sha256:bf503bb2243c5aad0aa951544dd60d165f992646441d35dea90893703fc26251

ENV PATH="/app/venv/bin:$PATH"
WORKDIR /app

COPY --from=httpcheck-bin /bin/httpcheck /bin/httpcheck
COPY . /app

RUN apt-get update && \
    rm -rf /var/lib/apt/lists/* && \
    groupadd -r pygrp && useradd -M -d /app -r -g pygrp -u 10001 pyuser && \
    chown -R pyuser:pygrp /app

USER 10001
RUN python -m venv venv && \
    . venv/bin/activate && \
    python -m pip install --no-cache-dir -U pip uv && \
    python -m uv pip install --no-cache-dir -e .

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 CMD /bin/httpcheck http://localhost:8000/health || exit 1

ENTRYPOINT ["python", "src/pkg_15903/main.py"]
