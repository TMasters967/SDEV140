#Author: Troy Masters
#Date written: 07/23/2023
#Assignment: Module# 8 exercise# Final Project 
#Short Desc: This program asks a user to select ingredients for a sandwich and then makes the sandwich

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

class SandwichApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sandwich App")
        self.root.geometry("500x500")
        

        # Bread choices
        self.bread_choices = ["White Bread", "Wheat Bread", "Sourdough Bread"]
        self.selected_bread = None

        # Meat choices
        self.meat_choices = ["Ham", "Turkey", "Roast Beef"]
        self.selected_meat = None

        # Cheese choices
        self.cheese_choices = ["Cheddar Cheese", "American Cheese", "Jalapeno Cheese"]
        self.selected_cheese = None

        # Condiment choices
        self.condiment_choices = ["Mayonnaise", "Mustard", "Chipotle Sauce"]
        self.selected_condiment = None

        # Vegetable choices
        self.vegetable_choices = ["Lettuce", "Onion", "Tomato", "Cucumbers"]
        self.selected_vegetables = []

        # Screen index
        self.screen_index = 0

        # First screen
        self.screens = [self.create_bread_screen, self.create_meat_screen, self.create_cheese_screen, self.create_condiment_screen, self.create_vegetable_screen]
        self.create_bread_screen()

    def create_bread_screen(self):
        self.clear_screen()

        # Label for bread choices
        bread_label = tk.Label(self.root, text="Select Bread", font=("Arial", 16))
        bread_label.pack(pady=10)

        # Buttons for bread choices
        for bread in self.bread_choices:
            bread_button = tk.Button(self.root, text=bread, font=("Arial", 12), command=lambda b=bread: self.select_bread(b))
            bread_button.pack()

        # Load and display image
        image = Image.open("bread.png")
        image = image.resize((300, 200))  # Adjust the image size as needed
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self.root, image=photo)
        image_label.image = photo
        image_label.pack()

        # Next button
        next_button = tk.Button(self.root, text="Next", font=("Arial", 12), command=self.next_screen)
        next_button.pack(pady=20)

    def create_meat_screen(self):
        self.clear_screen()

        # Label for meat choices
        meat_label = tk.Label(self.root, text="Select Meat", font=("Arial", 16))
        meat_label.pack(pady=10)

        # Buttons for meat choices
        for meat in self.meat_choices:
            meat_button = tk.Button(self.root, text=meat, font=("Arial", 12), command=lambda m=meat: self.select_meat(m))
            meat_button.pack()

        # Load and display image
        image = Image.open("meats.png")
        image = image.resize((300, 200))  # Adjust the image size as needed
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self.root, image=photo)
        image_label.image = photo
        image_label.pack()

        # Back button
        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), command=self.previous_screen)
        back_button.pack(pady=20)

        # Next button
        next_button = tk.Button(self.root, text="Next", font=("Arial", 12), command=self.next_screen)
        next_button.pack()

    def create_cheese_screen(self):
        self.clear_screen()

        # Label for cheese choices
        cheese_label = tk.Label(self.root, text="Select Cheese", font=("Arial", 16))
        cheese_label.pack(pady=10)

        # Buttons for cheese choices
        for cheese in self.cheese_choices:
            cheese_button = tk.Button(self.root, text=cheese, font=("Arial", 12), command=lambda c=cheese: self.select_cheese(c))
            cheese_button.pack()

        # Load and display image
        image = Image.open("cheese.png")
        image = image.resize((300, 200))  # Adjust the image size as needed
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self.root, image=photo)
        image_label.image = photo
        image_label.pack()
        

        # Back button
        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), command=self.previous_screen)
        back_button.pack(pady=20)

        # Next button
        next_button = tk.Button(self.root, text="Next", font=("Arial", 12), command=self.next_screen)
        next_button.pack()

    def create_condiment_screen(self):
        self.clear_screen()

        # Label for condiment choices
        condiment_label = tk.Label(self.root, text="Select Condiment", font=("Arial", 16))
        condiment_label.pack(pady=10)

        # Buttons for condiment choices
        for condiment in self.condiment_choices:
            condiment_button = tk.Button(self.root, text=condiment, font=("Arial", 12), command=lambda c=condiment: self.select_condiment(c))
            condiment_button.pack()
            
        # Load and display image
        image = Image.open("condiments.png")
        image = image.resize((300, 200))  # Adjust the image size as needed
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self.root, image=photo)
        image_label.image = photo
        image_label.pack()

        # Back button
        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), command=self.previous_screen)
        back_button.pack(pady=20)

        # Next button
        next_button = tk.Button(self.root, text="Next", font=("Arial", 12), command=self.next_screen)
        next_button.pack()

    def create_vegetable_screen(self):
        self.clear_screen()

        # Label for vegetable choices
        vegetable_label = tk.Label(self.root, text="Select Vegetables", font=("Arial", 16))
        vegetable_label.pack(pady=10)

        # Checkbuttons for vegetable choices
        self.vegetable_vars = []
        for vegetable in self.vegetable_choices:
            var = tk.IntVar()
            vegetable_check = tk.Checkbutton(self.root, text=vegetable, variable=var, font=("Arial", 12))
            vegetable_check.pack()
            self.vegetable_vars.append((vegetable, var))
            
        # Load and display image
        image = Image.open("veggies.png")
        image = image.resize((300, 200))  # Adjust the image size as needed
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(self.root, image=photo)
        image_label.image = photo
        image_label.pack()

        # Back button
        back_button = tk.Button(self.root, text="Back", font=("Arial", 12), command=self.previous_screen)
        back_button.pack(pady=20)

        # Next button
        next_button = tk.Button(self.root, text="Next", font=("Arial", 12), command=self.confirm_selection)
        next_button.pack()

    def previous_screen(self):
        if self.screen_index > 0:
            self.screen_index -= 1
            self.clear_screen()
            self.screens[self.screen_index]()

    def next_screen(self):
        if self.validate_selection():
            self.screen_index += 1
            self.clear_screen()
            self.screens[self.screen_index]()

    def validate_selection(self):
        if self.screen_index == 0 and self.selected_bread is None:
            messagebox.showwarning("Warning", "Please select a bread.")
            return False
        elif self.screen_index == 1 and self.selected_meat is None:
            messagebox.showwarning("Warning", "Please select a meat.")
            return False
        elif self.screen_index == 2 and self.selected_cheese is None:
            messagebox.showwarning("Warning", "Please select a cheese.")
            return False
        elif self.screen_index == 3 and self.selected_condiment is None:
            messagebox.showwarning("Warning", "Please select a condiment.")
            return False
        return True

    def confirm_selection(self):
        self.selected_vegetables = [vegetable for vegetable, var in self.vegetable_vars if var.get() == 1]

        confirm_message = f"Confirm Selection:\n\nBread: {self.selected_bread}\nMeat: {self.selected_meat}\nCheese: {self.selected_cheese}\nCondiment: {self.selected_condiment}\nVegetables: {', '.join(self.selected_vegetables)}"

        confirm = messagebox.askquestion("Confirmation", confirm_message)
        if confirm == "yes":
            self.make_sandwich()

    def make_sandwich(self):
        sandwich_message = f"Sandwich Created:\n\nBread: {self.selected_bread}\nMeat: {self.selected_meat}\nCheese: {self.selected_cheese}\nCondiment: {self.selected_condiment}\nVegetables: {', '.join(self.selected_vegetables)}"

        messagebox.showinfo("Success", sandwich_message)
        self.screen_index = 0
        self.create_bread_screen()

    def select_bread(self, bread):
        self.selected_bread = bread

    def select_meat(self, meat):
        self.selected_meat = meat

    def select_cheese(self, cheese):
        self.selected_cheese = cheese

    def select_condiment(self, condiment):
        self.selected_condiment = condiment

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
            
 

if __name__ == "__main__":
    root = tk.Tk()
    app = SandwichApp(root)
    root.mainloop()
