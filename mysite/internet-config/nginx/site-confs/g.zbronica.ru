server {
	listen 80 ;
        listen 443 http2 ssl;
        ssl_certificate /config/etc/letsencrypt/live/g.zbronica.ru/fullchain.pem;
        ssl_certificate_key /config/etc/letsencrypt/live/g.zbronica.ru/privkey.pem;
        include /config/nginx/ssl.conf;

	server_name g.zbronica.ru;

	location /static {
		alias /var/www/mysite/static;	
		sendfile on;
	}
	location / {
		proxy_pass http://mysite:8000;
	}
}
