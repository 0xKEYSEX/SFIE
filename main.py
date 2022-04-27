import smtplib, datetime
import time

from faker import Faker
import string, random
from email.mime.text import MIMEText
import random

# Created by KEYSEX#4176

def sendEmailFullInfo():
    sender = "SENDER EMAIL"
    receivers = ["RECEIVER EMAIL"]

    faker = Faker('fr_FR')
    phone = ''.join(random.choices(string.digits, k = 8))
    fakeCard = ''.join(random.choices(string.digits + string.digits, k = 16))
    fakeCCV = ''.join(random.choices(string.digits, k = 3))
    randomDays = random.randint(1, 12)

    dateChoice = random.randint(2, 5)
    now = datetime.datetime.now()
    today = now.strftime("%Y")
    finalDate = today[0:3]
    fakeExpiration = finalDate + str(dateChoice)

    with open ("email.txt", "r") as file:
        allText = file.read()
        mail = list(map(str, allText.split()))

    with open ("password.txt", "r") as file:
        allText = file.read()
        password = list(map(str, allText.split()))

        userAgents = [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.7.12 (KHTML, like Gecko) Version/7.1.7 Safari/537.85.16",
            "Mozilla/5.0 (Windows NT 6.0; rv:40.0) Gecko/20100101 Firefox/40.0",
            "Mozilla/5.0 (iPad; CPU OS 8_1_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B466 Safari/600.1.4",
            "Mozilla/5.0 (Linux; U; Android 4.0.3; en-us; KFTT Build/IML74K) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
            "Mozilla/5.0 (iPad; CPU OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Version/7.0 Mobile/11D201 Safari/9537.53",
            "Mozilla/5.0 (Linux; U; Android 4.4.3; en-us; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/3.68 like Chrome/39.0.2171.93 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko",
            "Mozilla/5.0 (iPad; CPU OS 8_4_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) GSA/8.0.57838 Mobile/12H321 Safari/600.1.4",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36"]

    numberChoice = random.randint(1, 2)

    if numberChoice == 1:
        body_of_email = """
        <html>
          <body>
            <p>🐱‍👤Information🐱‍👤: <br></p>
            <p>     💎 Nom: %s</p>
            <p>     💎 Date de naissance: %s</p>
            <p>     💎 Address: %s</p>
            <p>     💎 Numéro de téléphone: %s</p>
            <p>     💎 Email: %s</p>
            <p>     💎 Password: %s</p>
            <p> </p>
            <p>💲Information CC💲: </p>
            <p>     💳 Numéro de carte: %s</p>
            <p>     💳 CCV: %s</p>
            <p>     💳 Date d'expiration: %s%s%s</p>
            <p>     </p>
            <p>     💡 IP: %s</p>
            <p>     💡 User-Agent: %s</p>
            <p>     </p>
          </body>
        </html>
        """ %(faker.name(), faker.date_of_birth(), faker.address(), str("06")+phone, random.choices(mail), random.choices(password),fakeCard, fakeCCV, randomDays, "/", fakeExpiration, faker.ipv4() , random.choice(userAgents) )

    elif numberChoice == 2:
        body_of_email = """
        <html>
          <body>
            <p>🐱‍👤Information🐱‍👤: <br></p>
            <p>    💎 Nom: %s</p>
            <p>    💎 Date de naissance: %s</p>
            <p>    💎 Address: %s</p>
            <p>    💎 Numéro de téléphone: %s</p>
            <p>    💎 Email: %s</p>
            <p>    💎 Password: %s</p>
            <p> </p>
            <p>💲Information CC💲: </p>
            <p>     💳 Numéro de carte: %s</p>
            <p>     💳 CCV: %s</p>
            <p>     💳 Date d'expiration: %s%s%s</p>
            <p>     </p>
            <p>     💡 IP: %s</p>
            <p>     💡 User-Agent: %s</p>
            <p>     </p>
          </body>
        </html>
        """ %(faker.name(), faker.date_of_birth(), faker.address(), str("06")+phone, random.choices(mail), random.choices(password),fakeCard, fakeCCV, randomDays, "/", fakeExpiration, faker.ipv4() , random.choice(userAgents) )

    print(body_of_email)

    msg = MIMEText(body_of_email, 'html')
    msg['Subject'] = 'NEW FULL-INFO'
    msg['From'] = sender
    msg['To'] = ','.join(receivers)

    smtp = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
    smtp.login(user = 'SENDER EMAIL', password = 'SENDER PASSWORD')
    smtp.sendmail(sender, receivers, msg.as_string())
    smtp.quit()
    print("Email envoyé avec succès  [FULL INFO]!")

sendEmailFullInfo()

def sendEmailCCInfo():
    sender = "SENDER EMAIL"
    receivers = ["RECEIVERS EMAIL"]

    faker = Faker('fr_FR')
    fakeCard = ''.join(random.choices(string.digits + string.digits, k = 16))
    fakeCCV = ''.join(random.choices(string.digits, k = 3))
    randomDays = random.randint(1, 12)

    dateChoice = random.randint(2, 5)
    now = datetime.datetime.now()
    today = now.strftime("%Y")
    finalDate = today[0:3]
    fakeExpiration = finalDate + str(dateChoice)


    body_of_email = """
    <html>
      <body>
        <p>💲Information CC💲: <br></p>
            <p>    💳 Numéro de carte: %s</p>
            <p>    💳 CCV: %s</p>
            <p>    💳 Date d'expiration: %s%s%s</p>
      </body>
    </html>
    """%(fakeCard, fakeCCV, randomDays, "/", fakeExpiration)

    msg = MIMEText(body_of_email, 'html')
    msg['Subject'] = '🐱‍👤 NEW INFO-CC 🐱‍👤'
    msg['From'] = sender
    msg['To'] = ','.join(receivers)

    smtp = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
    smtp.login(user = 'SENDER EMAIL', password = 'SENDER PASSWORD')
    smtp.sendmail(sender, receivers, msg.as_string())
    smtp.quit()

    print("Email envoyé avec succès [INFO CC]!")

def sendFakePaypal():
    sender = "SENDER EMAIL"
    receivers = ["RECEIVERS EMAIL"]

    with open ("email.txt", "r") as file:
        allText = file.read()
        mail = list(map(str, allText.split()))

    with open ("password.txt", "r") as file:
        allText = file.read()
        password = list(map(str, allText.split()))

    body_of_email = """
    <html>
      <body>
        <p>💲Information Paypal💲: <br></p>
            <p>    ✨ Email: %s</p>
            <p>    ✨ Password: %s</p>
      </body>
    </html>
    """%(random.choice(mail), random.choice(password))

    msg = MIMEText(body_of_email, 'html')
    msg['Subject'] = '🐱‍👤 NEW INFO-PayPal 🐱‍👤'
    msg['From'] = sender
    msg['To'] = ','.join(receivers)

    smtp = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
    smtp.login(user = 'SENDER EMAIL', password = 'SENDER PASSWORD')
    smtp.sendmail(sender, receivers, msg.as_string())
    smtp.quit()

    print("Email envoyé avec succès [INFO PayPal]!")

def start():
    randomTimer = random.randint(600, 1200)

    sendFakePaypal()
    time.sleep(randomTimer)
    sendEmailFullInfo()
    time.sleep(randomTimer)
    sendEmailCCInfo()
    time.sleep(randomTimer)

    return start()

if __name__ == "__main__":
    print("Execution start(): (Created by KEYSEX#4176)")
    start()

# Created by KEYSEX#4176
