from tkinter import *
from tkinter import ttk

from setuptools import Command

news_paper = Tk()

news_paper.geometry("500x300")
news_paper.minsize(250,150)

def logos():
    print("hello logo")
def logo():
    print("hello logo6666666666")

f0 = Frame(news_paper,bg = "purple", borderwidth=3,relief=SUNKEN)
f0.pack(anchor = "nw",side =LEFT,fill= "y")
f00 = Frame(news_paper,bg = "purple", borderwidth=3,relief=SUNKEN)
f00.pack(anchor = "ne",side =TOP,fill="x")

f11 = Frame(news_paper,bg = "red", borderwidth=3,relief=SUNKEN)
f11.pack(anchor = "n",fill="x",padx = 5,pady = 5)

label = PhotoImage(file = "D:\\vscode\\.vscode\\python\\final_project\\15844506446241.png")
logo = Button(f0,image = label, command = logo)
logo.pack(fill="x",padx = 10,pady = 5)

title = Button(f00,text ="Dainik Bhaskar",bg = "white" ,fg = "red"
              ,padx = 5,pady = 5,font = #("comicsansms", 20 , "bold")
              "comicsansms 40 bold", command = logos, borderwidth= 5,relief= SUNKEN)
title.pack( fill= "y",padx = 5,pady = 5)

title_city = Label(f11,text ="Nagpur City reports @ 30 november 2022 ",bg = "black" ,fg = "white"
              ,padx = 5,pady = 5,font = #("comicsansms", 14 , "bold")
              "comicsansms 15" , borderwidth= 2)
title_city.pack( fill= "x",padx = 5,pady = 5)

f1 = Frame(news_paper,bg = "purple", borderwidth=3,relief=SUNKEN)
f1.pack(side = LEFT, anchor = "n" ,fill = "x")

title_BN = Label(f1,text ="Breaking News",bg = "black" ,fg = "white"
              ,padx = 5,pady = 5,font = #("comicsansms", 14 , "bold")
              "comicsansms 15" , borderwidth= 5)
title_BN.pack( anchor="nw",side = TOP, fill= "x",padx = 5,pady = 5)

bihari = Label(f1,text ="Bihar: JD(U) expels spokesperson\n"
               "Ajay Alok, 3 others from party"
              ,padx = 5,pady = 5,font = #("comicsansms", 14 , "bold")
              "comicsansms 15 underline" , borderwidth= 5)
bihari.pack( anchor="w", fill= "x")
bihari_news = Label(f1,text ='''In a major political \n development in Bihar, the \n ruling Janata Dal (United) on  \n Tuesday (June 14) expelled \n its spokesperson Ajay Alok from the \n primary membership of the party. \n Besides Ajay Alok, JD(U) has also \n suspended state general secretaries \n Anil Kumar and Vipin Kumar Yadav  \n from primary membership. Partys \n state general secretaries Anil  \n Kumar and Vipin Yadav and spokesperson  \n Ajay Alok are relieved of their  \n posts and suspended from partys  \n primary membership. Party leader \n Jitendra Neeraj is also being \n suspended from the primary  \n membership of the party. '''
              ,font = #("comicsansms", 14 , "bold")
              "comicsansms 12 bold " , borderwidth= 10,bg = "blue",fg = "white")
bihari_news.pack( anchor="w", fill= "x")

f15 = Frame(news_paper,bg = "purple", borderwidth=3,relief=SUNKEN)
f15.pack(side = LEFT, anchor = "w" ,fill = "x")

bihari5 = Label(f15,text ="Bihar: JD(U) expels spokesperson\n"
               "Ajay Alok, 3 others from party"
              ,padx = 5,pady = 5,font = #("comicsansms", 14 , "bold")
              "comicsansms 15 underline" , borderwidth= 5)
bihari5.pack( anchor="w", fill= "x")
bihari_news5 = Label(f15,text ='''AMAN  \n development in Bihar, the \n ruling Janata Dal (United) on  \n Tuesday (June 14) expelled \n its spokesperson Ajay Alok from the \n primary membership of the party. \n Besides Ajay Alok, JD(U) has also \n suspended state general secretaries \n Anil Kumar and Vipin Kumar Yadav  \n from primary membership. Partys \n state general secretaries Anil  \n Kumar and Vipin Yadav and spokesperson  \n Ajay Alok are relieved of their  \n posts and suspended from partys  \n primary membership. Party leader \n Jitendra Neeraj is also being \n suspended from the primary  \n membership of the party. '''
              ,font = #("comicsansms", 14 , "bold")
              "comicsansms 12 bold " , borderwidth= 10,bg = "blue",fg = "white")
bihari_news5.pack( anchor="w", fill= "x")

f2 = Frame(news_paper,bg = "purple", borderwidth=3,relief=SUNKEN)
f2.pack(side = RIGHT, anchor = "n" ,fill = "x")

title_daily_update = Label(f2,text ="Daily Update",bg = "black" ,fg = "white"
              ,padx = 5,pady = 5,font = #("comicsansms", 14 , "bold")
              "comicsansms 15" , borderwidth= 5)
title_daily_update.pack( anchor="ne",side = TOP, fill= "x",padx = 5,pady = 5)

bihar = Label(f2,text ="Bihar: JD(U) expels spokesperson\n "
              "Ajay Alok, 3 others from party"
              ,padx = 5,pady = 5,font = #("comicsansms", 14 , "bold")
              "comicsansms 15 underline" , borderwidth= 5)
bihar.pack( anchor="e", fill= "x")
bihar_news = Label(f2,text ='''In a major political\ndevelopment in Bihar, the\nruling Janata Dal (United) \non Tuesday (June 14) expelled\nits spokesperson Ajay Alok from\nthe primary membership of the party.\nBesides Ajay Alok, JD(U) has \nalso suspended state general \nsecretaries\nAnil Kumar and Vipin Kumar \nYadav from primary membership.\nPartys\nstate general secretaries Anil \nKumar and Vipin Yadav and \nspokesperson \nAjay Alok are relieved of \ntheir posts and suspended\nfrom partys \nprimary membership. Party\nleader Jitendra Neeraj is also being\nsuspended from the primary\nmembership of the party. '''
              ,font = #("comicsansms", 14 , "bold")
              "comicsansms 12 bold " , borderwidth= 10,bg = "blue",fg = "white")
bihar_news.pack( anchor="e", fill= "x")



f25 = Frame(news_paper,bg = "purple", borderwidth=3,relief=SUNKEN)
f25.pack(side = RIGHT, anchor = "e" ,fill = "x")

bihar5 = Label(f25,text ="Bihar: JD(U) expels spokesperson\n "
              "Ajay Alok, 3 others from party"
              ,padx = 5,pady = 5,font = #("comicsansms", 14 , "bold")
              "comicsansms 15 underline" , borderwidth= 5)
bihar5.pack( anchor="e", fill= "x")
bihar_news5 = Label(f25,text ='''SAHU\ndevelopment in Bihar, the\nruling Janata Dal (United) \non Tuesday (June 14) expelled\nits spokesperson Ajay Alok from\nthe primary membership of the party.\nBesides Ajay Alok, JD(U) has \nalso suspended state general \nsecretaries\nAnil Kumar and Vipin Kumar \nYadav from primary membership.\nPartys\nstate general secretaries Anil \nKumar and Vipin Yadav and \nspokesperson \nAjay Alok are relieved of \ntheir posts and suspended\nfrom partys \nprimary membership. Party\nleader Jitendra Neeraj is also being\nsuspended from the primary\nmembership of the party. '''
              ,font = #("comicsansms", 14 , "bold")
              "comicsansms 12 bold " , borderwidth= 10,bg = "blue",fg = "white")
bihar_news5.pack( anchor="e", fill= "x")



news_paper.mainloop()
 

