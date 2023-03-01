import tkinter as tk
from tkinter import filedialog
import zipfile

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Décompresseur de fichiers")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Bouton pour sélectionner le fichier à décompresser
        self.file_button = tk.Button(self, text="Sélectionner un fichier", command=self.select_file)
        self.file_button.pack()

        # Label pour afficher le chemin du fichier sélectionné
        self.file_path_label = tk.Label(self)
        self.file_path_label.pack()

        # Bouton pour décompresser le fichier
        self.decompress_button = tk.Button(self, text="Décompresser le fichier", command=self.decompress_file, state="disabled")
        self.decompress_button.pack()

        # Label pour afficher le message de réussite ou d'erreur
        self.message_label = tk.Label(self)
        self.message_label.pack()

    def select_file(self):
        # Sélection du fichier à décompresser
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers zip", "*.zip")])
        if file_path:
            self.file_path_label.config(text=file_path)
            self.decompress_button.config(state="normal")

    def decompress_file(self):
        # Décompression du fichier sélectionné
        file_path = self.file_path_label.cget("text")
        try:
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall()
            self.message_label.config(text="Le fichier a été décompressé avec succès.")
        except Exception as e:
            self.message_label.config(text=f"Erreur : {e}")

# Création de l'application
root = tk.Tk()
app = Application(master=root)
app.mainloop()
