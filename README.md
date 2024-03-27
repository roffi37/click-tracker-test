# click-tracker-test

This is simple django project to track user data when they are use our API.


## Features

- Track user data
- Watch user data in admin panel
- Create shorten link with custom API


## Installation

1. Clone repository

```bash
git clone https://github.com/roffi37/click-tracker-test.git
```
2. Set parameters in .env
3. Run docker compose
```bash
docker-compose up --build
```
4. Load data with base admin
```bash
docker ps
docker exec -it <YOUR COUNTAINER ID> sh
python manage.py loaddata db.json
```

## Test project

1. To track, get shorten link and redirect to "Thank you page"

```bash
http://0.0.0.0:8000/track/<your_site>/
```

2. To track, get shorten link and redirect to origin page

```bash
http://0.0.0.0:8000/track/<your_site>/origin/
```
3. To see data visit admin panel
```bash
http://0.0.0.0:8000/admin/
```

Credentials:
- `username`: **admin**
- `password`: **1234**
