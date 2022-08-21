git checkout main
git reset HEAD --hard
git clean -fd
git pull

backend/venv/bin/pip install -r backend/requirements.txt
backend/venv/bin/python backend/manage.py migrate
backend/venv/bin/python backend/manage.py collectstatic --noinput

cd frontend
npm i
npm run build

echo '12345' | sudo -S systemctl restart webcats_frontend
echo '12345' | sudo -S systemctl restart webcats_backend