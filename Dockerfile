FROM httpd:latest
COPY . /usr/local/apache2/htdocs/

EXPOSE 80
EXPOSE 8501

CMD ["httpd-foreground"]