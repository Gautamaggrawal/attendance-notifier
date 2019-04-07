# attendance-notifier


sudo cp webkiosk_celery.conf /etc/supervisor/conf.d/
sudo cp webkiosk_celerybeat.conf /etc/supervisor/conf.d/

sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl status webkioskcelerybeat
sudo supervisorctl status webkioskcelery
