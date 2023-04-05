FROM nginx

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install bcrypt==4.0.1 numpy==1.23.5 pandas==1.2.2 Pillow==9.3.0 streamlit==1.17.0


COPY ../ /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf
