import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
    from_add='astromaniago@gmail.com'
    to_add="sohamsen2542000@gmail.com"
    subject="Finance Stock Report"

    msg=MIMEMultipart()
    msg['From']=from_add
    msg['To']=to_add
    msg['Subject']=subject

    # body='Hey there! Sending message through Python!'
    # msg.attach(MIMEText(body,'plain'))        #2nd argument if body is xml html file or plain
    body="<b>Today's Finance Report Attached</b>"
    msg.attach(MIMEText(body,'html')) 

    my_file=open(filename,'rb')

    part=MIMEBase('application','octet-scream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachment; filename= ' + filename)
    msg.attach(part)

    message=msg.as_string()
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(from_add,'qmjwkbecpztpthii')



    server.sendmail(from_add,to_add,message)   #first arg=from second =to

    server.quit()