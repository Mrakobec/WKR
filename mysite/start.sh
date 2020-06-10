#!/bin/sh
#

docker-compose rm -sf ; docker-compose up --no-start; docker-compose start
# 
echo Doing some post-start things
docker cp ./sqliteadmin/phpliteadmin.config.php mysite_phpliteadmin_1:/srv/phpliteadmin.config.php 
docker exec -ti mysite_mysite_1 python ./manage.py collectstatic --noinput
docker exec -ti mysite_mysite_1 chown -R 1000:1000 static_media
#
echo Use docker-compose logs -f


