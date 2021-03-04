# Prework for Session One

## Environment assumptions
This course assumes you have ...
1. A [GitHub](https://github.com){:target="_blank"} account.
1. Python3 3.5 or newer, so that the builtin 'venv' module can be used for configuring virtual environments.

## Fork & clone the repo, and set up and run the webapp

Fork and clone [Tags](https://github.com/walquis/tags){:target="_blank"}.

Run these commands in a Terminal session (for best results, I recommend starting Terminal.app separately, rather than running a terminal session within your IDE).  You should be able to copy/paste pretty much verbatim, except that you need to replace \<yourlogin\> with your own login.
```console
$ cd                          # Start from your home directory
$ mkdir -p src
$ cd src                      # Or cd to wherever you keep code projects
$ git clone https://github.com/<yourlogin>/tags    # Clone your fork
# Or use ssh protocol...  $ git clone git@github.com:<yourlogin>/tags
$ cd tags
$ mkdir ../shared             # In case you want to share config across releases
$ cp config.yml.sample ../shared/config.yml
$ python3 -m venv venv        # Use the "venv" module to create a virtual env in the "venv" directory
$ source venv/bin/activate         # Enter your python3 virtual env
$ pip install -r requirements.txt  # Populate current virtual env with packages
$ python bin/load_schema.py   # Init your DB structure. Assumes FLASK_ENV=development
$ python bin/seed.py          # Add data to your DB.  Assumes FLASK_ENV=development
$ bin/run-flask-webserver.sh  # Assumes FLASK_ENV=development
```
Now visit [Your LocalHost](http://localhost:5000){:target="_blank"} in your browser.

To stop the app: At your shell prompt, hold down the Ctrl key and press 'c'.

To exit your virtualenv: In the terminal, type 'deactivate'.

## Explore the code
So what have we got running, exactly?  Take a look at ```app.py```.  The main pieces we're pulling in are [Flask](https://palletsprojects.com/p/flask/){:target="_blank"} for web services, and [peewee](http://docs.peewee-orm.com/){:target="_blank"} for our "Object-Relational Mapper", or [ORM](https://blog.bitsrc.io/what-is-an-orm-and-why-you-should-use-it-b2b6f75f5e2a).  Peewee is using a [Sqlite](https://www.sqlite.org/){:target="_blank"} database adapter for this project; Sqlite is the simplest of the databases for which Peewee offers adapters (two others are PostgreSQL and MySQL).

All three of these--Flask, Peewee, and Sqlite--are very simple instances of their respective generas.  For instance, roughly speaking Flask is to Django as a Raspberry Pi is to a Macbook.  Simple can be very useful!

```app.y``` also implements simple but powerful environment management.  NOTE: By 'environment' in this context, I'm referring to deployment destinations, such as "production", "uat", or "development".  Another definition of 'environment' is also in play, and it's actually in the same line of code: ```os.environ.get('FLASK_ENV')```.  The ```os.environ``` usage of 'environment' refers to shell environment variables available to the process--one of which, named FLASK_ENV, controls which _deployment_ environment we're going to use.  Confusing, yes, but necessary to know.

Anyway, back to the deployment environment.  The value of FLASK_ENV ('deployment' by default) selects a corresponding section in config/database.yml that tells it about the deployment--namely, which database to use; because yes it's handy not to do development with production databases.

### A side note - Debugging with [ipython](https://ipython.readthedocs.io/en/stable/){:target="_blank"}

Notice the commented-out ```# embed()``` (as well as the ```from IPython import embed```).  Try uncommenting this line, and restarting the server.  Code execution now stops at the embed() breakpoint.  You can examine variables by typing them (for instance ```dbname```), or run arbitrary code that makes sense in this context.  For instance, ```load_config('config/database.yml')[FLASK_ENV]``` will show you what makes up the 'development' environment's config.  How would you look at all of the config file's contents from IPython?

When ready to continue, type ```quit```.

### Another side note - looking at the Sqlite data directly

If you want to browse your DB outside of Flask/peewee, just install Sqlite.  On a Mac, this would be
```
brew install sqlite
```
Where does your Sqlite database live?  [HINT: The path to the database file is part of the config that the webapp loads.]

Fire up sqlite3 and start running queries.  In sqlite, commands other than SQL queries are prefixed with ".", e.g. ".help".  To exit, ".q", and so on.
```
$ sqlite3 <path-to-sqlite3-database-file>
sqlite> .headers on
sqlite> .mode column
sqlite> select * from tag;
```

## How does everything start up?
To finish off this prework, look at ```bin/run-flask-webserver.sh```.  Notice how it inits the virtual environment (Digression: yet another use of 'environment'!  But this usage is actually closer to the 'environment variable' sense of the word; the 'activate' and 'deactivate' commands add and remove actual environment variables.  Test this by running the 'env' command inside and outside the virtualenv state.  Look especially closely at the values of VIRTUALENV and PATH in each case.  What are the implications of the PATH change?)

Anyway, back to startup.  The shell script calls main.py, which brings in a couple variables from ```app```, messes with the PATH so that it can find the Tag model and the views, and then inits the DB if needed and runs the app.

If you have time, also take a look at ```views.py``` and look at how routes are defined. 
- How many routes does the app have?
- What code retrieves tags from the database?  What would straight SQL look like (i.e., no ORM)?
- What code inserts tags into the view?
- Where does the image path come from?
- What code saves a tag to the database?  What would straight SQL look like (i.e., no ORM)?
- Can you think of any structural improvements that could be made to this view?

Now that's done; we can proceed with [Session 1](session-1-handout).  The git skills we'll pick up are summarized in the [Syllabus](syllabus-session-1).


## Bonus prework - explore some [Unix/Shell Concepts](unix-shell-concepts)
I'll cover these *very* briefly in class, but please, feel free to google around on your own.
