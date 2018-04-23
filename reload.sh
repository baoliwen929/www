killall -9 uwsgi
nginx -s stop
sleep 2
cd /home/www
uwsgi uwsgiconfig.ini
nginx
