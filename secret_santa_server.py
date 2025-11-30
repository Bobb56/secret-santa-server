import socket
from rsa import *

HOST = '0.0.0.0'  # écoute sur toutes les interfaces réseau
PORT = 12345



def handle_request(data):
    data = data.split('\0')

    if not (len(data) > 0 and len(data) <= 3):
        return "ERROR"

    function = data[0]
    
    if function == "getPhase":
        f = open("phase", "r")
        phase = f.read()
        f.close()
        return phase
    
    elif function == "getAllNames":
        try:
            f = open("public_keys.txt", "r")
            dict = eval(f.read())
            f.close()
            return str(list(dict.keys()))
        except FileNotFoundError:
            return str([])
    
    elif function == "addName":
        if len(data) < 3:
            return "ERROR"
        
        name = data[1]
        pubkey = eval(data[2])
        
        try:
            f = open("public_keys.txt", "r")
            dict = eval(f.read())
            f.close()
        except FileNotFoundError:
            dict = {}
        
        if name in dict:
            return "ERROR"
        
        dict[name] = pubkey

        f = open("public_keys.txt", "w+")
        f.write(str(dict))
        f.close()

        return ""
    
    elif function == "decode":

        if len(data) < 2:
            return "ERROR"
        
        name = data[1]

        f = open("result.txt", "r")
        result = eval(f.read())
        f.close()
        
        if not (name in result):
            return "ERROR"

        return result[name]
    else:
        return "ERROR"




def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        print(f"Serveur en écoute sur le port {PORT}")
        while True:
            try:
                conn, addr = s.accept()
                conn.settimeout(5)
                data = conn.recv(1024)
                if data:
                    data = data.decode()
                    response = bytes(handle_request(data), "utf-8")
                    conn.sendall(response)
                    conn.close()
            except KeyboardInterrupt:
                break

main()
