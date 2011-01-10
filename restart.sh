
pkill nginx
pkill python

cp /var/FlavorPages/nginx.conf /etc/nginx/

python /var/FlavorPages/app/__init__.py 8000
python /var/FlavorPages/app/__init__.py 8001
python /var/FlavorPages/app/__init__.py 8002
python /var/FlavorPages/app/__init__.py 8003

/etc/init.d/nginx start
