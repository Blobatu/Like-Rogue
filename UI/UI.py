import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

app = customtkinter.CTk()
app.title("Like-Rogue")
app.geometry("800x600")

label = customtkinter.CTkLabel(master=app, text="Like-Rogue", font=("Pixel", 24, "bold"))
label.pack(pady=12, padx=10)



def play():
    print("Play button clicked")



    frame = customtkinter.CTkFrame(master=app)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    play_button = customtkinter.CTkButton(master=frame, text="Play", command=play)
    play_button.pack(pady=12, padx=10)

def open_settings():    
    print("Settings button clicked")

    settings_button = customtkinter.CTkButton(app, text="Settings", command=open_settings)
    settings_button.pack(pady=12, padx=10)

    exit_button = customtkinter.CTkButton(app, text="Exit", command=app.quit)
    exit_button.pack(pady=12, padx=10)

    app.mainloop()