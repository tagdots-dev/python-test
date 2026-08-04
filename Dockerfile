FROM python:3.14-slim-trixie@sha256:cea0e6040540fb2b965b6e7fb5ffa00871e632eef63719f0ea54bca189ce14a6

ENV PATH="/app/venv/bin:$PATH"
WORKDIR /app

COPY --from=ghcr.io/tarampampam/microcheck /bin/httpcheck /bin/httpcheck
COPY . /app

RUN apt-get update && \
    rm -rf /var/lib/apt/lists/* && \
    groupadd -r pygrp && useradd -M -d /app -r -g pygrp pyuser && \
    chown -R pyuser:pygrp /app

USER pyuser
RUN python -m venv venv && \
    . venv/bin/activate && \
    python -m pip install --no-cache-dir -U pip uv && \
    python -m uv pip install --no-cache-dir -e .

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 CMD /bin/httpcheck http://localhost:8000/health || exit 1

ENTRYPOINT ["python", "src/pkg_15903/main.py"]
