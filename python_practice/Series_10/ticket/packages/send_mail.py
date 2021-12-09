import smtplib

class mail:
    def __init__(self, username, email, massage):
        self.username = username
        self.email = email
        self.massage = massage

    def send(self):
        try :
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login("testpythontest1379@gmail.com", "ali1379ali")
            message = f'subject: {"Authentication"}\n\n{f"hi dear {self.username} - {self.massage}"}'
            server.sendmail("testpythontest1379@gmail.com", self.email, message)
            server.quit()
            print("Success: Email send!")
        except:
            print("Email failed to send.")
