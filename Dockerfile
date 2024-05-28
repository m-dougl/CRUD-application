FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install poetry

RUN poetry install

RUN poetry config virtualenvs.create false

EXPOSE 8501

CMD ["poetry", "run", "streamlit", "run", "app.py"]
