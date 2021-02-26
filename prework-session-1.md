# Prework for Session One

## Environment assumptions
This course assumes you have ...
1. A [GitHub](https://github.com) account.
1. Python3 3.5 or newer, so that the builtin 'venv' module can be used for configuring virtual environments.

## Fork & clone the repo, and set up and run the webapp

Fork this repo from https://github.com/walquis/tags.

Run these commands in a Terminal session (for best results, I recommend starting Terminal.app separately, rather than using the terminal session within your IDE).  You should be able to copy/paste pretty much verbatim, except for supplying \<yourlogin\>...
```bash
cd # Start from your home directory
mkdir -p src; cd src  # Or cd to wherever you keep code projects
git clone https://github.com/\<yourlogin\>/tags # Clone your fork
# Or use ssh protocol...  $ git clone git@github.com:\<yourlogin\>/tags
cd tags
mkdir ../shared  # In case you want to share config across releases
cp config.yml.sample ../shared/config.yml
python3 -m venv venv  # Make a virtual env in the "venv" directory
source venv/bin/activate  # Enter your python3 virtual env
pip install -r requirements.txt  # Populate current virtual env with packages
python bin/load_schema.py   # Init your DB structure. Assumes FLASK_ENV=development
python bin/seed.py   # Add data to your DB.  Assumes FLASK_ENV=development
bin/run-flask-webserver.sh  # Assumes FLASK_ENV=development
```
Now visit [Your LocalHost](http://localhost:5000){:target="_blank"} in your browser.

To stop the app: At your shell prompt, hold down the Ctrl key and press 'c'.

To exit your virtualenv: In the terminal, type 'deactivate'.

