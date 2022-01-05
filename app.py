from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = '123'

from assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

users = {'user1': {'name': 'Sapir', 'email': 'sapir@gmail.com'}, 'user2': {'name': 'Liel', 'email': 'liel@gmail.com'},
         'user3': {'name': 'Eliran', 'email': 'eliran@gmail.com'}, 'user4': {'name': 'Eden', 'email': 'eden@gmail.com'},
         'user5': {'name': 'Nati', 'email': 'nati@gmail.com'}}

@app.route('/')
def show_cv_template():  # put application's code here
    return render_template('cv.html')

@app.route('/assignment8')
def call_hobbies_template():
    #DB
    user = True
    if user:
        return render_template('assignment8.html', fullName={'firstN': 'sapir', 'lastN': 'lulvi'}, HobbiesList=('music', 'surfing', 'family trips', 'design', 'reading'))
    else:
        return redirect(url_for('show_cv_template'))


@app.route('/assignment9', methods=['GET', 'POST'])
def forms_template():
    if request.method == 'POST':
        if 'Button1' in request.form:
            session['nickN'] = ''
        if 'nickName' in request.form:
            nickname = request.form['nickName']
            session['nickN'] = nickname
            return redirect('/assignment9')
        return render_template('assignment9.html')

    if request.method == 'GET':
        if 'user' in request.args:
            username = request.args['user'].title()
            if username != "":
                for i in users:
                        if username in users[i].values():
                            return render_template('assignment9.html', listR1=users[i])
                        else:
                            return render_template('assignment9.html', strError="user name not found, please try again")
            else:
                return render_template('assignment9.html', listR2=users)
        else:
            return render_template('assignment9.html')


if __name__ == '__main__':
    app.run()
