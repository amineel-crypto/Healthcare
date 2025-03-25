import customtkinter as ctk
from database.db_connection import initialize_db
from ui.main_window import MainWindow

def main():
    # Initialize the database
    initialize_db()

    # Start the application
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()