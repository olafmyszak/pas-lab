import imaplib


def imap_client_all_mailboxes_message_count(server, port, user, password):
    mail = imaplib.IMAP4(server, port)
    mail.login(user, password)
    result, mailboxes = mail.list()
    total_message_count = 0
    for mailbox in mailboxes:
        status, count = mail.status(mailbox.decode(), "(MESSAGES)")
        if status == "OK":
            message_count = int(count[0].split()[2].decode())
            total_message_count += message_count
            print(f"Liczba wiadomości w {mailbox.decode()}: {message_count}")
    print("Łącznie wiadomości we wszystkich skrzynkach:", total_message_count)
    mail.logout()


imap_client_all_mailboxes_message_count('212.182.24.27', 143, 'pasinf2017@infumcs.edu', 'P4SInf2017')
