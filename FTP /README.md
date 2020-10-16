# FTP Connector 
There are three types of FTP connections possible 

- FTP
Plain, unencrypted FTP that defaults over port 21. Most web browsers support basic FTP.

- FTPS
Implicit SSL/TLS encrypted FTP that works just like HTTPS. Security is enabled with SSL as soon as the connection starts. The default FTPS port is 990. This protocol was the first version of encrypted FTP available, and while considered deprecated, is still widely used. None of the major web browsers support FTPS.

- FTPES
Explicit FTP over SSL/TLS. This starts out as plain FTP over port 21, but through special FTP commands is upgraded to TLS/SSL encryption. This upgrade usually occurs before the user credentials are sent over the connection. FTPES is a somewhat newer form of encrypted FTP (although still over a decade old), and is considered the preferred way to establish encrypted connections because it can be more firewall friendly. None of the major web browsers support FTPES.