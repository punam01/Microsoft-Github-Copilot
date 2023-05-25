from tkinter import *
import tkinter.messagebox
import customtkinter
import tool
# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("Dark")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")

city = tool.get_location()
current_weather = tool.get_weather(city)
print(current_weather)

# create main window


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(
            self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Weather Tool", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_Label_1 = customtkinter.CTkLabel(
            self.sidebar_frame, width=200, text="Coordinates:", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.sidebar_Label_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_Label_2 = customtkinter.CTkLabel(
            self.sidebar_frame, bg_color="#6666ff", width=200, text="Laditute: "+current_weather["latitude"])
        self.sidebar_Label_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_Label_3 = customtkinter.CTkLabel(
            self.sidebar_frame, bg_color="#6666ff", width=200, text="Longitude: "+current_weather["longitude"])
        self.sidebar_Label_3.grid(row=3, column=0, padx=20, pady=5)
        # create a box to sipaly wetaher icon
        self.weather_icon = customtkinter.CTkLabel(
            self.sidebar_frame, text=current_weather["icon"], font=customtkinter.CTkFont(size=70, weight="bold"), wraplength=20)
        self.weather_icon.grid(row=4, column=0, padx=20, pady=10)
        #craete a label for temperature and city with city above and bold
        self.sidebar_Label_4 = customtkinter.CTkLabel(
            self.sidebar_frame, width=200, text="Temperature:", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.sidebar_Label_4.grid(row=5, column=0, padx=20, pady=10)
        self.sidebar_Label_5 = customtkinter.CTkLabel(
            self.sidebar_frame, width=200, text=current_weather["current_city"],font=customtkinter.CTkFont(size=15, weight="bold"))
        self.sidebar_Label_5.grid(row=6, column=0, padx=20, pady=10)
        self.sidebar_Label_6 = customtkinter.CTkLabel(
            self.sidebar_frame, width=200, text=current_weather["current_temperature"],font=customtkinter.CTkFont(size=25, weight="bold"))
        self.sidebar_Label_6.grid(row=7, column=0, padx=20, pady=10)
        # create a switch to toggle unit of temperature standard imperial mertic
        switch = customtkinter.CTkSwitch(
            master=self.sidebar_frame, text="Standard")
        switch.grid(row=8, column=0, padx=10, pady=(0, 20))

        self.appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event, fg_color="#6666ff", button_color="#6666ff", button_hover_color="#3333cc")
        self.appearance_mode_optionemenu.grid(
            row=10, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=11, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=[
                                                               "80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event, fg_color="#6666ff", button_color="#6666ff", button_hover_color="#3333cc")
        self.scaling_optionemenu.grid(row=12, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(
            self, placeholder_text="Search City here....")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(
            20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(
            master=self, fg_color="transparent", bg_color="#6666ff", text="Search", hover_color="#3333cc", corner_radius=2, command=self.weather_search)
        self.main_button_1.grid(row=3, column=3, padx=(
            20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=0, column=1, padx=(
            20, 0), pady=(20, 0), sticky="nsew")
        self.textbox.insert("0.0", "Description of Current Weather\n\n" +current_weather["weather_description"] +"\n\n")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(
            20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Wind Speed")
        self.tabview.add("Wind Degree")

        #configure grid of individual tabs
        self.tabview.tab("Wind Speed").grid_columnconfigure(0, weight=1)  
        self.tabview.tab("Wind Degree").grid_columnconfigure(0, weight=1)

        #create a label in tab speed
        self.label_tab_speed = customtkinter.CTkLabel(
            self.tabview.tab("Wind Speed"), text=current_weather["wind_speed"],font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_tab_speed.grid(row=0, column=0, padx=20, pady=20)
         #create a labe for wind icon
        self.wind_icon = customtkinter.CTkLabel(
            self.tabview.tab("Wind Speed"), text="💨", font=customtkinter.CTkFont(size=50, weight="bold"), wraplength=20)
        self.wind_icon.grid(row=1, column=0, padx=20, pady=10)

        #create a label in tab degree
        self.label_tab_degree = customtkinter.CTkLabel(
            self.tabview.tab("Wind Degree"), text=current_weather["wind_deg"],font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_tab_degree.grid(row=0, column=0, padx=20, pady=20)
        #create a labe for wind icon
        self.wind_icon = customtkinter.CTkLabel(
            self.tabview.tab("Wind Degree"), text="🌬️", font=customtkinter.CTkFont(size=50, weight="bold"), wraplength=20)
        self.wind_icon.grid(row=1, column=0, padx=20, pady=10)
        

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=3,padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.tabview.add("Sunrise")
        self.tabview.add("Sunset")

        #configure grid of individual tabs
        self.tabview.tab("Sunrise").grid_columnconfigure(0, weight=1)  
        self.tabview.tab("Sunset").grid_columnconfigure(0, weight=1)

        #create a label in tab speed
        self.label_tab_sunrise = customtkinter.CTkLabel(
            self.tabview.tab("Sunrise"), text=current_weather["sunrise"],font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_tab_sunrise.grid(row=0, column=0, padx=20, pady=20)
         #create a labe for wind icon
        self.sunrise_icon = customtkinter.CTkLabel(
            self.tabview.tab("Sunrise"), text="🌅", font=customtkinter.CTkFont(size=50, weight="bold"), wraplength=20)
        self.sunrise_icon.grid(row=1, column=0, padx=20, pady=10)

        #create a label in tab degree
        self.label_tab_sunset = customtkinter.CTkLabel(
            self.tabview.tab("Sunset"), text=current_weather["sunset"],font=customtkinter.CTkFont(size=20, weight="bold"))
        self.label_tab_sunset.grid(row=0, column=0, padx=20, pady=20)
        #create a labe for wind icon
        self.sunset_icon = customtkinter.CTkLabel(
            self.tabview.tab("Sunset"), text="🌇", font=customtkinter.CTkFont(size=50, weight="bold"), wraplength=20)
        self.sunset_icon.grid(row=1, column=0, padx=20, pady=10)
        

        #create tab view 
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=1, column=3, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Atmospheric Pressure")
        self.tabview.add("Humidity")
        #create label in tabview
        self.label_tab_pressure = customtkinter.CTkLabel(
            self.tabview.tab("Atmospheric Pressure"), text=current_weather["current_pressure"],font=customtkinter.CTkFont(size=20, weight="bold"),wraplength=100)
        self.label_tab_pressure.grid(row=0, column=0, padx=20, pady=20)
        #create a text box READONLY in atmospheric pressure tab
        self.textbox_pressure = customtkinter.CTkTextbox(self.tabview.tab("Atmospheric Pressure"), width=250)
        self.textbox_pressure.grid(row=1, column=0, padx=10, pady=20)
        self.textbox_pressure.insert("0.0", "Atmospheric Pressure\n\n" +"Atmospheric Pressure influences various weather patterns and conditions. High pressure systems are associated with fair and stable weather, while low pressure systems often bring unsettled or stormy weather\n\n")
        
        #create label in tabview
        self.label_humidity = customtkinter.CTkLabel(
            self.tabview.tab("Humidity"), text=current_weather["current_humidity"],font=customtkinter.CTkFont(size=20, weight="bold"),wraplength=100)
        self.label_humidity.grid(row=0, column=0, padx=20, pady=20)
        #create a text box READONLY in atmospheric pressure tab
        self.textbox_humidity = customtkinter.CTkTextbox(self.tabview.tab("Humidity"), width=250)
        self.textbox_humidity.grid(row=1, column=0, padx=10, pady=20)
        self.textbox_humidity.insert("0.0", "Humidity\n\n" +"Humidityaffects how we perceive temperature and influences various weather conditions. Higher humidity levels can make the air feel more humid and uncomfortable, while lower humidity levels can result in drier conditions.\n\n")

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(
            self, label_text="CTkScrollableFrame")
        self.scrollable_frame.grid(row=1, column=2, padx=(
            20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(
                master=self.scrollable_frame, text=f"CTkSwitch {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)

        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(
            row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.checkbox_1 = customtkinter.CTkCheckBox(
            master=self.checkbox_slider_frame)
        self.checkbox_1.grid(row=1, column=0, pady=(
            20, 0), padx=20, sticky="n")
        self.checkbox_2 = customtkinter.CTkCheckBox(
            master=self.checkbox_slider_frame)
        self.checkbox_2.grid(row=2, column=0, pady=(
            20, 0), padx=20, sticky="n")
        self.checkbox_3 = customtkinter.CTkCheckBox(
            master=self.checkbox_slider_frame)
        self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

        # set default values
        self.checkbox_3.configure(state="disabled")
        self.checkbox_1.select()
        self.scrollable_frame_switches[0].select()
        self.scrollable_frame_switches[4].select()
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        
        

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(
            text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def weather_search(self):
        current_weather = tool.get_weather(self.entry.get())
        # update all text widgets with new weather data
        self.sidebar_Label_2.configure(
            text="Laditute: "+current_weather["latitude"])
        self.sidebar_Label_3.configure(
            text="Longitude: "+current_weather["longitude"])
        self.weather_icon.configure(text=current_weather["icon"])
        self.label_tab_speed.configure(text=current_weather["wind_speed"])
        self.label_tab_degree.configure(text=current_weather["wind_deg"])
        self.label_tab_sunrise.configure(text=current_weather["sunrise"])
        self.label_tab_sunset.configure(text=current_weather["sunset"])
        self.label_tab_pressure.configure(text=current_weather["current_pressure"])
        self.label_humidity.configure(text=current_weather["current_humidity"])
        self.textbox.delete("0.0", END)
        self.textbox.insert("0.0", "Description of Current Weather\n\n" +current_weather["weather_description"] +"\n\n")

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = App()
    app.mainloop()
