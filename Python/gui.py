from tkinter import *
import tkinter.messagebox
import customtkinter
import tool

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

city = tool.get_location()
current_weather = tool.get_weather(city)

# create main window
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Weather Tool")
        self.geometry(f"{1100}x{600}")
        
        # configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Weather Tool", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_Label_coordinates = customtkinter.CTkLabel(self.sidebar_frame, width=200, text="Coordinates:", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.sidebar_Label_coordinates.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_Label_Latitude = customtkinter.CTkLabel(self.sidebar_frame, bg_color="#4287f5", width=200, text="Laditute: "+str(current_weather["latitude"]))
        self.sidebar_Label_Latitude.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_Label_Longitude = customtkinter.CTkLabel(self.sidebar_frame, bg_color="#4287f5", width=200, text="Longitude: "+str(current_weather["longitude"]))
        self.sidebar_Label_Longitude.grid(row=3, column=0, padx=20, pady=5)

        self.weather_icon = customtkinter.CTkLabel(self.sidebar_frame, text=current_weather["icon"], font=customtkinter.CTkFont(size=70, weight="bold"), wraplength=20)
        self.weather_icon.grid(row=4, column=0, padx=20, pady=10)
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event, fg_color="#4287f5", button_color="#4287f5", button_hover_color="#3333cc")
        self.appearance_mode_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event, fg_color="#4287f5", button_color="#4287f5", button_hover_color="#3333cc")
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Search City here....")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_search = customtkinter.CTkButton(master=self, fg_color="transparent", bg_color="#4287f5", text="Search", hover_color="#4287f5", corner_radius=2, command=self.weather_search)
        self.main_button_search.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.textbox_desc = customtkinter.CTkTextbox(self, width=250)
        self.textbox_desc.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.textbox_desc.insert("0.0", "Description of Current Weather\n\n" +current_weather["weather_description"] +"\n\n")

        self.tabview_wind = customtkinter.CTkTabview(self, width=250)
        self.tabview_wind.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview_wind.add("Wind Speed")
        self.tabview_wind.add("Wind Degree")

        self.tabview_wind.tab("Wind Speed").grid_columnconfigure(0, weight=1)  
        self.tabview_wind.tab("Wind Degree").grid_columnconfigure(0, weight=1)

        self.label_tab_speed = customtkinter.CTkLabel(self.tabview_wind.tab("Wind Speed"), text=str(current_weather["wind_speed"])+" meter/sec",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_tab_speed.grid(row=0, column=0, padx=20, pady=20)

        self.wind_icon = customtkinter.CTkLabel(self.tabview_wind.tab("Wind Speed"), text="💨", font=customtkinter.CTkFont(size=50, weight="bold"), wraplength=20)
        self.wind_icon.grid(row=1, column=0, padx=20, pady=10)

        self.label_tab_degree = customtkinter.CTkLabel(self.tabview_wind.tab("Wind Degree"), text=str(current_weather["wind_deg"])+" degrees",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_tab_degree.grid(row=0, column=0, padx=20, pady=20)

        self.wind_icon = customtkinter.CTkLabel(self.tabview_wind.tab("Wind Degree"), text="🌬️", font=customtkinter.CTkFont(size=50, weight="bold"), wraplength=20)
        self.wind_icon.grid(row=1, column=0, padx=20, pady=10)        

        self.tabview_sun = customtkinter.CTkTabview(self, width=250)
        self.tabview_sun.grid(row=0, column=3,padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.tabview_sun.add("Sunrise")
        self.tabview_sun.add("Sunset")

        self.tabview_sun.tab("Sunrise").grid_columnconfigure(0, weight=1)  
        self.tabview_sun.tab("Sunset").grid_columnconfigure(0, weight=1)

        self.label_tab_sunrise = customtkinter.CTkLabel(self.tabview_sun.tab("Sunrise"), text=str(current_weather["sunrise"])+" IST",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_tab_sunrise.grid(row=0, column=0, padx=20, pady=20)

        self.sunrise_icon = customtkinter.CTkLabel(self.tabview_sun.tab("Sunrise"), text="🌅", font=customtkinter.CTkFont(size=50, weight="bold"), wraplength=20)
        self.sunrise_icon.grid(row=1, column=0, padx=20, pady=10)

        self.label_tab_sunset = customtkinter.CTkLabel(self.tabview_sun.tab("Sunset"), text=str(current_weather["sunset"])+" IST",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_tab_sunset.grid(row=0, column=0, padx=20, pady=20)

        self.sunset_icon = customtkinter.CTkLabel(self.tabview_sun.tab("Sunset"), text="🌇", font=customtkinter.CTkFont(size=50, weight="bold"), wraplength=20)
        self.sunset_icon.grid(row=1, column=0, padx=20, pady=10)

        self.tabview_atmp = customtkinter.CTkTabview(self, width=250)
        self.tabview_atmp.grid(row=1, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview_atmp.add("Atmospheric Pressure")
        self.tabview_atmp.add("Humidity")

        self.label_tab_pressure = customtkinter.CTkLabel(self.tabview_atmp.tab("Atmospheric Pressure"), text=str(current_weather["pressure"])+" hPa",font=customtkinter.CTkFont(size=20, weight="bold"),wraplength=100)
        self.label_tab_pressure.grid(row=0, column=0, padx=20, pady=20)

        self.textbox_pressure = customtkinter.CTkTextbox(self.tabview_atmp.tab("Atmospheric Pressure"), width=250)
        self.textbox_pressure.grid(row=1, column=0, padx=10, pady=20)
        self.textbox_pressure.insert("0.0", "Atmospheric Pressure\n\n" +"Atmospheric Pressure influences various weather patterns and conditions. High pressure systems are associated with fair and stable weather, while low pressure systems often bring unsettled or stormy weather\n\n")
        
        self.label_humidity = customtkinter.CTkLabel(self.tabview_atmp.tab("Humidity"), text=str(current_weather["humidity"])+" %",font=customtkinter.CTkFont(size=20, weight="bold"),wraplength=100)
        self.label_humidity.grid(row=0, column=0, padx=20, pady=20)

        self.textbox_humidity = customtkinter.CTkTextbox(self.tabview_atmp.tab("Humidity"), width=250)
        self.textbox_humidity.grid(row=1, column=0, padx=10, pady=20)
        self.textbox_humidity.insert("0.0", "Humidity\n\n" +"Humidityaffects how we perceive temperature and influences various weather conditions. Higher humidity levels can make the air feel more humid and uncomfortable, while lower humidity levels can result in drier conditions.\n\n")

        self.current_weather_frame = customtkinter.CTkFrame(self, width=250, corner_radius=0)
        self.current_weather_frame.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.current_weather_frame.grid_rowconfigure(4, weight=1)
        self.current_weather_frame.grid_columnconfigure(0, weight=1)
        self.current_weather_label = customtkinter.CTkLabel(self.current_weather_frame, text="Current Weather", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.current_weather_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_Label_city = customtkinter.CTkLabel(self.current_weather_frame, width=200, text=str(current_weather["name"]).capitalize(),font=customtkinter.CTkFont(size=30, weight="bold"))
        self.sidebar_Label_city.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_Label_temp = customtkinter.CTkLabel(self.current_weather_frame, width=200, text=str(current_weather["temp"])+" Kelvin",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.sidebar_Label_temp.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_Label_date = customtkinter.CTkLabel(self.current_weather_frame, width=200, text=str(current_weather["current_date_time"])+" IST")
        self.sidebar_Label_date.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_Label_country = customtkinter.CTkLabel(self.current_weather_frame, width=200, text=str(current_weather["country"]),font=customtkinter.CTkFont(size=30, weight="bold"))
        self.sidebar_Label_country.grid(row=1, column=0, padx=20, pady=10)
        
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")      

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def weather_search(self):
        if(self.entry.get() == "" or self.entry.get().isdigit()):
            tkinter.messagebox.showinfo("Error", "Please enter a city name")
            return 
        if(tool.get_weather(self.entry.get()) == None):
            tkinter.messagebox.showinfo("Error", "City not found")
            return
        else:
            current_weather = tool.get_weather(self.entry.get())
            self.sidebar_Label_Latitude.configure(text="Latitude: "+str(current_weather["latitude"]))
            self.sidebar_Label_Longitude.configure(text="Longitude: "+str(current_weather["longitude"]))
            self.weather_icon.configure(text=str(current_weather["icon"]))
            self.label_tab_speed.configure(text=str(current_weather["wind_speed"])+" meter/sec")
            self.label_tab_degree.configure(text=str(current_weather["wind_deg"])+" degrees")
            self.label_tab_sunrise.configure(text=str(current_weather["sunrise"])+" IST")
            self.label_tab_sunset.configure(text=str(current_weather["sunset"])+" IST")
            self.label_tab_pressure.configure(text=str(current_weather["pressure"])+" hPa")
            self.label_humidity.configure(text=str(current_weather["humidity"])+" %")
            self.textbox_desc.delete("0.0", END)
            self.textbox_desc.insert("0.0", "Description of Current Weather\n\n" +current_weather["weather_description"] +"\n\n")        
            self.sidebar_Label_city.configure(text=current_weather["name"].capitalize())
            self.sidebar_Label_temp.configure(text=str(current_weather["temp"])+" Kelvin")
            self.sidebar_Label_date.configure(text=str(current_weather["current_date_time"])+" IST")
            self.sidebar_Label_country.configure(text=current_weather["country"])
            self.entry.delete(0, END)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


if __name__ == "__main__":
    app = App()
    app.mainloop()
