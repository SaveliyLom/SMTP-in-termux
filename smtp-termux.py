import time
import smtplib
from colorama import init, Fore
import random

# CREATOR SAVELOM IN GITHUB

init()
png = random.randint(1,3)

if png == 1:
    print(" ⣿⣿⣿⣿⣿⣿⣿⠋⣉⡙⠛⣉⣉⠻⣿⣿⣿⣿⣿⣿\n ⣿⣿⣿⣿⣿⣿⣿⠸⣿⣿⣾⣿⡿⠀⣿⣿⣿⣿⣿⣿\n ⣿⣿⣿⣿⣿⣿⣿⣦⡘⠻⣿⠟⣡⣾⣿⣿⣿⣿⣿⣿\n ⣿⣿⣿⣿⣿⣿⠿⢿⣿⣶⣤⣼⠟⠻⢿⣿⣿⣿⣿⣿\n ⣿⣿⣿⣿⣿⢡⣶⣦⡌⠻⡿⢁⣾⣷⠀⣿⣿⣿⣿⣿\n ⣿⣿⣿⣿⣿⡄⢻⣿⣿⣦⡀⢸⣿⡏⣸⣿⣿⣿⣿⣿\n ⣿⣿⣿⣿⣿⣿⣦⠙⢿⣿⣿⣆⠙⢠⣿⣿⣿⣿⣿⣿\n ⣿⣿⣿⣿⣿⣿⣿⣷⡌⠻⣿⣿⣷⣄⠻⣿⣿⣿⣿⣿\n ⣿⣿⣿⣿⣿⣿⣿⢡⣴⣤⡘⢿⣿⣿⣧⡈⢿⣿⣿⣿\n ⣿⣿⣿⣿⡟⢋⣁⠘⢿⣿⣿⣆⠙⣿⣿⣷⡀⢻⣿⣿\n ⣿⣿⣿⠿⠀⣿⣿⣷⣄⠻⣿⣿⣿⣿⣿⣿⣷⠈⣿⣿\n ⣿⡟⢠⣶⣤⡈⠻⣿⣿⣷⣿⣿⣿⣿⣿⣿⠏⣰⣿⣿\n ⣿⣿⡈⢿⣿⣿⣶⣼⣿⣿⣿⣿⣿⣿⣿⠋⣰⣿⣿⣿\n ⣿⣿⣷⣄⠙⢿⣿⣿⣿⣿⣿⣿⡿⠟⣡⣾⣿⣿⣿⣿\n ⣿⣿⣿⣿⣷⣦⣉⠛⠛⠛⢛⣉⣴⣾⣿⣿⣿⣿⣿⣿\n \n CREATOR SAVELOM IN GITHUB\n \n \n")
elif png == 2:
    print(" ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n ⣿⣿⡿⠋⣡⣤⣤⣄⡉⠻⠟⢉⣠⣤⣤⣌⠙⢿⣿⣿\n ⣿⡟⢀⣾⣿⣿⣿⣿⣿⣄⣠⣿⣿⣿⣿⣿⣷⡄⢻⣿\n ⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿\n ⣿⣧⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣼⣿\n ⣿⣿⣧⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢁⣼⣿⣿\n ⣿⣿⣿⣿⣦⡈⠻⣿⣿⣿⣿⣿⣿⠟⢁⣴⣿⣿⣿⣿\n ⣿⣿⣿⣿⣿⣿⣦⡈⠻⣿⣿⠟⢁⣴⣿⣿⣿⣿⣿⣿\n ⣿⣿⣿⣿⣿⣿⣿⣿⣆⠈⠁⣰⣿⣿⣿⣿⣿⣿⣿⣿\n ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿\n \n CREATOR SAVELOM IN GITHUB\n \n \n")    
elif png == 3:
    print(" ⠀⠀⠀⠀⣠⠞⠉⢉⠩⢍⡙⠛⠋⣉⠉⠍⢉⣉⣉⣉⠩⢉⠉⠛⠲⣄⠀⠀⠀⠀\n ⠀⠀⠀⡴⠁⠀⠂⡠⠑⠀⠀⠀⠂⠀⠀⠀⠀⠠⠀⠀⠐⠁⢊⠀⠄⠈⢦⠀⠀⠀\n ⠀⣠⡾⠁⠀⠀⠄⣴⡪⠽⣿⡓⢦⠀⠀⡀⠀⣠⢖⣻⣿⣒⣦⠀⡀⢀⣈⢦⡀⠀\n ⣰⠑⢰⠋⢩⡙⠒⠦⠖⠋⠀⠈⠁⠀⠀⠀⠀⠈⠉⠀⠘⠦⠤⠴⠒⡟⠲⡌⠛⣆\n ⢹⡰⡸⠈⢻⣈⠓⡦⢤⣀⡀⢾⠩⠤⠀⠀⠤⠌⡳⠐⣒⣠⣤⠖⢋⡟⠒⡏⡄⡟\n ⠀⠙⢆⠀⠀⠻⡙⡿⢦⣄⣹⠙⠒⢲⠦⠴⡖⠒⠚⣏⣁⣤⣾⢚⡝⠁⠀⣨⠞⠀\n ⠀⠀⠈⢧⠀⠀⠙⢧⡀⠈⡟⠛⠷⡾⣶⣾⣷⠾⠛⢻⠉⢀⡽⠋⠀⠀⣰⠃⠀⠀\n ⠀⠀⠀⠀⠑⢤⡠⢂⠌⡛⠦⠤⣄⣇⣀⣀⣸⣀⡤⠼⠚⡉⢄⠠⣠⠞⠁⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠉⠓⠮⣔⡁⠦⠀⣤⠤⠤⣤⠄⠰⠌⣂⡬⠖⠋⠀⠀⠀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠤⢤⣀⣀⡤⠴⠒\n \n CREATOR SAVELOM IN GITHUB\n \n \n")
    
time.sleep(1)
print("\n ░██████╗███╗░░░███╗████████╗██████╗░\n ██╔════╝████╗░████║╚══██╔══╝██╔══██╗\n ╚█████╗░██╔████╔██║░░░██║░░░██████╔╝\n ░╚═══██╗██║╚██╔╝██║░░░██║░░░██╔═══╝░\n ██████╔╝██║░╚═╝░██║░░░██║░░░██║░░░░░\n ╚═════╝░╚═╝░░░░░╚═╝░░░╚═╝░░░╚═╝░░░░░\n \n \n")
print(" \n ")
print("\n ╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮\n ┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃\n ┃╰━┳╮╱╭╮╭━━┳━━┳╮╭┳━━┫┃╭━━┳╮╭╮\n ┃╭╮┃┃╱┃┃┃━━┫╭╮┃╰╯┃┃━┫┃┃╭╮┃╰╯┃\n ┃╰╯┃╰━╯┃┣━━┃╭╮┣╮╭┫┃━┫╰┫╰╯┃┃┃┃\n ╰━━┻━╮╭╯╰━━┻╯╰╯╰╯╰━━┻━┻━━┻┻┻╯\n ╱╱╱╭━╯┃\n ╱╱╱╰━━╯\n ")
print(Fore.RESET + "\n Write the username and password for the email that will send messages (I advise you to use non-primary mail for security purposes)")
try:
    login_mail = str(input("\n Login: "))
    password_mail = str(input("\n Password: "))
except:
    print(Fore.LIGHTRED_EX + "\n \n Error")
print("\n Ok, next..")
time.sleep(0.3)
print("\n List of supported mail addresses:\n ")
print(Fore.LIGHTYELLOW_EX + " mail.ru\n  mail.com\n   gmail.com\n    yandex.com\n     yandex.ru\n      outlook.com\n       aol.com")  
server = str(input(Fore.RESET + "Write your: "))
text_mail = str(input("Text to send: "))

if server == 'mail.ru':
    server_mail = "smtp.mail.ru"
elif server == "mail.com":
    server_mail = "smtp.mail.com"
elif server == "gmail.com":
    server_mail = "smtp.gmail.com"
elif server == "yandex.com":
    server_mail = "smtp.yandex.com"
elif server == "yandex.ru":
    server_mail = "smtp.yandex.ru"    
elif server == "outlook.com":
    server_mail = "smtp.outlook.com"    
elif server == "aol.com":
    server_mail = "smtp.aol.com"
        
# AUTHOR SAVELOM IN GITHUB

print("Write these emails..")
a = str(input("(ex.:smtptool@gmail.com,example@mail.com,etc): "))
print("The server and port connecting...")
smtpObj = smtplib.SMTP(server_mail, 587)
print(Fore.LIGHTGREEN_EX + "The server and port connected")
time.sleep(0.5)
print(Fore.RESET + "Starting TLS")
smtpObj.starttls()
time.sleep(0.5)
print(Fore.LIGHTGREEN_EX + "TLS started")
time.sleep(0.3)
try:
    print(Fore.RESET + "Loginning..")
    smtpObj.login(login_mail,password_mail)
    time.sleep(0.5)
    print(Fore.LIGHTGREEN_EX + "Loginned")
except:
    print(Fore.LIGHTRED_EX + "It looks like you entered the wrong username or password")    
time.sleep(2)
try:
    print(Fore.RESET + "Send message..")
    smtpObj.sendmail(login_mail,a,text_mail)
    time.sleep(0.2)
    print(Fore.LIGHTGREEN_EX + "Message sended")
except:
    print(Fore.LIGHTRED_EX + "Failed to send messages. There may be an error in incorrectly entered emails")    
print(Fore.LIGHTGREEN_EX + "Quit...")
time.sleep(5)

# AUTHOR SAVELOM IN GITHUB


smtpObj.quit()
