# Project structure

## Project creation

01. Create repo. Clone repo to local

02. Create venv

03. Create folders 

04. Create .env .gitignore

05. Locate data in place and unzip if necessary

06. commit

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

## Project setup

01. Freeze requirements
02. Set .env with ROOT_DIR and PATHS

```bash
pip freeze > requirements.txt
```

## Conventions

### Notebooks

1. Naming: <type>_<number>_<short_description>.ipynb
2. Types: eda, prep

### Preprocessing processes

1. Preprocessing must finish with datasets for modeling: [x_train, x_test, y_train, y_test] or equivalent
2. Data generated in preprocessing must be loaded in dir with the same name of preprocessing file. Intermediate results in data/checkpoint and final data in data/processed.


