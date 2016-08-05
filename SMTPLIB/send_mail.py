import smtplib

FROM     = "your email address"
PASSWORD = "your password"
TO       = "receiver's email address"
BODY     = "your content"

mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()

try:
    mail.login(FROM,PASSWORD)
except:
    print "Wrong Login Credentials"
    exit()
try:
    mail.sendmail(str(i)+FROM,TO,BODY)
    print i+1,":","MESSAGE SENT"
except:
    print "Oops! Message not sent"
mail.close()
