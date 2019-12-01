# Botkun

Create tweet from your timeline.  
By adding entries to database, able to create many variety tweet.

## Required

- Python3
- mecab

## Installation

```sh
git clone https://github.com/lnsf/TwitterBotPy
cd TwitterBotPy
pip3 install -r requirements.txt
./create_config_file.sh
# then edit ~/.botkun.toml
```

## Configuration

Automatically check locations

- ~/.botkun.toml
- ~/.config/botkun.toml
- ~/.config/botkun/botkun.toml

You can specify custom configuration file path using command line argument.

## Usage

```sh
# Get your timeline and add to database
python3 ./main.py add

# Create tweet from database entries
python3 ./main.py tweet

# Clear all database entries
python3 ./main.py clear

# Show config
python3 ./main.py info
```

## Command Line Arguments

```sh
# Show help
python3 ./main.py -h

# Specify configuration path
python3 ./main.py -c CONFIG

# Don't post tweet, only show in console (local mode)
python3 ./main.py -l

# Don't use database
python3 ./main.py --no-database
```
