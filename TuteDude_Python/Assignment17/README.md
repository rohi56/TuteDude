# Assignment 17: Network Programming – Building a Chat Application  

## 📌 Module  
**Module 22 – Network Programming in Python Using Socket**  

---

## 📄 Description  
This assignment demonstrates how to build a **chat application** in Python using the **socket library**.  
It consists of a **server** and **client** program, enabling real-time text communication over a network.  

The server listens for incoming connections, while the client connects and exchanges messages.  
This is a classic implementation of **TCP/IP socket programming** and provides a strong foundation for understanding networking concepts in Python.  

---

## 📂 Project Structure  

```plaintext
NetworkProgramming/
│── client.py            # Client-side chat application
│── server.py            # Server-side chat application
│── output_final.mp4     # Screen recording of code and working demo

```

## ⚙️ Explanation of Files
### 1. server.py

Initializes a socket server.

Binds it to a host (IP address) and port.

Listens for incoming client connections.

Handles the chat communication by receiving and sending messages.

### 2. client.py

Connects to the server using IP and port.

Allows the user to type messages.

Sends messages to the server and displays responses from other connected clients.

### 3. output_final.mp4

A screen recording showing the working of the chat application.

Demonstrates both server and client interaction.

## ▶️ Demo Video

![Demo Video](.NetworkProgramming/original.mp4)

## 📝 Notes

For security reasons, some terminal portions are slightly hidden since they displayed the system ID.

The functionality remains fully intact and identical to the course lecture demonstration.