FROM python:3.13-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv && uv sync --no-dev

COPY . /app

EXPOSE 8000

CMD ["uv", "run", "fastapi", "run", "src/main.py"]
