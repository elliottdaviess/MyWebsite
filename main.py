import os
from flask import Flask, redirect, request, render_template, make_response, url_for
from flask_mail import Mail, Message
import sqlite3

app = Flask(__name__)

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USE_TLS=False,
	MAIL_USERNAME = '',
	MAIL_PASSWORD = ''
	)

mail = Mail(app)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route("/", methods = ['GET','POST'])
def SendMail():
    if request.method=='GET':
        return render_template('index.html', msg = '')
    elif request.method=='POST':
        name = request.form.get('name', default = "Name Server Error")
        email = request.form.get('email', default = "Email Server Error")
        mobile = request.form.get('mobile', default = "Mobile Server Error")
        subject = request.form.get('subject', default = "Subject Server Error")
        message = request.form.get('message', default = "Message Server Error")

        subjectmsg = name + " - " + subject

        bodymsg = "Name: " + name + "\n\n" "Email: " + email + "\n\n" + "Mobile: " + mobile + "\n\n" + "Message: "+ message

        try:
            msg = Message(subjectmsg,
                sender="elliott.davies10@gmail.com",
                recipients=["elliott_davies@live.co.uk"])
            msg.body = bodymsg
            mail.send(msg)
            resp = make_response(render_template('index.html', msg='Thank you for getting in touch'))
            return resp
        except Exception as e:
            return(str(e))

@app.route("/References")
def home():
   return render_template('References.html', msg = '')

if __name__ == "__main__":
   app.run()
