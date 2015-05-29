#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import csv
import codecs
import json
import sys
import random

from scrape import scrape_subreddit

reload(sys)
sys.setdefaultencoding('utf-8')

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#


@app.route('/')
def home():
    # data = []
    # comments = scrape_subreddit()
    # for comment in comments:
    #     comment.body = (comment.body[:199] + '...') if len(comment.body) > 199 else comment.body 
    #     data.append(str(comment.body).encode('utf-8').strip() + " | " + str(comment.date) + " | " + 
    #         str(comment.author) + " | " + str(comment.karma))
    csv_files = ['askreddit.csv', 'ssbm.csv', 'news.csv', '4chan.csv', 'fitness.csv']
    data_compressed = []

    for csv_file in csv_files:
        try:
            data = [row for row in csv.reader(codecs.open(csv_file, 'U', encoding='utf-8', errors = 'replace'))]
        except ValueError:
            print "Fucking reddit amiright?"
        for _ in range(5):
            line = random.choice(data)
            temp_line = []
            for attribute in line:
                attribute = (attribute[:199] + '...') if len(attribute) > 199 else attribute
                temp_line.append(attribute)
            line = ' | '.join(temp_line)
            data_compressed.append(line)

    return render_template('pages/placeholder.home.html', context = data_compressed)


@app.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@app.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)


@app.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@app.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)

# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
