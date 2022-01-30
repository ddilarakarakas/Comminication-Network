# Mobile Comminication Network Project

## Web Server

A simple Web server was developed in Python that can only process one request. Specifically, the Web server will (i) create a connection socket when connected by a client (browser); (ii) receive the HTTP request from that connection; (iii) parse the request to identify the specific file requested; (iv) retrieve the requested file from the server's file system; (v) generating an HTTP response message consisting of the requested file preceded by the header lines; and (vi) response sent over TCP connection to the requesting browser. If a browser requests a file that is not on the server, the server returns a "404 Not Found" error message.

## UDP Pinger

In this part, a client ping program was written in Python. The client will send a simple ping message to a server, receive a corresponding pong message from the server, and determine the delay (Round Trip Time - RTT) between the client sending the ping message and receiving the pong message. The functionality provided by the client and server is similar to the functionality provided by the standard ping program found in modern operating systems. However, standard ping programs use the Internet Control Message Protocol (ICMP). A non-standard (but simple!) UDP-based ping program is created here.
The ping program is to send 10 ping messages to the target server over UDP. For each message, your client will determine and print the RTT when the corresponding pong message is returned. Because UDP is an unreliable protocol, a packet sent by a client or server may be lost. Therefore, the client cannot wait indefinitely for a response to a ping message. It should make the client wait about a second for a response from the server; If no reply is received, the customer should assume that the package is lost and print a message accordingly.

## Mail Client

The purpose of this program is to create a simple mail client that sends email to any recipient. The client needs to establish a TCP connection with a mail server (for example, a Google mail server), establish a dialog with the mail server using the SMTP protocol, send an email message to a recipient via the mail server, and finally close the TCP connection with the mail server.
