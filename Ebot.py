import smtplib
Server=smtplib.SMTP('smtp.gmail.com',587)
Server.starttls()
Server.login('mailid','password')
Server.sendmail('visweshkannan2000@gmail','mec.it.visweshkannan@gmail.com','Hello today is the last date for submitting NPTEL assignment-2')
