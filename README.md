# sbpy-email-wrapper
This project is aimed to simplify email integration in applications. This library / wrapper is written for python projects. This wrapper supports most popular email services such as AWS SES, Mailgun, etc. Refere wiki page for full list.

### Install from PyPI

```bash
pip install sbpyEmailWrapper
```

### Install from Source (GitHub)

```bash
git clone https://github.com/Shiftbytes-Opensource/sbpy-email-wrapper.git
cd sbpy-email-wrapper
pip install .
```

## Usage

After installation, you can use `EmailWrapper` to train a model and make predictions.

### Example: Instantiation

```python
from .wrapper import EmailWrapper

# Initialize the Wrapper
email_wrapper = EmailWrapper()

# Send simple email without attachment.
email_wrapper.sendMail(["bob@gmail.com", "jack@gmail.com"], "jill@gmail.com", "Hi From Jill!", "Happy to connect with you, Hope this email finds you well. Awaiting reposonse, Bye - Jill")

# See email status


```