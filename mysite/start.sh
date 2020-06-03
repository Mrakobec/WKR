#!/bin/sh
#

docker-compose rm -sf ; docker-compose up --no-start; docker-compose start
echo Use docker-compose logs -f


