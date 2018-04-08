##Imports:
import smtplib
import time
import imaplib
from email.message import Message
import json
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import nltk


def Send_completion_email(From_email, To_email, server, Password):
    '''
    Sends an email that lets the user know that the code has finished running
    '''
    smtpObj = smtplib.SMTP(server, 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(From_email, Password)
    smtpObj.sendmail(From_email, To_email,'Hello, Your Code Has finished running!')
    return True

def Send_update_email(From_email, To_email, server, Password,val_text):
    '''
    Sends an email that lets the user know that the code has finished running
    '''
    smtpObj = smtplib.SMTP(server, 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(From_email, Password)
    smtpObj.sendmail(From_email, To_email,val_text)
    return True
