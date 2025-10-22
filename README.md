# Handcoding

404 Found's hand-coding activity where participants write their Python scripts on a whiteboard, without any external help. Just you and your brain *(and your marker)*.

This repository contains source code of all the problems presented during the activity.

## Download contents

1. Download the repository as a `.zip` file. (It's located at the green `<> code` button on top)
2. Extract its contents into a folder
3. Go inside that folder and open it in your preferred code editor (Spyder, Visual Studio Code, etc.)

## Set up Virtual Environment (optional, but recommended)

1. Open a terminal and enter the script below

```shell
python -m venv .venv
# Try `python3 -m venv .venv` if above doesn't work
```

This will set up a little sandbox so that modules from your other Python projects won't overlap

2. Once you see a `.venv` folder show up with the other files, run this command to enter the virtual environment

```shell
# Windows:
.venv/Scripts/activate

# Linux and Mac:
source .venv/bin/activate
```
If all goes well, you should be in your virtual environment. If all doesn't go well, I'm sorry maybe you need to search for a tutorial somewhere o|-<

## Install requirements.txt

`requirements.txt` contains all the prerequisite modules to run this project. To install them, run:

```shell
pip install -r requirements.txt
```

Once they're installed, you're good to go!

## What now?

Well, you can run these scripts like any Python file you've made. Maybe you use a `run` button, or you go into the terminal and type

```shell
python practice-problems/fizzbuzz.py
```

At this point, everything should work fine. Happy testing!