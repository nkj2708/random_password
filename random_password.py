import tkinter as tk
import random
import string

def generate_password():
    length = int(entry.get())
    if length <= 0:
        display.config(text="Please enter a positive value")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(length))
    display.config(text=generated_password)

# Creating the main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("300x400")
root.config(bg="grey")

# Creating and placing widgets

#Heading of the project
heading = tk.Label(root, text="Password Generator",font=("Arial",20,"bold","underline"),bg="blue")
heading.pack(pady=10)

#Taking input length from the user
input = tk.Label(root, text="Enter Password Length:",font=("Arial",10),bg="yellow")
input.pack(pady=10)

#Taking Entry
entry = tk.Entry(root)
entry.pack(pady=10)

#Button to execute and generate password
button = tk.Button(root, text="Generate Password", command=generate_password,font=("Arial",10),bg="orange")
button.pack(pady=10)

#Displaying password
display = tk.Label(root, text="", wraplength=500, justify="center",bg="pink")
display.pack()

# Starting the GUI event loop
root.mainloop()
