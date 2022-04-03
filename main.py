# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys; print(sys.executable)
import smtplib

address = 'elisystembot@gmail.com'
password = 'unsecurepassword'

def send_mail():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(address, password)

        subject = 'Test Mail'
        body = ':) This message was sent from my new python script.'

        msg = f'Subject: {subject}\n\n{body}'

        #smtp.sendmail(address, 'benjamindnelson1@gmail.com', msg)
        #smtp.sendmail(address, 'whitleymn12@gmail.com', msg)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    send_mail()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
