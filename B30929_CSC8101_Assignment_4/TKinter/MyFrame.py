import tkinter as tk
from tkinter import ttk, Menu, messagebox, BOTH
import sys

# Import the Feedback Dialog class from the other file
from FeedBackDlg import FeedBackDlg 

# Global variable to hold the main application instance
app = None

class MyFrame(ttk.Frame):
    """
    Main application frame class containing the menu and basic layout.
    """
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()
        
    def init_ui(self):
        """Initializes the main user interface elements."""
        self.parent.title("Tkinter GUI Assignment Solution")
        self.style = ttk.Style()
        
        # Configure a main button style (as seen in the PDF)
        self.style.configure("MainButton.TButton", foreground="white", background="red", font=("Arial", 10, "bold"))
        self.style.configure("Exit.TButton", foreground="red", background="white")

        # Set up Menu Bar
        self.create_menu()
        
        # Basic layout elements
        self.label = ttk.Label(self, text="Welcome to the Tkinter Assignment", font=("Arial", 14, "bold"))
        self.label.place(x=50, y=50)

        # Button to launch the dialog
        btnLaunch = ttk.Button(self, 
                               text="Launch Feedback Form", 
                               command=self.btnLaunchFeedback,
                               style="MainButton.TButton")
        btnLaunch.place(x=100, y=100)

        # Exit button
        btnExit = ttk.Button(self, 
                             text="Exit Application", 
                             command=self.exitButtonClick,
                             style="Exit.TButton")
        btnExit.place(x=120, y=150)
        
        self.pack(fill=BOTH, expand=True)

    def create_menu(self):
        """Creates the File and Help menu bars."""
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        # File Menu
        file_menu = Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open Feedback Form", command=self.btnLaunchFeedback)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exitButtonClick)
        menubar.add_cascade(label="File", menu=file_menu)

        # Help Menu
        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

    def btnLaunchFeedback(self):
        """Launches the modal feedback dialog."""
        # Create and show the modal dialog
        dialog = FeedBackDlg(self.parent) 
        # The show() method handles the wait_window() to make it modal
        dialog.show() 

    def show_about(self):
        """Shows an information box."""
        messagebox.showinfo("About", "Tkinter Assignment Solution by Gemini.")

    # --- Event Handler from PDF ---
    def exitButtonClick(self):
        """Handles the application exit with confirmation."""
        if messagebox.askokcancel("OK to close?", "Close application?"):
            self.parent.destroy()
            sys.exit() # Ensure the entire Python process closes


def main():
    """Main entry point of the Tkinter application."""
    global app
    root = tk.Tk()
    # Set the initial size and position the window near the center
    root.geometry("400x300+400+300")
    root.resizable(False, False) # Recommended for simpler apps
    app = MyFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()