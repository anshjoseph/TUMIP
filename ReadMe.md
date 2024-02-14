# [TCP/UDP Multimedia Interaction Protocol (TUMIP)]
Motive:- build for tranmitting the video frame and processing user chat at same

## Registration Process(TCP)
Payload 
-  Request: 
```
        <--------------user_id(32)-------------->
        <-req type(8)-><-Flag-><-frame size(16)->
```
-  Response: 
```
        <--------------user_id(32)-------------->
        <-awk type(8)-><-Flag-><--UDP PORT(16)-->
```



## Chat With BOT
Payload Header(size 32 bits)
- Request: 
```
        <--------------user_id(32)-------------->
        <-req type(8)-><-Flag-><--Data Len(16)-->
        <----------------Data------------------->
```
- Response:
```
        <--------------user_id(32)-------------->
        <-awk type(8)-><-Flag-><--Data Len(16)-->
        <----------------Data------------------->
```
## Request 
<table>
        <tr>
                <tH>Req</tH>
                <tH>Flag</tH>
                <th>Des</th>
        </tr>
        <tr>
                <td>0000 0001</td>
                <td>0000 0000</td>
                <td>you have to this request at time of connection</td>
        </tr>
        <tr>
                <td>0000 0011</td>
                <td>0000 0000</td>
                <td>you have to this request at time of sending question to chat bot</td>
        </tr>
</table>

## Acknowledge
<table>
        <tr>
                <tH>Awk</tH>
                <tH>Flag</tH>
                <th>Des</th>
        </tr>
        <tr>
                <td>0000 0001</td>
                <td>0000 0000</td>
                <td>You req. this flag when your request is accepted by the server</td>
        </tr>
        <tr>
                <td>0000 0001</td>
                <td>0001 0000</td>
                <td>You req. this flag when your request is rejected by the server</td>
        </tr>
        <tr>
                <td>0000 0011</td>
                <td>0000 0000</td>
                <td>chat bot response succeful</td>
        </tr>
        <tr>
                <td>0000 0011</td>
                <td>0001 0000</td>
                <td>chat bot response fail</td>
        </tr>
</table>


## Note
-   use jpeg compression for sending images to the server MAX size is 230x230x3

## Code For Interacting
```python
import socket
import numpy as np
import pickle
from random import randint
import cv2
import os 

_payload = (np.array([[[randint(0,255),randint(0,255),randint(0,255)]for __ in range(230)] for _ in range(230)]))

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 4123  # The port used by the server

def getCompress(payload) ->bytes:
    path = f'temp.jpeg'
    cv2.imwrite(path,payload)
    with open(path,'rb') as file:
        ret = file.read()
    os.remove(path)
    return ret

def getPort(payload):
    return payload & 2**16 -1

# TESTING for video UDP and TCP port reg..
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = 1 << 64
    data1 = data | 32 << 32
    data2 = data1 | 1 << 24
    data3 = data2 | 0 << 16
    data4 = data3 | 128*128
    payload = data4.to_bytes(9,'big')
    print(payload)
    s.send(payload)
    data = s.recv(8024)
    count = 1
    while True:
        print(f"Received {(int.from_bytes(data,byteorder='big'))}")
        UDP_PORT = getPort(int.from_bytes(data,byteorder='big'))
        print(UDP_PORT)
        MESSAGE = getCompress(_payload)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
        sock.sendto(MESSAGE, (HOST, UDP_PORT))
        if count == 10:
            break
        count += 1
    s.close()

def dataExtractor(payload):
    header:bytes = int.from_bytes(payload[:9],'big')
    user_id = header >> 32 & 2**32 -1
    req,flag,com = (header & 2**32-1) >> 24  ,((header & 2**32-1) >> 16) & 2**8 - 1, (header & 2**32-1) & 2**16 - 1
    data:bytes = payload[9:]
    return data
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = 1 << 64
    data1 = data | 32 << 32
    data2 = data1 | 3 << 24
    data3 = data2 | 0 << 16
    data4 = data3 | 128*128
    payload = data4.to_bytes(9,'big')
    message = b'hello wordl i am R Ansh Joseph'
    payload += message
    print(payload)
    s.send(payload)
    data = s.recv(8024)
    print(dataExtractor(data))       
```