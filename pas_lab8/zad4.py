import imaplib


def imap_client_unread_messages(server, port, user, password):
    mail = imaplib.IMAP4(server, port)
    mail.login(user, password)
    mail.select("inbox")
    result, data = mail.search(None, "UNSEEN")
    if result == "OK":
        for num in data[0].split():
            result, message_data = mail.fetch(num, "(RFC822)")
            if result == "OK":
                print("Nieprzeczytana wiadomość:")
                print(message_data[0][1].decode('utf-8'))
                mail.store(num, '+FLAGS', '\\Seen')
    mail.logout()


imap_client_unread_messages('212.182.24.27', 143, 'pasinf2017@infumcs.edu', 'P4SInf2017')
