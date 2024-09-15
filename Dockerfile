FROM python:3.8-slim-buster

RUN apt update -y && apt install awscli -y &&  apt install -y nginx
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

RUN sudo systemctl daemon-reload && \
    sudo rm -f /etc/nginx/sites-enabled/default && \
    sudo cp nginx.conf /etc/nginx/sites-available/cnncls && \
    sudo ln -s /etc/nginx/sites-available/cnncls /etc/nginx/sites-enabled/ && \
    sudo gpasswd -a www-data ubuntu && \
    sudo systemctl restart nginx && \
    sudo ufw allow 'Nginx Full'

CMD ["python3", "app.py"]

# 3:;04:58