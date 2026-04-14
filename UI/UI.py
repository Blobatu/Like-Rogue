import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def play():
    print("Play button clicked")



    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=frame, text="Like-Rogue", text_font=("Pixel", 24))
    label.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text="Play", command=play)
    button.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text="Settings")
    button.pack(pady=12, padx=10)

    root.mainloop()