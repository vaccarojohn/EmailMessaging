import sys
from main import sendMail

if __name__ == '__main__':
    if len(sys.argv) == 6:
        sendMail(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
        print("Email Message Sent Successfully!")
    else:
        print("Usage: python commandline.py [subject] [body] [from] [to] [password]")