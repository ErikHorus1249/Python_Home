import socket # import socket lib
from requests  import get# pip3 install requests


hostName = socket.gethostname() # phuong thuc lay host name
local_ip = socket.gethostbyname(hostName) # phuong thuc lay dia chi IP qua hostName
public_ip = get('https://api.ipify.org').text


# display
print(f"Host name :{hostName}") 
print(f"Local Ip : {local_ip}")
print(f"Public Ip : {public_ip}")
