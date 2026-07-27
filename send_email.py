import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "srinidhi.22ad057@sode-edu.in"
    password = "ptmv ljea ztzy pkxz"

    receiver = "srinidhi.22ad057@sode-edu.in"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

    