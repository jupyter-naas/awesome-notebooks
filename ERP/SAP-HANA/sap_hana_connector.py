import sys

from hdbcli import dbapi
print("trying to connect")
connection = dbapi.connect('182.18.156.155', 30015, 'JPAK2', 'jp@P@ssw0rd@2020')

#This statement prints true if the connection is successfully established
print(connection.isconnected())
