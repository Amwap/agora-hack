# ZADEPLOYME как тимлид учил

## postgres
Меняю метод аутентификации пользователя в postgresql
sudo nano /etc/postgresql/12/main/pg_hba.conf
"local" is for Unix domain socket connections only
    local  all      all      md5

CREATE ROLE webcats WITH LOGIN ENCRYPTED PASSWORD 'webcats_pass';
CREATE DATABASE webcats WITH OWNER webcats;

## python 
python3.10 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

## nginx 
sudo ln -s "$PWD/config/systemd/webcats_backend.service" /etc/systemd/system/
sudo ln -s "$PWD/config/systemd/webcats_frontend.service" /etc/systemd/system/

## systemd
sudo ln -s "$PWD/config/nginx/webcats_nginx.conf" /etc/nginx/sites-available/
sudo ln -s "$PWD/config/nginx/webcats_nginx.conf" /etc/nginx/sites-enabled/