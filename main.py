import tkinter as tk
from tkinter import messagebox
import json
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

ARQUIVO = "tasks.json"
tasks = []

# ---------------- FUNÇÕES ----------------
def carregar_tasks():
    global tasks
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            tasks = json.load(f)
            for t in tasks:
                texto = f"{'✔️' if t['done'] else '⬜'} {t['task']}"
                listbox.insert(tk.END, texto)

def salvar_tasks():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def add_task():
    task_text = entry.get().strip()
    if task_text:
        task = {"task": task_text, "done": False}
        tasks.append(task)
        listbox.insert(tk.END, f"⬜ {task_text}")
        entry.delete(0, tk.END)
        salvar_tasks()
    else:
        messagebox.showwarning("Aviso", "Digite uma tarefa por favor!")

def remove_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        listbox.delete(index)
        salvar_tasks()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa por favor!")

def toggle_done():
    try:
        index = listbox.curselection()[0]
        tasks[index]["done"] = not tasks[index]["done"]
        texto = f"{'✔️' if tasks[index]['done'] else '⬜'} {tasks[index]['task']}"
        listbox.delete(index)
        listbox.insert(index, texto)
        salvar_tasks()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa!")

#interface
root = ttk.Window(themename="darkly")
root.title("Tasks Vibes")
root.geometry("450x350")

# Entrada de texto (ttkbootstrap Entry)
entry = ttk.Entry(root, width=30, bootstyle="info")
entry.pack(pady=10)

# Botões
frame = ttk.Frame(root)
frame.pack(pady=5)

add_button = ttk.Button(frame, text="Adicionar", bootstyle="success-outline", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

remove_button = ttk.Button(frame, text="Remover", bootstyle="danger-outline", command=remove_task)
remove_button.pack(side=tk.LEFT, padx=5)

done_button = ttk.Button(frame, text="Concluir", bootstyle="primary-outline", command=toggle_done)
done_button.pack(side=tk.LEFT, padx=5)

# Lista personalizada (tk.Listbox)
listbox = tk.Listbox(root, width=50, height=12, bg="#2b2b2b", fg="white", selectbackground="#007bff")
listbox.pack(pady=10)

# Carregar tarefas salvas
carregar_tasks()

root.mainloop()
