service supervisor stop
python ginkgoapp/manage.py makemigrations
python ginkgoapp/manage.py migrate
npm run build
supervisord -c conf/supervisord.conf
