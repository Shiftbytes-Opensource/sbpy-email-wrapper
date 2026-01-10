from setuptools import setup, find_packages

setup(
    name="sbpyEmailWrapper",
    version="0.0.1",
    description=(
        "This project is aimed to simplify email integration in applications. "
        "This library / wrapper is written for python projects. "
        "This wrapper supports most popular email services such as AWS SES, Mailgun, etc. "
        "Refer wiki page for full list."
    ),
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Sreenath",
    author_email="sreenath@shiftbytes.co.in",
    license="GPL-3.0-only",
    python_requires=">=3.10",
    install_requires=[
        "boto3>=1.42.24",
    ],
    packages=find_packages(),
    url="https://github.com/Shiftbytes-Opensource/sbpy-email-wrapper",
    include_package_data=True,
)