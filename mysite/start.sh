#!/bin/sh
#

docker-compose rm -sf ; docker-compose up --no-start; docker-compose start
docker cp ./sqliteadmin/phpliteadmin.config.php mysite_phpliteadmin_1:/srv/phpliteadmin.config.php 
echo Use docker-compose logs -f


