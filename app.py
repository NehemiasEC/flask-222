from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask:flask@localhost/flaskmovie'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(80),unique = True)
    email = db.Column(db.String(120), unique = True)

    def __init__(self,username,email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r'%self.username


@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['username'],request.form['email'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/")
def home():
    return render_template('add_user.html')

if __name__== "__main__":
    app.run()
