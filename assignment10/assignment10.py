from flask import Blueprint, render_template, request, redirect
from interact_with_DB import interact_db

assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/assignment10', template_folder='templates')

@assignment10.route('/assignment10')
def display_users():
    query = 'select * from users;'
    users_list = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=users_list)


@assignment10.route('/insert_user', methods=["post"])
def insert_user():
    name = request.form['name']
    email = request.form['email']
    query = "INSERT INTO users(name,email) VALUES ('%s', '%s' );" %(name, email)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')

@assignment10.route('/delete_user', methods=["post"])
def delete_user():
    user_id = request.form['user_id']
    query = "DELETE FROM users WHERE id='%s';" % user_id
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')

@assignment10.route('/update_email', methods=["post"])
def update_email():
    name = request.form['name']
    newEmail = request.form['email']
    query = "UPDATE users SET email='%s' WHERE name='%s';" % (newEmail,name)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')

@assignment10.route('/update_name', methods=["post"])
def update_name():
    Newname = request.form['name']
    email = request.form['email']
    query = "UPDATE users SET name='%s' WHERE email='%s';" % (Newname,email)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')