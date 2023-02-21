# All the Necessary Imports
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# Main Form
root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)
root.configure(bg="#ede6e7")

# This Function will take the city or country from the textfield and get the Weather using Open Weather API 
def getWeather():
    city = textfield.get()
    geolocator = Nominatim(user_agent="geopiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")
    api_key = '21f6ebe6a361661195560a9709fe2a06'
    weather_url = "http://api.openweathermap.org/data/2.5/weather"
    weather_result = f"{weather_url}?appid={api_key}&q={city}"
    # Weather Result
    json_data = requests.get(weather_result).json()
    condition = json_data["weather"][0]["main"]
    description = json_data["weather"][0]["description"]
    temp = int(json_data["main"]["temp"] - 273.15)
    pressure = json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]
    wind = json_data["wind"]["speed"]

    # Assigning Temperature and Condition result to the label
    t.config(text=(temp, "°"), )
    c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"), bg= "#ede6e7")

    # Assigning Wind, Humidity, Description and Pressure result to the bottom Labels
    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)

    
# Search Box Text Field
textfield = tk.Entry(root, justify= "center", width= 20, font=("poppins", 25, "bold"), bg="#404040", border = 1, fg="white")
textfield.place(x=20, y=20)

# Search Button
Search_icon = PhotoImage(file = "search_icon.png")
myimage_icon = Button(image= Search_icon, borderwidth=2, width=50, height=35, cursor= "hand2", bg= "#404040", command = getWeather)
myimage_icon.place(x=400, y=20)

# Time
name = Label(root, font=("arial", 15, "bold"), bg= "#ede6e7")
name.place(x=30,y=100)
clock = Label(root, font=("helvetica", 20), bg= "#ede6e7")
clock.place(x=30, y=130)

# Logo
Logo_image = PhotoImage(file="weatherLogo.png")
logo = Label(image=Logo_image, bg="#ede6e7")
logo.place(x=160, y = 130)

# Bottom Label Background
resultLabel = Label(root, font=("arial", 45, "bold" ), bg="#1ab5ef", width=23, borderwidth=0, relief="ridge")
resultLabel.place(x=20,y=400)


# Wind
label1 = Label(root, text = "WIND", font=("Helvetica", 15, "bold"), fg = "white", bg="#1ab5ef")
label1.place(x=120,y=400)
w=Label(text = " ", font = ("arial", 20, "bold"), bg = "#1ab5ef")
w.place(x=120, y= 430)

# Humidity
label2 = Label(root, text = "HUMIDITY", font=("Helvetica", 15, "bold"), fg = "white", bg="#1ab5ef")
label2.place(x=250,y=400)
h=Label(text = " ", font = ("arial", 20, "bold"), bg = "#1ab5ef")
h.place(x=280, y= 430)

# Description
label3 = Label(root, text = "DESCRIPTION", font=("Helvetica", 15, "bold"), fg = "white", bg="#1ab5ef")
label3.place(x=430,y=400)
d=Label(text = " ", font = ("arial", 20, "bold"), bg = "#1ab5ef")
d.place(x=400, y= 430)

# Pressure
label4 = Label(root, text = "PRESSURE", font=("Helvetica", 15, "bold"), fg = "white", bg="#1ab5ef")
label4.place(x=650,y=400)
p=Label(text = " ", font = ("arial", 20, "bold"), bg = "#1ab5ef")
p.place(x=670, y= 430)

# Temperature
t = Label(font=("arial", 70, "bold"), bg= "#ede6e7", fg="#ee666d")
t.place(x=400, y=150)

# Condition
c=Label(font=("arial", 15, "bold"), bg= "#ede6e7")
c.place(x=400, y=250)

# MainLoop
root.mainloop()
