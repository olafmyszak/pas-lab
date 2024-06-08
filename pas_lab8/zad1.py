import telnetlib


def imap_check_message_count(server, port, user, password):
    tn = telnetlib.Telnet(server, port)
    tn.read_until(b"* OK")

    tn.write(b"1 LOGIN " + user.encode('ascii') + b" " + password.encode('ascii') + b"\r\n")
    tn.read_until(b"1 OK")

    tn.write(b"2 SELECT INBOX\r\n")
    response = tn.read_until(b"2 OK").decode('ascii')

    message_count = response.split()[1]
    print("Liczba wiadomości w skrzynce INBOX:", message_count)

    tn.write(b"3 LOGOUT\r\n")
    tn.read_until(b"3 OK")

    tn.close()


imap_check_message_count('212.182.24.27', 143, 'pasinf2017@infumcs.edu', 'P4SInf2017')
