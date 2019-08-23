# Botkun

Create tweet from your timeline.  
By adding entries to database, able to create many variety tweet.

## Required

- Python3
- mecab

## Installation

```shell script
git clone https://github.com/lnsf/TwitterBotPy
cd TwitterBotPy
pip3 install -U .
```

## Configuration

Automatically check locations
- ~/.botkun.toml
- ~/.config/botkun.toml
- ~/.config/botkun/botkun.toml

You can specify custom configuration file path using command line argument.


## Usage
```shell script
# Get your timeline and add to database
botkun add

# Create tweet from database entries
botkun tweet

# Clear all database entries
botkun clear

# Show config
botkun info
```

## Command Line Arguments
```shell script
# Show help
botkun -h

# Specify configuration path
botkun -c CONFIG

# Don't post tweet, only show in console (local mode)
botkun -l

# Don't use database
botkun --no-database
```