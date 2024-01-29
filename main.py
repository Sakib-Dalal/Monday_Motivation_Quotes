import datetime as dt
import smtplib
import random

MY_EMAIL = "sakibdalal73@gmail.com"
MY_PASSWORD = "dzywnwnzhutsgcge"


day = dt.datetime.now()
week = day.weekday()
print(week)

if week == 0:
    with open("quotes.txt", "r") as quotes_file:
        quote = quotes_file.readlines()
        quote = random.choice(quote)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Today's Quote\n\n{str(quote)}")
