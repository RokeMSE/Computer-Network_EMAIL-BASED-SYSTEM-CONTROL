import time
import datetime
import smtplib
import imaplib
import email.message
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 

user = "computernetworkbob@gmail.com"
password = "xjoa qbfz vhvr qgqp"
imapserver = "imap.gmail.com"  # imap server for account
smtpserver = "smtp.gmail.com"  # smtp server for account

def imap_init():
    """
    Initialize IMAP connection
    """
    print("Initializing IMAP... ", end = '')
    global imap
    imap = imaplib.IMAP4_SSL(imapserver, 993)
    imap.login(user, password)
    print("Done.")

def smtp_init():
    """
    Initialiaze SMTP connection
    """
    print("Initializing SMTP...")
    global smtp
    smtp = smtplib.SMTP_SSL(smtpserver)
    smtp.login(user, password)
    print("Done.")

def send_mail(smtp, user, sender, msg: MIMEMultipart):
    print("[Info] Sending mail...")

    # Create a reply message
    reply_msg = MIMEMultipart()
    reply_msg['From'] = user
    reply_msg['To'] = sender
    reply_msg['Subject'] = "Re: "
    reply_msg.attach(msg)

    # Send a reply message to the sender
    smtp.sendmail(user, sender, reply_msg.as_string())

    print("[Info] Mail sent to", sender, "successfully")

def receive_mail(imap, smtp):
    print("[Info] Receiving mail...")
    while True:
        # refresh mail box
        imap.select('Inbox')

        # search for unseen messages since last day
        date_since = (datetime.date.today() -
                      datetime.timedelta(days=1)).strftime("%d-%b-%Y")
        status, data = imap.search(None, '(UNSEEN SINCE "' + date_since + '")')

        if data[0] == b'':
            print('[Info] No new emails')
        else:
            print('[Info] New emails received')

            # Process the new messages
            for msg_id in data[0].split():
                typ, data = imap.fetch(msg_id, '(RFC822)')
                email_body = data[0][1]
                mail_message = email.message_from_bytes(email_body)

                # Get the sender, subject, and content of the message
                sender = mail_message['From']
                subject = mail_message['Subject']

                # check is multipart (ex: attachment, emoji, image)
                if mail_message.is_multipart():
                    content = mail_message.get_payload()[0].get_payload()
                else:
                    content = mail_message.get_payload()

                # Print the message details to the console
                print('- From:', sender)
                print('- Subject:', subject)
                print('- Content:', content)

                # Mark the message as read
                imap.store(msg_id, '+FLAGS', '\\SEEN')

                # do something here
                res = function(subject)

                # reply back to sender
                send_mail(smtp, user, sender,  res)

        # Sleep for 10 second before checking for new emails again
        time.sleep(10)

def function(msg):
    print("[Info] Processing message...")
    res = MIMEMultipart()
    if msg == 'HELLO':
        res.attach(MIMEText('Hello world'))
    else:
        res.attach(MIMEText('Invalid command'))
    return res

imap_init()
smtp_init()
receive_mail(imap, smtp)