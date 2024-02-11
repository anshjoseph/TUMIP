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
