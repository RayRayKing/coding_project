##################### Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib

# 1. Update the birthdays.csv with your friends & family's details.
# HINT: Make sure one of the entries matches today's date for testing purposes.
today = dt.datetime.now()
month = today.month
day = today.day
today_tuple = (today.month, today.day)

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
bday_data = pd.read_csv("birthdays.csv")

bday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in bday_data.iterrows()}

# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
if today_tuple in bday_dict.keys():
    letter = random.choice(["letter_1.txt", "letter_2.txt", "letter_3.txt"])
    my_msg = open(f"letter_templates\{letter}").read()
    bday_owner = bday_dict[today_tuple]["name"]
    print(bday_owner)

    full_msg = my_msg.replace("[NAME]", bday_owner)
    print(full_msg)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp


# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
email = "somehting@gmail"
pw = "somethingpw"

connection = smtplib.SMTP()

connection.connect("smtp.gmail.com")
connection.login(email, pw)
connection.starttls()
connection.sendmail(from_addr=email,to_addrs=email,msg=full_msg)
connection.close
