FROM httpd:latest

COPY . /usr/local/apache2/htdocs/

WORKDIR /usr/local/apache2/htdocs/

EXPOSE 80

CMD ["httpd-foreground"]

FROM python:3.9-slim-buster

COPY ./streamlit/ /app/

WORKDIR /app/

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "interview.py", "--server.port=8501", "--server.address=0.0.0.0"] 
