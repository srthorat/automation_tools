#!/usr/bin/env python3
"""
Description: Send mail Library
Author : Sakharam Thorat
Date   : 06/06/2018
Email  : srt.2011@outlook.com

"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os


class SendEmailUtility(object):

    def __init__(self, from_user, from_password, email_server, to):
        self.email_server = email_server
        self.from_user = from_user
        self.from_password = from_password
        self.to = to

    def send(self,report_file):
        msg = MIMEMultipart()

        msg['From'] = self.from_user
        msg['To'] = self.to
        msg['Subject'] = "Automation test report"

        msg.attach(MIMEText("Please find the Attachment for report"))
        dir = os.getcwd()
        part = MIMEBase('application', 'octet-stream')
        with open(dir+"\\"+ report_file, 'rb') as f:
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="%s"' % os.path.basename(dir+"\\"+report_file))
        msg.attach(part)

        mailServer = smtplib.SMTP(self.email_server, 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(self.from_user, self.from_password)
        mailServer.sendmail(self.from_user, self.to, msg.as_string())
        mailServer.close()

