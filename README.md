# flaskalicious

a simple flask app to welcome you

### configuration

this app requires you to generate your own `settins.ini` file to store a secret key for managing sessions. that file should look like this

```
[flaskalicious]
secret_key = paste_your_secret_key_here
```

### python 3.9.2

to setup:
```bash
pip install -r requirements.txt
```

to test:
```bash
python app_test.py
```

to initialize database:
```bash
python init_db.py
```

to serve app:
```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

navigate to `http://127.0.0.1:5000` in your favorite web browser and enjoy.

### Docker

to build:
```bash
docker build --tag flaskalicious .
```

to run:
```bash
docker run --publish 5000:5000 flaskalicious
```

navigate to `http://0.0.0.0:5000` in your favorite browser to view app.