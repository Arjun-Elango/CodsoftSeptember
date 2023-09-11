from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

A=Tk()
A.title("Weather Forecasting")
A.geometry("400x500")
A.resizable(False,False)

Arjun_color="#50C878"
A.config(bg=Arjun_color)

#function
def search():
    place=textfield.get()

    geolocator= Nominatim(user_agent="geoapiExercises")
    location= geolocator.geocode(place)
    t = TimezoneFinder()
    result = t.timezone_at(lng=location.longitude,lat=location.latitude)

    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    time.config(text=current_time)
    topic.config(text="Current Weather")
    #using openweather api for weather and temperature

    url="https://api.openweathermap.org/data/2.5/weather?q="+place+"&appid=979e4a64e3f1298eeeea0b9d428641a1"

    reponse = requests.get(url)
    data = reponse.json()

    condition = data['weather'][0]['main']
    description = data['weather'][0]['description']
    temp = int(data['main']['temp']-273.15)
    humidity = data['main']['humidity']

    temperature.config(text=(temp,"°"))
    cond.config(text=condition)
    weathr.config(text=(description,"|","FEELS", "LIKE",temp,"°"))
    hum.config(text=humidity)


#labels
title=tk.Label(A,bg=Arjun_color,text="Weather Forecasting \n Application",font=("Times",28,"bold"),fg="#0203E2")
title.pack(pady=7)

label_1=tk.Label(A,text="Enter The city Name:",font=("arial",10,),fg="#0203E2",bg=Arjun_color)
label_1.pack(pady=10)

textfield=tk.Entry(A,justify="center",width=17,font=("poppins",25,"bold"),bg="black",fg="white")
textfield.pack(pady=6)

btn_1= tk.Button(A,text="Get Weather Info",fg="#0203E2",command=search)
btn_1.pack(pady=5)

topic=tk.Label(A,font=("Helvetica",15,"bold"),bg=Arjun_color)
topic.pack(pady=5)

time=tk.Label(A,font=("Helvetica",10,"bold"),bg=Arjun_color)
time.pack(pady=5)

cond=tk.Label(A,font=("ariel",10,"bold"),bg=Arjun_color)
cond.pack()

weathr=tk.Label(A,font=("Helvetica",10,"bold"),bg=Arjun_color)
weathr.pack(pady=5)

hum=tk.Label(A,font=("Helvetica",10,"bold"),bg=Arjun_color)
hum.pack(pady=5)

temperature=tk.Label(A,font=("Helvetica",70,"bold"),bg=Arjun_color)
temperature.pack(pady=5)

A.mainloop()