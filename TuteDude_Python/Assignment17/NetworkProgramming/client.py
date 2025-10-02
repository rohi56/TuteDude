import socket
from tkinter import *

def send(listbox, entry):
    msg = entry.get()
    if msg:
        listbox.insert(END, "Client: " + msg)
        s.send(msg.encode("utf-8"))
        entry.delete(0, END)

def receive(listbox):
    try:
        msg = s.recv(1024)
        if msg:
            listbox.insert(END, "Server: " + msg.decode("utf-8"))
        else:
            listbox.insert(END, "Server disconnected.")
    except:
        listbox.insert(END, "Error receiving message.")

# ---------------- GUI ----------------
root = Tk()
root.title("Client Chat")

listbox = Listbox(root, width=50, height=15)
listbox.pack()

entry = Entry(root, width=40)
entry.pack(side=LEFT, padx=5, pady=5)

button = Button(root, text="Send", command=lambda: send(listbox, entry))
button.pack(side=LEFT, padx=5, pady=5)

receivebutton = Button(root, text="Receive", command=lambda: receive(listbox))
receivebutton.pack(side=RIGHT, padx=5, pady=5)

# ---------------- SOCKET ----------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
port = 12345
s.connect((host_name, port))

root.mainloop()
s.close()
