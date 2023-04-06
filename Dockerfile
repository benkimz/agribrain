FROM httpd:latest

COPY . /usr/local/apache2/htdocs/

WORKDIR /usr/local/apache2/htdocs/

RUN pip3 install --no-cache-dir -r streamlit/requirements.txt

EXPOSE 80

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

CMD ["httpd-foreground"] 

ENTRYPOINT ["streamlit", "run", "interview.py", "--server.port=8501", "--server.address=0.0.0.0"]
