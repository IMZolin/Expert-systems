### Expert systems Telegram bot 

Telergam bot for organizing lab work on the topic: Expert Systems

Tasks:

1. Caesar's cipher
    - You are given an encrypted word as input, you don't know the shift
    - You have to implement a decryptor that goes through all the possible shifts
    - Decrypt the resulting word
2. Hiring
   - Each candidate has 4 characteristics: 
     - Level (junior/middle/senior)
     - Programming language (Python/C++/Java/R) 
      One candidate = one language
     - higher education level (yes/no)
     - Favorite OS (Windows/Linux/MacOS)
   - Candidate = [level, language, higher education, OS]
   - You are given a list of 10 candidates(candidate[i] = (junior, -, -, -) candidate[j] = (middle, C++, yes, -))
   - So you also know the "ideal" candidate pattern. If the person does not meet this template, you refuse him, otherwise you hire him.
   - You need to implement a control system (function Select) with a strategy of the first fit that brings us closer to a decision, which will return either the decision made (hire/reject) or the next question to ask the candidate.
   - Example:
    Let perf_cand = [middle, -, yes, windows/linux]
      At this point, we query candidate = [senior, ?, yes, ?]

   - The next question should be about the OS, not the language! Since the company does not care what language the candidate writes in.
3. Information entropy
   - You are given 10 different lines of labels = [...].
   - You need to implement 2 functions: class_probabilities and entropy. The first one calculates class_probabilities and the second one entropy of those classes.
   - As a response the bot also accepts 10 lines with entropy values for each line labels = ... 
   - Note: Each value in the message should be on a separate line
  
URL: https://t.me/ExpertSystemsBot
<hr>

- [Bot structure](#bot-structure)
- [Getting started](#getting-started)
  - [First steps](#first-steps)
  - [Configure environment variables](#configure-environment-variables)
  - [Bot settings:](#bot-settings)
  - [Database](#database)
- [Docker](#docker)
  - [Start bot](#start-bot)
  - [Manage bot container](#manage-bot-container)
  - [View bot logs](#view-bot-logs)
  - [Stop bot](#stop-bot)
  - [Database postgres](#database-postgres)
    - [Manage postgres via psql](#manage-postgres-via-psql)
    - [Migrations](#migrations)
      - [Create revision](#create-revision)
      - [Upgrade database](#upgrade-database)
  - [I18n locales](#i18n-locales)
    - [Create locales](#create-locales)
    - [Update locales](#update-locales)
<hr>

## Bot structure
```bash
├───bin                 # some bash scripts for docker
├───bot
│   ├───filters         # some aiogram filters
│   ├───handlers
│   │   ├───errors      # error handlers
│   │   ├───tasks       # tasks handlers
│   │   └───users       # message handlers
│   ├───keyboards
│   │   ├───default     # aiogram markups
│   │   └───inline      # aiogram inline markups
│   ├───middlewares     # aiogram middlewares
│   └───states          # aiogram states
├───data
│   ├───locales         # i18n locales
│   └───logs            # bot logs
├───models              # database models
├───services            # database services
└───utils               # some helpful things
```

## Getting started

### First steps
```bash
git clone https://github.com/IMZolin/Expert-systems.git <your project name>
cd <your project name>
pip install -r requirements.txt

# initialize database
pw_migrate migrate --database $(python _get_database_url.py) --directory ./migrations
# or if you have make you can simply type 
make db_upgrade
# run pooling
python main.py
```

### Configure environment variables
Copy file `.env.dist` and rename it to `.env`
```
cp .env.dist .env
```
Than configure variables
```bash
vim .env
# or 
nano .env
```

### Bot settings:

`ADMINS` - administrators ids divided by ,
```bash
# example
ADMINS=12345678,12345677,12345676
# or one admin
ADMINS=12345678
```
`BOT_TOKEN` - bot token from [@BotFather](https://t.me/BotFather)
```bash
# example
BOT_TOKEN=123452345243:Asdfasdfasf
```
`RATE_LIMIT` - throttling rate limit (anti-spam)
```bash
# example
RATE_LIMIT=0.5 # seconds
```
### Database
Sqlite by default but if you want to use postgres you can configurate it

```bash
# Dababase postgres
DB_USER=<some username>
DB_PASSWORD=<some password>
DB_HOST=localhost
DB_PORT=5432
DB_NAME=<some database name>
```

## Docker 
### Start bot
```bash
# grant execution rights
chmod +x ./bin/entrypoint.sh
docker-compose up -d --force-recreate
# or if you have make you can simply type 
make run
# or only make
make 
```
### Manage bot container
```bash
docker-compose exec bot /bin/bash
# or if you have make you can simply type 
make exec
```
### View bot logs
```bash
docker-compose logs -f bot
# or if you have make you can simply type 
make logs
```

### Stop bot
```bash
docker-compose stop
# or if you have make you can simply type 
make stop
```
### Database postgres
#### Manage postgres via psql
```bash
docker-compose exec postgres psql -U postgres postgres
# or if you have make you can simply type 
make psql
```
#### Migrations
##### Create revision
```bash
pw_migrate create --auto --database $(python _get_database_url.py) --directory ./migrations "<some revision message>"
# or if you have make you can simply type 
make db_revision "<some revision message>"
```
##### Upgrade database
```bash
pw_migrate migrate --database $(python _get_database_url.py) --directory ./migrations
# or if you have make you can simply type 
make db_upgrade
```

### I18n locales

#### Create locales

first you should extract all messages from bot
```bash
pybabel extract --input-dirs=. -o data/locales/bot.pot --project=bot
# or if you have make you can simply type 
make pybabel_extract
```
then init languages
```bash
pybabel init -i data/locales/bot.pot -d data/locales -D bot -l <language code>
# or if you have make you can simply type 
$ make pybabel_init <language code>
```
finaly translate messages in `/data/locales/<language code>/LC_MESSAGES/bot.po` and compile translations
```bash
pybabel compile -d data/locales -D bot --statistics
# or if you have make you can simply type 
make pybabel_compile
```
#### Update locales
to add new messages to already existing translations you should `extract again` and then write this command
```bash
pybabel update -i data/locales/bot.pot -d data/locales -D bot
# or if you have make you can simply type 
make pybabel_update
```
and finaly translate and `compile again`