import smtplib
import random
import datetime as dt
import json

# Send email
def send_email():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=login_data["from_email"], password=login_data["from_password"])
        connection.sendmail(from_addr=login_data["from_email"], to_addrs=login_data["to_email"], msg=f"Subject:Weekday Motivation\n\n{random_quote}")

# Checking for email/password file:
try:
    with open ("secret.json", mode='r') as data:
        login_data = json.load(data)
except:
    print("secret.json with login details is missing.")
else:
    # Find today's day
    now = dt.datetime.now()
    day_of_the_week = now.strftime("%A")
    if day_of_the_week == 'Monday':
        # Creating a list of quotes and randomly selecting a quote
        with open ("quotes.txt", mode='r') as data:
            quotes_data = data.readlines()
            random_quote = random.choice(quotes_data)
        # Calling send email to send the email
        send_email()




