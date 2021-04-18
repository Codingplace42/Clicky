# README
This project is a basic Click Counting example in Django Channels.
Many users can click from different hosts and will get realtime updates on
current click count and last timestamp.

# Requirements & Setup
There are two setup possibilities included:
- local setup
- docker setup (recommended)

**General Setup**
You will need following steps, doesn't matter if you gonna use this setup in
local requirements or containerized:

1. Clone this repository
```
git clone https://github.com/Codingplace42/Clicky.git
```

2. Init submodule
```
git submodule init
```

3. Update Submodule (this will pull the used SB-Admin-2 Repository for Frontend)
```
git submodule update
```

4. Create `.env` File by copying the example file:
```
cp clicky/.env.example clicky/.env
```
Change the values inside of that file depends on the setup what you want to use.


## Local Requirements & Setup
- Python v. 3.6 or higher is required
- PostgresQL Database (optional - alternative: Change DB Settings to Sqlite)
- Redis

5. Install Requirements
```
pip install -r requirements.txt
```
_Note: A virtual environment is recommended here_

6. Migrate the database
```
python manage.py migrate
```
_Note: Make sure that correct parameters in your .env file are set_

7. Start Server
```
python manage.py runserver
```

## Docker Requirements & Setup
- Docker
- Docker Compose

5. Start docker composition
```
docker-compose up
```
_Note: Make sure that correct parameters in your .env file are set_

**About The Docker Setup**
Services for Postgres, Redis and Nginx are included in the docker-composition.
Make sure that you've used the correct ports in your .env file for being able
to communicate between services.

**Cheat** For local development I do recommend to start redis and postgres via
docker setup and run the django project separate in local configuration.
