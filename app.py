import tkinter as tk
from tkinter import messagebox, filedialog
import psycopg2
import subprocess

class GeoJSONUploader:
    def __init__(self, root):
        self.root = root
        self.root.title("GeoJSON Uploader")
        self.root.geometry("450x400")
        self.root.config(bg="#f4f4f9")

        self.db_host = tk.StringVar()
        self.db_port = tk.StringVar()
        self.db_name = tk.StringVar()
        self.db_user = tk.StringVar()
        self.db_password = tk.StringVar()

        self.create_connection_widgets()

    def create_connection_widgets(self):
        header_label = tk.Label(self.root, text="Database Connection", font=("Arial", 18, "bold"), bg="#f4f4f9", fg="#333")
        header_label.pack(pady=10)

        self.create_input_field("Host:", self.db_host)
        self.create_input_field("Port:", self.db_port)
        self.create_input_field("Database Name:", self.db_name)
        self.create_input_field("User Name:", self.db_user)
        self.create_input_field("Password:", self.db_password, show="*")

        test_button = tk.Button(self.root, text="Test Connection", command=self.test_connection, bg="#4CAF50", fg="white", font=("Arial", 12), width=20, relief="flat")
        test_button.pack(pady=15)

    def create_input_field(self, label_text, variable, show=None):
        frame = tk.Frame(self.root, bg="#f4f4f9")
        frame.pack(pady=5, fill="x", padx=30)

        label = tk.Label(frame, text=label_text, font=("Arial", 12), bg="#f4f4f9", fg="#333")
        label.pack(side="left", padx=5)

        entry = tk.Entry(frame, textvariable=variable, font=("Arial", 12), show=show, relief="solid", bd=2, width=25)
        entry.pack(side="left", padx=5)

    def create_file_upload_widgets(self):
        for widget in self.root.winfo_children():
            widget.pack_forget()

        header_label = tk.Label(self.root, text="GeoJSON Upload", font=("Arial", 18, "bold"), bg="#f4f4f9", fg="#333")
        header_label.pack(pady=10)

        self.file_path = tk.StringVar()
        self.table_name = tk.StringVar()

        tk.Label(self.root, text="Select GeoJSON File:", font=("Arial", 12), bg="#f4f4f9", fg="#333").pack(pady=5)

        file_button = tk.Button(self.root, text="Select File", command=self.select_file, bg="#2196F3", fg="white", font=("Arial", 12), width=20, relief="flat")
        file_button.pack(pady=10)

        tk.Label(self.root, text="Table Name:", font=("Arial", 12), bg="#f4f4f9", fg="#333").pack(pady=5)

        table_entry = tk.Entry(self.root, textvariable=self.table_name, font=("Arial", 12), relief="solid", bd=2, width=30)
        table_entry.pack(pady=10)

        save_button = tk.Button(self.root, text="Save", command=self.save_to_db, bg="#4CAF50", fg="white", font=("Arial", 12), width=20, relief="flat")
        save_button.pack(pady=20)

    def test_connection(self):
        try:
            conn = psycopg2.connect(
                host=self.db_host.get(),
                port=self.db_port.get(),
                dbname=self.db_name.get(),
                user=self.db_user.get(),
                password=self.db_password.get()
            )
            conn.close()
            messagebox.showinfo("Success", "Connection Successful!")
            self.create_file_upload_widgets()
        except Exception as e:
            messagebox.showerror("Error", f"Connection Error: {e}")

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("GeoJSON Files", "*.geojson")])
        if file_path:
            self.file_path.set(file_path)

    def save_to_db(self):
        if not self.file_path.get():
            messagebox.showerror("Error", "Please select a GeoJSON file!")
            return
        if not self.table_name.get():
            messagebox.showerror("Error", "Please enter a table name!")
            return

        command = f'ogr2ogr -f "PostgreSQL" PG:"host={self.db_host.get()} port={self.db_port.get()} dbname={self.db_name.get()} user={self.db_user.get()} password={self.db_password.get()}" "{self.file_path.get()}" -nln {self.table_name.get()}'
        
        try:
            subprocess.run(command, shell=True, check=True)
            messagebox.showinfo("Success", "Data successfully uploaded!")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Error running command: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeoJSONUploader(root)
    root.mainloop()
