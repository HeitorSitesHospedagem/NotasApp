import tkinter as tk
from tkinter import filedialog
import threading

class TextEditorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Bloco de Notas")
        self.master.geometry("600x400")

        self.text_area = tk.Text(self.master, undo=True)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Arquivo", menu=self.file_menu)
        self.file_menu.add_command(label="Novo", command=self.new_file)
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Salvar", command=self.save_file)
        self.file_menu.add_command(label="Salvar como...", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command=self.master.quit)

    def new_file(self):
        self.text_area.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Arquivos de texto", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self):
        content = self.text_area.get(1.0, tk.END)
        threading.Thread(target=self._save_file, args=(content,)).start()

    def _save_file(self, content):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)
        self.master.update()  # Atualiza a interface após salvar

    def save_as_file(self):
        content = self.text_area.get(1.0, tk.END)
        threading.Thread(target=self._save_as_file, args=(content,)).start()

    def _save_as_file(self, content):
        file_path = filedialog.asksaveasfilename(filetypes=[("Arquivos de texto", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(content)
        self.master.update()  # Atualiza a interface após salvar

def main():
    root = tk.Tk()
    app = TextEditorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
