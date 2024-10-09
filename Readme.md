# Project structure

## Project creation

01. Create repo. Clone repo to local

02. Create venv

03. Create folders 

04. Create .env .gitignore

05. Locate data in place and unzip if necessary

```bash
python3 -m venv venv
source venv/bin/activate
mkdir data data/processed data/raw data/checkpoint
mkdir notebooks src docs artifacts
touch .env .gitignore
echo .env > .gitignore
echo venv >> .gitignore
echo data/ >> .gitignore
cd data/raw; unzip titanic.zip
```