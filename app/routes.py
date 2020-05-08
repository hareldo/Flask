from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm, CodeForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/code', methods=['GET', 'POST'])
def run_code():
    form = CodeForm()
    if form.validate_on_submit():
        flash('Run Code {}, result={}'.format(
            form.code.data, 0))
        exec(form.code.data)
        return redirect('/index')
    return render_template('code.html', title='IDE', form=form)