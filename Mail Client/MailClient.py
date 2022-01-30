import base64
import ssl
from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

MailFrom = "mobile.network.proje@gmail.com"
RcptMail = "karakasdilara1@gmail.com"
password = "dilaramobile123"

# Choose a mail server (e.g. Google mail server) and call it mailserver
# Fill in start
mailserver = ("smtp.gmail.com", 587)
# Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
# Fill in end

recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command then print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Start TLS
tls = 'starttls\r\n'
clientSocket.send(tls.encode())
recvTls = clientSocket.recv(1024)
print(recvTls)
if recvTls[:3] != '220':
    print('220 reply not received from server.')

# Secure Sockets Layer (SSL)
WrapClientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)
# Send Auth login
WrapClientSocket.send(('AUTH LOGIN\r\n').encode())
recvAuthLogin = WrapClientSocket.recv(1024)
print("Recv Auth Login: ", recvAuthLogin.decode())
if recvAuthLogin[:3] != '334':
    print('334 reply not received from server.')

# Send mail
WrapClientSocket.send((base64.b64encode(MailFrom.encode()))+('\r\n').encode())
recvMail = WrapClientSocket.recv(1024)
print("Recv Send Mail: ", recvMail.decode())
if recvMail[:3] != '334':
    print('334 reply not received from server.')

# Send password
WrapClientSocket.send((base64.b64encode(password.encode()))+('\r\n').encode())
recvPassword = WrapClientSocket.recv(1024)
print("Recv Send Password: ", recvPassword.decode())
if recvPassword[:3] != '235':
    print('235 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = "MAIL FROM: <"+MailFrom+"> \r\n"
WrapClientSocket.send(mailFrom.encode())
recvMailFrom = WrapClientSocket.recv(1024)
print("Recv Mail From: ", recvMailFrom)
if recvMailFrom[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptMail = "RCPT TO: <"+RcptMail+"> \r\n"
WrapClientSocket.send(rcptMail.encode())
recvRCPTMail = WrapClientSocket.recv(1024)
print("Recv RCPT Mail: ", recvRCPTMail)
if recvRCPTMail[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send DATA command and print server response.
# Fill in start
data = "DATA\r\n"
WrapClientSocket.send(data.encode())
recvData = WrapClientSocket.recv(1024)
print("Recv Data: ", recvData)
if recvData[:3] != '354':
    print('354 reply not received from server.')
# Fill in end

# Send message data.
# Fill in start
message = "SUBJECT: SMTP Mail Client Test \r\n\r\n" + msg
WrapClientSocket.send(("From: "+MailFrom + '\r\n').encode())
WrapClientSocket.send(("To: "+RcptMail + '\r\n').encode())
WrapClientSocket.send(message.encode())
WrapClientSocket.send(endmsg.encode())
recvSendMessage = WrapClientSocket.recv(1024)
print("Recv Send Message: ", recvSendMessage)
if recvSendMessage[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
WrapClientSocket.send("QUIT\r\n".encode())
recvQuit = WrapClientSocket.recv(1024)
print("Recv Quit: ", recvQuit)
if recvQuit[:3] != '221':
    print('221 reply not received from server.')
WrapClientSocket.close()
# Fill in end