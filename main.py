import smtplib

# session = smtplib.SMTP(host='smtp.gmail.com', port=587)
# session.starttls()
# session.login(user="info.remotesquad@gmail.com", password='use tyay yjrz wogs')
# session.sendmail(from_addr="jordan.jakisa@gmail.com", to_addrs="jordan.jakisa@gmail.com", msg="Hello, this is a test email to test my sample email client")
# session.quit()

with smtplib.SMTP(host='smtp.gmail.com', port=587) as session:
    session.set_debuglevel(1)   
    session.starttls()
    session.login(user="jordan.jakisa@gmail.com", password='rkwa xmmf qwuq tdyi')
    session.sendmail(from_addr="jordan.jakisa@gmail.com", to_addrs="jordan.jakisa@gmail.com", msg="Hello, this is a test email to test my sample email client")

    