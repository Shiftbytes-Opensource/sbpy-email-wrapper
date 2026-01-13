from sbpyEmailWrapper.mailServices.aws_ses import sendRegularEmail as AWSsendRegularEmail
import os, re
from sbpyEmailWrapper.errors import InvalidToEmailAddress, InvalidFromEmailAddress, InvlidEmailService, AttachmentsNotsupported, AsyncSendNotSupported, NoCallbackFunctionGiven

class EmailWrapper:
    
    def __init__(self, email_service_name, async_send = False, callback_function = None):
        if not email_service_name:
            raise InvlidEmailService
        
        if async_send:
            raise AsyncSendNotSupported
            if not callback_function:
                raise NoCallbackFunctionGiven
        
        self.email_service_name = email_service_name

    def is_valid_email(email):
        """
        Checks if the email string matches a common email format using regex.
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
        # re.fullmatch ensures the ENTIRE string matches the pattern, 
        # which is preferred for validation in Python 3.4+.
        if re.fullmatch(pattern, email):
            return True
        else:
            return False

    def sendMail(self, toAddress, fromAddress, subject, body, attachements = None):
        toAddressList = []

        if not toAddress:
            raise InvalidToEmailAddress

        if isinstance(toAddress, str):
            if not self.is_valid_email(toAddress):
                raise InvalidToEmailAddress
            toAddressList.append(toAddress)
        elif isinstance(toAddress, list):
            for em in toAddress:
                if not self.is_valid_email(em):
                    raise InvalidToEmailAddress
                else:
                    toAddressList.append(em)
        
        if not fromAddress or not isinstance(fromAddress, str):
            raise InvalidFromEmailAddress
        
        if attachements:
            hasAttachments = True
            raise AttachmentsNotsupported
        else:
            #No attachments
            AWSsendRegularEmail(toAddressList, subject, body, fromAddress)
    
    def isValidPath(filename):
        if os.path.isfile(filename):
            return True
        
        return False
