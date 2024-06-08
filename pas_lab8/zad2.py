import imaplib


def imap_client_inbox_message_count(server, port, user, password):
    mail = imaplib.IMAP4(server, port)
    mail.login(user, password)
    mail.select("inbox")
    result, data = mail.search(None, "ALL")
    message_count = len(data[0].split())
    print("Liczba wiadomości w skrzynce Inbox:", message_count)
    mail.logout()


imap_client_inbox_message_count('212.182.24.27', 143, 'pasinf2017@infumcs.edu', 'P4SInf2017')
