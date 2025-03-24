FROM nginx
RUN apt-get update && apt-get install certbot python3-certbot-nginx -y
COPY nginx.conf /etc/nginx/nginx.conf
COPY html /var/www/html
EXPOSE 80 443
