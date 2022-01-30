# Mobile Comminication Network Project

## Web Server

A simple Web server was developed in Python that can only process one request. Specifically, the Web server will (i) create a connection socket when connected by a client (browser); (ii) receive the HTTP request from that connection; (iii) parse the request to identify the specific file requested; (iv) retrieve the requested file from the server's file system; (v) generating an HTTP response message consisting of the requested file preceded by the header lines; and (vi) response sent over TCP connection to the requesting browser. If a browser requests a file that is not on the server, the server returns a "404 Not Found" error message.
