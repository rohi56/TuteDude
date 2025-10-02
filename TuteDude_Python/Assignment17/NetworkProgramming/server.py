import socket
from tkinter import *

def send(listbox, entry):
    msg = entry.get()
    if msg:
        listbox.insert(END, "Server: " + msg)
        client.send(msg.encode("utf-8"))
        entry.delete(0, END)

def receive(listbox):
    try:
        msg = client.recv(1024)
        if msg:
            listbox.insert(END, "Client: " + msg.decode("utf-8"))
        else:
            listbox.insert(END, "Client disconnected.")
    except:
        listbox.insert(END, "Error receiving message.")

# ---------------- GUI ----------------
root = Tk()
root.title("Server Chat")

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
s.bind((host_name, port))
s.listen(4)

print("Waiting for connection...")
client, addr = s.accept()

root.mainloop()

client.close()
s.close()
