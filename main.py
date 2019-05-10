# main.py

from app import app
from db_setup import init_db, db_session
from forms import Mode
from flask import flash, render_template, request, redirect, session, abort
from models import Point, 
from tables import Results
from flask import Markup
import os 

init_db()

# Creating the main part of the website
# Links we used to gain a better understanding for this task -> 
# https://www.blog.pythonlibrary.org/2017/12/14/flask-101-adding-editing-and-displaying-data/
# Utilized this tutorial to adapt it our website idea
# Connects to index.html and login.html 


@app.route('/login')
def home():
    if session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Testing"

@app.route('/login', methods=['POST', 'GET'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'username': 
        session['logged_in'] = True
        #return redirect_dest(fallback=url_for('index.html'))
        search = Mode(request.form)
        return render_template('index.html', form=search) 
    else:
        return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


@app.route('/', methods=['GET', 'POST'])
def index():
    search = Mode(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form=search)
  
 #trying to implement another page where users will be able to select 
 #a different mode - FanDuel mode 
 #where they will be base it off of salary 
# @app.route('/fanduel', methods=['GET', 'POST'])
# def fanduel():
#     form = new(request.form)
#     if request.method == 'POST' and form.validate():
#         point = Point()
#         save_changes(point, form, new=True)
#         return redirect('/')
#     return render_template('fanduel.html', form=form)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
 
    if search_string:
        if search.data['select'] == 'Points':
            qry = db_session.query(Point, ).filter(
                .id==Point._id).filter(
                    .name.contains(search_string))
            results = [item[0] for item in qry.all()]
        elif search.data['select'] == 'Points':
            qry = db_session.query(Point).filter(
                Point.title.contains(search_string))
            results = qry.all()
        else:
            qry = db_session.query(Point)
            results = qry.all()
    else:
        qry = db_session.query(Point)
        results = qry.all()
 
    if not results:
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)


if __name__ == '__main__':
    app.run(debug=True)

















