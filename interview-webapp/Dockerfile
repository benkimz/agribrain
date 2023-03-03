FROM python:3.8-slim-buster

COPY . /app/

WORKDIR /app/

RUN python -m pip install --upgrade pip

RUN python -m pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "interview.py"]