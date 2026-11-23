import tkinter as tk

window = tk.Tk()

window.title("Miles to Km Converter")
window.geometry("400x200")
window.config(padx=20, pady=20)


# label Miles
label = tk.Label(window, text="Miles", font=("Open Sans", 20))
label.grid(row=0, column=0)
label.place(x=255,y=4)


# Input box
input = tk.Entry(window, width=10,font=("Open Sans", 20) )
input.place(x=110,y=2)
input.insert(tk.END,"0")

# label "is equal to"
label_2 = tk.Label(window, text="is equal to", font=("Open Sans", 20))
label_2.place(x=1,y=50)

# label "0"
label_3 = tk.Label(window, text="0", font=("Open Sans", 20))
label_3.place(x=175,y=52)


# label "Km"
label_4 = tk.Label(window, text="Km", font=("Open Sans", 20))
label_4.place(x=265,y=50)


# button functionality

def miles_km_converter():

  user_input = input.get()
  miles = float(user_input)
  non_rounded_km = miles * 1.60934
  rounded_km = round(non_rounded_km, 2)
  label_3['text'] = str(rounded_km)








# button "Calculate"
button_c = tk.Button(text="Calculate", font=("Open Sans",20), command=miles_km_converter)
button_c.place(x=125,y=90)


window.mainloop()