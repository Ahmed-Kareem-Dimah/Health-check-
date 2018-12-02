from netmiko import ConnectHandler
from tkinter import *
from tkinter import messagebox
import re
from tkinter.ttk import *
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


window = Tk()

window.title("DIMAH #3 - Check Routers")
window.geometry('800x500')

sysip = Label(window, text="Enter the system IP: ")
sysip.grid(row=1)
sysiptxt = Entry(window, width=20)
sysiptxt.grid(row=1, column=2)

lbl1 = Label(window, text='1st')
lbl1.grid(row=4)

lbl2 = Label(window, text='2nd')
lbl2.grid(row=5)

def dev7750(self):
    power1 = connect.send_command('show chassis detail | match "Power supply number               : 1" post-lines 3')
    power_1 = re.search(r"(.+Status) +(:) +(.+)", power1, re.I).group(3)

    while True:
        if power_1 == 'up':
            print("first (" + self + ") power is up ")
            break

        else:
            if power_1 == "critical failure":
                print("first (" + self + ") power is down")
                send_email(devicename)
                break
            else:
                print("It may not equipped or Strange error")
                break

    power1 = connect.send_command('show chassis detail | match "Power supply number               : 2" post-lines 3')
    power_2 = re.search(r"(.+Status) +(:) +(.+)", power1, re.I).group(3)
    while True:
        if power_2 == 'up':
            print("second (" + self + ") power is up")
            break
        else:
            if power_2 == "critical failure":
                print("second (" + self + ") power is down")
                send_email(devicename)
                break
            else:
                print("It may not equipped or Strange error")
                break

def dev7705sr8v2(self):
    power1 = connect.send_command('show chassis power-feed')
    power_1 = re.search(r"(.+Input power feed+) +(: A+\n) + (.+Type) +(.+.+\n) +(.+Status) +(:) +(.+.)", power1, re.I).group(7)

    while True:
        if power_1 == 'up':
            print("first (" + self + ") power is up ")
            break
        else:
            if power_1 == "critical failure":
                print("first (" + self + ") power is down")
                send_email(devicename)
                break
            else:
                print("It may not equipped or Strange error")
                break
    power2 = connect.send_command('show chassis power-feed')
    power_2 = re.search(r"(.+Input power feed+) +(: B+\n) + (.+Type) +(.+.+\n) +(.+Status) +(:) +(.+.)", power2, re.I).group(7)
    while True:
        if power_2 == 'up':
            print("second (" + self + ") power is up")
            break
        else:
            if power_2 == "critical failure":
                print("second (" + self + ") power is down")
                send_email(devicename)
                break
            else:
                print("It may not equipped or Strange error")
                break

def dev7705srW(self):
    power1 = connect.send_command(
        'show chassis | match "Input power feed              : A" context all')
    power_1 = re.search(r"(.+Status) +(:) +(.+.)", power1, re.I).group(3)

    while True:
        if power_1 == 'up':
            print("first (" + self + ") power is up ")
            break
        else:
            if power_1 == "critical failure":
                print("first (" + self + ") power is down")
                #send_email(devicename)
                break
            else:
                print("It may not equipped or Strange error")
                break
    power2 = connect.send_command(
        'show chassis | match "Input power feed              : B" context all')
    power_2 = re.search(r"(.+Status) +(:) +(.+.)", power2, re.I).group(3)

    while True:
        if power_2 == 'up':
            print("second (" + self + ") power is up")
            break
        else:
            if power_2 == "critical failure":
                print("second (" + self + ") power is down")
                #send_email(devicename)
                break
            else:
                print("It may not equipped or Strange error")
                break

def dev7705srAxor(self):
    power1 = connect.send_command(
        'show chassis | match "Input power feed              : A" context all')
    power_1 = re.search(r"(.+Status) +(:) +(.+.)", power1, re.I).group(3)

    while True:
        if power_1 == 'up':
            print("first (" + self + ") power is up ")
            break
        else:
            if power_1 == "critical failure":
                print("first (" + self + ") power is down")
                send_email(devicename)
                break
            else:
                print("It may not equipped or Strange error")
                break
    power2 = connect.send_command(
        'show chassis | match "Input power feed              : B" context all')
    power_2 = re.search(r"(.+Status) +(:) +(.+.)", power2, re.I).group(3)

    while True:
        if power_2 == 'up':
            print("second (" + self + ") power is up")
            break
        else:
            if power_2 == "critical failure":
                print("second (" + self + ") power is down")
                send_email(devicename)
                break
            else:
                print("It may not equipped or Strange error")
                break

def dev7210(self):
    power1 = connect.send_command('show chassis | match "Power supply number               : 1" post-lines 3')
    power_1 = re.search(r"(.+Status) +(:) +(.+.)", power1, re.I).group(3)

    while True:
        if power_1 == 'up':
            print("first (" + self + ") power is up ")
            break
        else:
            if power_1 == "critical failure":
                print("first (" + self + ") power is down")
                send_email(devicename)
                break
            else:
                print("It may not equipped or Strange error")
                break
    power2 = connect.send_command('show chassis | match "Power supply number               : 2" post-lines 3')
    power_2 = re.search(r"(.+Status) +(:) +(.+.)", power2, re.I).group(3)
    while True:
        if power_2 == 'up':
            print("second (" + self + ") power is up")
            break
        else:
            if power_2 == "critical failure":
                print("second (" + self + ") power is down")
                send_email(devicename)
                break
            else:
                print("It may not equipped or Strange error")
                break

def dev7210sasT(self):
    power1 = connect.send_command('show chassis | match "Power supply number               : 1" post-lines 3')
    power_1 = re.search(r"(.+Status) +(:) +(.+.)", power1, re.I).group(3)

    while True:
        if power_1 == 'up':
            print("first (" + self + ") power is up ")
            break
        else:
            if power_1 == "critical failure":
                print("first (" + self + ") power is down")
                send_email(devicename)
                break
            else:
                print("It may not equipped or Strange error")
                break
    power2 = connect.send_command('show chassis | match "Power supply number               : 2" post-lines 3')
    power_2 = re.search(r"(.+Status) +(:) +(.+.)", power2, re.I).group(3)
    while True:
        if power_2 == 'up':
            print("second (" + self + ") power is up")
            break
        else:
            if power_2 == "critical failure":
                print("second (" + self + ") power is down")
                send_email(devicename)
                break
            else:
                print("It may not equipped or Strange error")
                break

def devsar18(self):
    power1 = connect.send_command('show chassis | match "Input power feed              : A" context all')
    power_1 = re.search(r"(.+Status) +(:) +(.+.)", power1, re.I).group(3)
    while True:
        if power_1 == 'up':
            print("first (" + self + ") power is up ")
            break
        else:
            if power_1 == "critical failure":
                print("first (" + self + ") power is down")
                send_email(devicename)
                break
            else:
                print("It may not equipped or Strange error")
                break
    power2 = connect.send_command('show chassis | match "Input power feed              : B" context all')
    power_2 = re.search(r"(.+Status) +(:) +(.+.)", power2, re.I).group(3)
    while True:
        if power_2 == 'up':
            print("second (" + self + ") power is up")
            break
        else:
            if power_2 == "critical failure":
                print("second (" + self + ") power is down")
                send_email(devicename)
                break
            else:
                print("It may not equipped or Strange error")
                break

def devsarA_T1_E1(self):
    power1 = connect.send_command(
        'show chassis | match "Input power feed              : A" context all')
    power_1 = re.search(r"(.+Status) +(:) +(.+.)", power1, re.I).group(3)

    while True:
        if power_1 == 'up':
            print("first (" + self + ") power is up ")
            break
        else:
            if power_1 == "critical failure":
                print("first (" + self + ") power is down")
                send_email(devicename)
                break
            else:
                print("It may not equipped or Strange error")
                break
    power2 = connect.send_command(
        'show chassis | match "Input power feed              : B" context all')
    power_2 = re.search(r"(.+Status) +(:) +(.+.)", power2, re.I).group(3)

    while True:
        if power_2 == 'up':
            print("second (" + self + ") power is up")
            break
        else:
            if power_2 == "critical failure":
                print("second (" + self + ") power is down")
                send_email(devicename)
                break
            else:
                print("It may not equipped or Strange error")
                break

def check_error():
    try:
        if sysiptxt.get() == '':
            messagebox.showinfo("check", "enter sys ip first")
        else:
            nokia = {
                'device_type': 'alcatel_sros',
                'ip': sysiptxt.get(),
                'username': '******',
                'password': '******',
            }
            connect = ConnectHandler(**nokia)
            try:
                type7750 = connect.send_command('show chassis detail | match Name post-lines 13')
                typever7750 = re.search(r"(.+Type) +(:) (.+) ", type7750, re.I).group(3)
                if typever7750 == "7750":
                    fan1 = connect.send_command('show chassis detail | match "Fan tray number                   : 1" post-lines 2')
                    fancheck1 = re.search(r"(.+Status) +(:) +(.+)", fan1, re.I).group(3)
                    while True:
                        if fancheck1 == 'up':
                            lbl1.configure(text="the first Fan is UP")
                            lbl1.update()
                            break
                        else:
                            if fancheck1 == "critical failure":
                                lbl1.configure(text="the first Fan is in Critical failure")
                                break

                    fan2 = connect.send_command('show chassis detail | match "Fan tray number                   : 2" post-lines 2')
                    fancheck2 = re.search(r"(.+Status) +(:) +(.+)", fan2, re.I).group(3)
                    while True:
                        if fancheck2 == 'up':
                            lbl2.configure(text="the first Fan is UP")
                            lbl2.update()
                            break
                        else:
                            if fancheck2 == "critical failure":
                                lbl2.configure(text="the first Fan is in Critical failure")
                                break
            except:
                pass
                type7705 = connect.send_command('show chassis | match Name post-lines 13')
                typever7705 = re.search(r"(.+Type) +(:) (.+) ", type7705, re.I).group(3)
                if typever7705 == "7705":
                    fan1 = connect.send_command('show chassis | match "Input power feed              : A" context all')
                    fancheck1 = re.search(r"(.+Status) +(:) +(.+.)", fan1, re.I).group(3)
                    while True:
                        if fancheck1 == 'up':
                            lbl1.configure(text="the first Fan is UP")
                            break
                        else:
                            if fancheck1 == "critical failure":
                                lbl1.configure(text="the first Fan is in Critical failure")
                                break
                    fan2 = connect.send_command('show chassis | match "Input power feed              : B" context all')
                    fancheck2 = re.search(r"(.+Status) +(:) +(.+.)", fan2, re.I).group(3)
                    while True:
                        if fancheck2 == 'up':
                            lbl2.configure(text="the first Fan is UP")
                            break
                        else:
                            if fancheck2 == "critical failure":
                                lbl2.configure(text="the first Fan is in Critical failure")
                                break

    except:
        print("Error in the code")

def send_email(self):
    try:
        email_user = 'ahmed.k.dema@gmail.com'
        email_password = '**********'
        email_send = 'ahmed.kareem@gmail.com'
        cc = 'ahmed.kareem@gmail.com'
        send = [email_send, cc]
        subjectt = "Hardware Error"
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['CC'] = cc
        msg['Subject'] = subjectt
        body = ("Dear  Team, \n"
                "there is an power feed issue in site :" + self +
                "\n" +
                "\n"
                "Note: this is an automatic email, DONT reply to it!.")
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, send, text)
        server.quit()
        print("message send")
    except:
        messagebox.showinfo("Error", "emails not working")

def check_list():
    ips_file = open('ip_lists', 'r')        ## open a file from root
    ips_file.seek(0)            ## put the first read on the begining
    iplist = ips_file.read().splitlines()       ## splite the ip's in a list
    ips_file.close()
    while True:

        check = False
        for ip in iplist:
            while True:
                a = ip.split('.')
                if (len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (
                        int(a[0]) != 169 or int(a[1]) != 254) and (
                        0 <= int(a[1]) <= 255 and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255):
                    print('\n')
                    print("IP's formula is good :%s" %ip)
                    check = True
                    nokia = {
                        'device_type': 'alcatel_sros',
                        'ip': ip,
                        'username': '*******',
                        'password': '********',
                    }
                    try:
                        global connect
                        connect = ConnectHandler(**nokia)
                    except:
                        print("this ip is wrong %s" % ip)
                        break
                    try:
                        try:
                            global devicename
                            device = connect.send_command('show system information | match "System Name"')
                            devicename = re.search(r"(.+System)? +(:) (.+)", device, re.I).group(3)
                            type7750 = connect.send_command('show chassis detail | match Name post-lines 13')
                            typever7750 = re.search(r"(.+Type) +(:) (.+) ", type7750, re.I).group(3)
                            if typever7750 == "7750":
                                dev7750(devicename)

                        except:
                            type7705 = connect.send_command('show chassis')
                            typever7705 = re.search(r"(.+Type) +(:) (.+)?", type7705, re.I).group(3)
                            if typever7705 == "7705 SAR-8 v2":
                               dev7705sr8v2(devicename)
                            elif typever7705 == "7705 SAR-W":
                                dev7705srW(devicename)
                            elif typever7705 == "7705 SAR-A (Eth XOR)":
                                dev7705srAxor(devicename)
                            elif typever7705 == "7210 SAS-M 24F 2XFP-1":
                                dev7210(devicename)
                            elif typever7705 == "7705 SAR-18":
                                devsar18(devicename)
                            elif typever7705 == "7705 SAR-A (Eth XOR with T1/E1)":
                                devsarA_T1_E1(devicename)
                            elif typever7705 == "7210 SAS-T 12F10T 4XFP-1":
                                dev7210sasT(devicename)

                    except:
                        print("Call ahmed Kareem dimah")

                    connect.disconnect()
                    break

                else:
                    b = "the wrong ip is %s" % ip
                    print(b)
                    check = False
                    break

        if check == False:
            messagebox.showinfo("report", "there is ip not reachable")
        elif check == True:
            lbl2.configure(text="first cycle done")
            print('\n')
            print('All routers has been check and finished !!!')
            print('\n')
            print('Another round will START now : ')
            quit()



check = Button(window, text="Check", command=check_error)
check.grid(row=2)

checkall = Button(window, text="Check-list", command=check_list)
checkall.grid(row=3)
window.mainloop()