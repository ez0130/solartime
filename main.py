from tkinter import *
import requests
from tkinter import ttk



def get_sun():
    lat = str(latitude.get())
    lng = str(longitude.get())
    url = "https://api.sunrise-sunset.org/json?lat=" + str(lat) + "&lng=" +str(lng)
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    datas = data["results"]
    times = datas[timelist.get()]
    if timelist.get() != "day_length":
        
        if len(times) != 11:
            times = '0' + times
        hours = int(times[0:2])
        time_edit = gmt.get() 
        subtract = False
        if time_edit[0] == '-':
            subtract = True
        timenumber = int(time_edit[1:])
        if subtract :
            hours = hours - timenumber
        else:
            hours = hours + timenumber
        print(hours)
        if hours > 12:
            if times[-2] == 'P':
                times = times.replace('P', 'A')
                hours = hours -12
            else: 
                times = times.replace('A', 'P')
                huors = hours - 12
        if hours < 0:
            if times[-2] == 'P':
                times = times.replace('P', 'A')
                hours = hours + 12
            else: 
                times = times.replace('A', 'P')
                huors = hours + 12
        times = str(hours) + times[2:]
        
    
    canvas.itemconfig(quote_text, text=times)

window = Tk()
window.title("Sun rise...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=200)
quote_text = canvas.create_text(150, 100, text="Times for", width=300, font=("Arial", 30, "bold"), fill="black")
canvas.grid(row=5, column=0)
label1 = Label(text ="Latitude", font=("Arial", 30, "bold"))
label1.grid(row=2, column = 0)
label2 = Label(text = "Longitude", font=("Arial", 30, "bold"))
label2.grid(row=3, column = 0)
comb = Label(window,text = "Select the option", font = ("Arial", 20, "bold"))
comb.grid(row = 1, column =0 )
timelist = ttk.Combobox(window, 
                            values=[
                                    "sunrise", 
                                    "sunset",
                                    "solar_noon",
                                    "day_length",
                                    "civil_twilight_begin",
                                    "civil_twilight_end",
                                    "nautical_twilight_begin",
                                    "nautical_twilight_end",
                                    "astronomical_twilight_begin",
                                    "astronomical_twilight_end"])
label3 = Label(text = "GMT \n (ex: +0, +3, -2)", font = ("Arial", 20, "bold"))
label3.grid(row=4, column = 0)

gmt = Entry ()
gmt.grid(row= 4, column = 1)
timelist.grid(row = 1, column = 1)

latitude = Entry()
longitude = Entry()
latitude.grid(row=2, column = 1)
longitude.grid(row=3, column = 1)




sun_img = PhotoImage(file="sun.png")
sun_button = Button(image=sun_img, highlightthickness=0, command=get_sun)
sun_button.grid(row=5, column=1)



window.mainloop()