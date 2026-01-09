import boto3
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

def sendRegularEmail(toAddresses, subject, message, fromAddress):
    client = boto3.client('ses')

    response = client.send_email(
        Destination={
            'ToAddresses': toAddresses,
            },
            Message={
                'Body': {
                    'Text': {
                        'Charset': 'UTF-8',
                        'Data': message,
                    },
                },
                'Subject': {
                    'Charset': 'UTF-8',
                    'Data': subject,
                },
            },
            Source = fromAddress,
    )

def sendEmailWithAttachment(toAddresses, subject, message, fromAddress, attachment_string, attachment_files):
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = fromAddress
    message['To'] = ', '.join(toAddresses)

    part = MIMEText(message, 'html')
    message.attach(part)

    if attachment_string:
        part = MIMEApplication(str.encode(attachment_string))
    elif attachment_files:
        for fi in attachment_files:
            part = MIMEApplication(open(fi["file_path"], 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename = fi["attachment_name"])
            message.attach(part)
    
    client = boto3.client('ses')

    response = client.send_raw_email(
        Source=message['From'],
        Destinations=toAddresses,
        RawMessage={
            'Data': message.as_string()
        }
)
