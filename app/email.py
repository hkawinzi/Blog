from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,template,to,**kwargs)
    sender_firstname = 'happiness'

    email = Message(subject, sender=sender_firstname, recipients=[to])
    email.body = render_template(template + ".txt",**kwagrs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)