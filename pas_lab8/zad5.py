import imaplib


def imap_client_delete_message(server, port, user, password, message_id):
    mail = imaplib.IMAP4(server, port)
    mail.login(user, password)
    mail.select("inbox")
    mail.store(message_id, '+FLAGS', '\\Deleted')
    mail.expunge()
    print("Wiadomość została usunięta.")
    mail.logout()


imap_client_delete_message('212.182.24.27', 143, 'pasinf2017@infumcs.edu', 'P4SInf2017', '1')
