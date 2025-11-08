import tkinter as tk
from tkinter import ttk, Listbox, END, messagebox
from typing import Optional, Any

class FeedBackDlg(tk.Toplevel):
    """
    A modal dialog (Toplevel) window to capture user feedback using various widgets.
    """
    
    def __init__(self, parent: tk.Tk):
        # Toplevel is used for dialogs/sub-windows
        super().__init__(parent)
        self.parent = parent
        self.title("User Feedback Form")
        self.transient(parent) # Set dialog to be on top of the parent window
        
        # Data variables for widgets
        self.serviceFeedback = tk.IntVar(self, value=1) # 1=Excellent (default)
        self.electronicsChoice = tk.BooleanVar(self)
        self.sportsChoice = tk.BooleanVar(self)
        self.gardeningChoice = tk.BooleanVar(self)
        self.dept = tk.StringVar(self, value="Sales") # Default value for Combobox

        self.init_ui()

    def init_ui(self):
        """Initializes all widgets and layout for the dialog."""
        
        # Position the dialog relative to the parent window
        self.geometry("350x450") 
        self.resizable(False, False)

        # --- Radio Buttons (Service Feedback) ---
        ttk.Label(self, text="1. Service Feedback:", font=("Arial", 10, "bold")).place(x=20, y=20)
        
        y_start_radio = 45
        ttk.Radiobutton(self, text="Excellent", variable=self.serviceFeedback, value=1).place(x=30, y=y_start_radio)
        ttk.Radiobutton(self, text="Good", variable=self.serviceFeedback, value=2).place(x=30, y=y_start_radio + 20)
        ttk.Radiobutton(self, text="Poor", variable=self.serviceFeedback, value=3).place(x=30, y=y_start_radio + 40)
        
        # --- Checkboxes (Interests) ---
        ttk.Label(self, text="2. Your Interests:", font=("Arial", 10, "bold")).place(x=20, y=120)
        
        y_start_check = 145
        ttk.Checkbutton(self, text="Electronics", variable=self.electronicsChoice).place(x=30, y=y_start_check)
        ttk.Checkbutton(self, text="Sports", variable=self.sportsChoice).place(x=30, y=y_start_check + 20)
        ttk.Checkbutton(self, text="Gardening", variable=self.gardeningChoice).place(x=30, y=y_start_check + 40)
        
        # --- List Box (State Selection) ---
        ttk.Label(self, text="3. Select Your State:", font=("Arial", 10, "bold")).place(x=20, y=225)
        
        self.lb = Listbox(self, height=4, selectmode=tk.SINGLE)
        states = ["Kampala", "Entebbe", "Jinja", "Mbarara"]
        for state in states:
            self.lb.insert(END, state)
        self.lb.place(x=30, y=250, width=150)
        # Set default selection for the Listbox (Index 0: Kampala)
        self.lb.select_set(0)

        # --- Drop Down / Combobox (Department) ---
        ttk.Label(self, text="4. Select Department:", font=("Arial", 10, "bold")).place(x=200, y=225)
        
        self.cb = ttk.Combobox(self, textvariable=self.dept, state="readonly", values=("Sales", "Marketing", "Support", "Finance"))
        # Set the default value via the StringVar self.dept, initialized in __init__
        self.cb.place(x=200, y=250, width=120)
        self.cb.current(0) # Ensure the default is set in the widget

        # --- Buttons ---
        xpos1, xpos2 = 80, 200
        ypos = 380

        # Submit Button (from PDF)
        btnSubmit = ttk.Button(self, text="Submit", command=self.btnSubmitClick, style="MainButton.TButton")
        btnSubmit.place(x=xpos1, y=ypos)

        # Exit/Close Button
        btnClose = ttk.Button(self, text="Close", command=self.destroy)
        btnClose.place(x=xpos2, y=ypos)

        # Configure geometry management to center the dialog on the parent
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        x = self.parent.winfo_x() + (self.parent.winfo_width() // 2) - (w // 2)
        y = self.parent.winfo_y() + (self.parent.winfo_height() // 2) - (h // 2)
        self.geometry(f'{w}x{h}+{x}+{y}')

        # Set focus and modal behavior
        self.grab_set() # Captures all input until the window is closed

    # --- Event Handler from PDF ---
    def btnSubmitClick(self):
        """
        Retrieves data from all form controls and prints them to the console.
        """
        
        # Retrieve Checkbox values (BooleanVar)
        electronics = self.electronicsChoice.get()
        sports = self.sportsChoice.get()
        gardening = self.gardeningChoice.get()
        
        # Retrieve Radio Button value (IntVar)
        service_feedback_value = self.serviceFeedback.get()
        
        # Retrieve Listbox selection (returns a tuple of selected indices, we take the first one)
        listbox_selection_index = self.lb.curselection()
        if listbox_selection_index:
            state_index = listbox_selection_index[0]
            state_value = self.lb.get(state_index)
        else:
            state_value = "No State Selected"

        # Retrieve Combobox value (StringVar)
        department_value = self.dept.get()
        
        # Print results to console (as required by the PDF snippet)
        print("\n--- Feedback Form Submitted Data ---")
        print(f"Interests: electronics={electronics}, sports={sports}, gardening={gardening}")
        print(f"Service Feedback (1=Ex, 3=Poor): {service_feedback_value}")
        print(f"State Selection: {state_value}")
        print(f"Department Selected: {department_value}")
        print("------------------------------------")
        
        messagebox.showinfo("Success", "Feedback submitted successfully! Check console for data.")
        self.destroy() # Close the dialog after submission

    def show(self):
        """Makes the dialog modal and waits until it is closed."""
        self.wait_window(self)