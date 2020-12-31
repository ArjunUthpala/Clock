from tkinter import *
from tkinter.ttk import *
import datetime

window = Tk()
window.title("New Year Countdown")
window.geometry('725x475')
window.configure(background='black')

title_label = Label(window, font = 'Helvetica 25 bold', foreground = 'white', background='black')
title_label.pack(anchor='center')
title_label.config(text = ''+'\n'+'New Year Countdown'+'\n'+'')

time_label = Label(window, font = 'Helvetica 50 bold', foreground = 'white', background='black')
time_label.pack(anchor='center')

date_label = Label(window, font = 'Helvetica 50 bold', foreground = 'white', background='black')
date_label.pack(anchor='s')

wish_label = Label(window, font = 'Helvetica 20 bold', foreground = 'white', background='black')
wish_label.pack(anchor='center')


def clock():
        date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
        date,time1 = date_time.split()
        time2,time3 = time1.split('/')
        hour,minutes,seconds =  time2.split(':')
        if int(hour) > 12 and int(hour) < 24:
                time = str(int(hour) - 12) + ':' + minutes + ':' + seconds + ' ' + time3
        else:
                time = time2 + ' ' + time3
        time_label.config(text = time)
        date_label.config(text = date)
        time_label.after(1000, clock)
        if date == '01-01-2021' and time == '00:00:01 AM':
            wish_label.config(text = ''+'\n'+'Happy New Year!' +'\n'+ 'May 2021 brings you all happiness & prosperity!!'+'\n'+ '- Best Regards from Arjun Waththegedara')

clock()
window.mainloop()

#Arjun_Waththegedara
