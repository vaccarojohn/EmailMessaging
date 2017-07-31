# EmailMessaging
This package provides a command line interface for sending emails via Gmail's SMTP server. It also provides a Python and C# method to send emails.

This package will only work with emails provided through Gmail.

Remember to sign in to your account and then go to [this](https://myaccount.google.com/lesssecureapps?pli=1) link to allow less secure apps to access your email.

## How To Use (Windows):
- Clone this repository to your computer
- OPTIONAL: Add the win32 directory to your PATH enviornment variable. Now, this command line script may be executed from any directory.
- If you did not add the win32 directory to your PATH, navigate to the win32 directory.
- Execute the following command: sendMail [subject] [body] [from] [to] [password]
- EXAMPLE: sendMail "test" "This is a test." "me@gmail.com" "you@example.com" "mygmailpassword"


## How To Use (Unix):
- Install python if you don't already have it
- Clone this repository to your computer
- Navigate to the python directory
- Execute the following command: python commandline.py [subject] [body] [from] [to] [password]
- EXAMPLE: python commandline.py "test" "This is a test." "me@gmail.com" "you@example.com" "mygmailpassword"

## How To Import The Python Script Into Your Another Python Package (For Use In Your Python Applications):
- Clone this repository to your computer
- Copy the file "main.py" into your python application
- Import the sendMail function from "main.py" by using the following python syntax: 
```python
from main import sendMail
```

## How To Use The C# Script:
- Clone this repository to your computer
- Copy the DLL compiled for the version of .NET corresponding to your project into your project's references
- Add the following "using" statement to your code: 
```c#
using Email;
```
- To send an email, first declare an email message object with the following syntax: 
```c#
EmailMessage message = new EmailMessage('subject', 'body', 'from', 'to', 'password');
```
- Send the message with:
```c#
message.Send();
```
- Or if you are using .NET 5+, you can send the message with await:
```c#
await message.SendAsync();
```
