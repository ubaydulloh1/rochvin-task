# Task

### clone repository && cd

```bash
git clone https://github.com/ubaydulloh1/rochvin-task.git
cd rochvin-task
```

### run without docker

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### run with docker

```bash
docker-compose -f dev-compose.yml up -d --build
docker exec -it rochwin_task-django python manage.py migrate
```
