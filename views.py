from flask import request, redirect, render_template, g
from datetime import datetime
from app import app
from tag import Tag

@app.route('/', methods=['GET'])
def show_tags():
    g.setdefault('image', app.config['config']['awesome_image']) # Flask.g: a way to pass var to a template
    return render_template('index.html', tags=Tag.select())

@app.route('/tags', methods=['POST'])
def add_tag():
    Tag.get_or_create(
      name=request.form['tag-name'],
      defaults={'created_at': datetime.now(), 'updated_at': datetime.now()})

    return redirect('/')
