# MerossApi

This application provide REST API using flask to control your meross devices,
this application integrates the latest meross-iot library.

With this app you can Load and Toggle your devices with multiple accounts at the same time.

The authentication is guaranteed by a token, and the output is a json, so you
can implement your custom front-end to manage your devices.

This is my first project in python, so please have a mercy on me! =)

in the future i will release a front-end, maybe in Vue or React, 
and improvements for the back-end.

Remind this is a work in progress project.

# Routes usage examples

###  localhost:4449/auth:
- Request type ****[POST]****
- In the body add:
``` json
{
    "user": "yourRealMerossEmailAccount@xxxx.xxx",
    "password": "YourPassword"
}
```
****Return a token****
``` json 
{"token":"k782qW65U6sUyCqHACorMjAIcw-Xt9tAIxCr4VhkuLofmhy80lwfd"}
```

### localhost:4449/loaddevices:
- Request type ****[GET]****
- In the body add filters:
``` json 
[
    {"model":"mss710"},
    {"model":"mssXXX"}
]
```
- In the headers add: 
``` json 
{"token":"k782qW65U6sUyCqHACorMjAIcw-Xt9tAIxCr4VhkuLofmhy80lwfd"}
```

****Return a list of devices:****
``` json 
[
    {
        "deviceName": "Luci Platani",
        "deviceUid": "2006XXXXXXXX",
        "firmwareVersion": "3.1.6",
        "hardwareVersion": "3.0.0",
        "model": "mss710",
        "status": "ONLINE"
    },
    {
        "deviceName": "Luce Ufficio Dx",
        "deviceUid": "2006XXXXXXXX",
        "firmwareVersion": "3.1.6",
        "hardwareVersion": "3.0.0",
        "model": "mss710",
        "status": "ONLINE"
    },
    {
        "deviceName": "Luce Ufficio Sx",
        "deviceUid": "2006XXXXXXXX",
        "firmwareVersion": "3.1.6",
        "hardwareVersion": "3.0.0",
        "model": "mss710",
        "status": "ONLINE"
    }
]
```

### localhost:4449/toggledevice 
- Request type ****[POST]****
- In the body add filters:
``` json 
[    
    {
        "deviceId": "2006XXXXXXXX",
        "enabled": false
    },
    {
        "deviceId": "22006XXXXXXXX",
        "enabled": true
    }
]
```

- In the headers add: 
``` json 
   {"token":"k782qW65U6sUyCqHACorMjAIcw-Xt9tAIxCr4VhkuLofmhy80lwfd"}
``` 

****Return a list of enabled device id:****
``` json 
[
    "2006XXXXXXXX",
    "2006XXXXXXXX"
]
```

### localhost:4449/logout:
- Request type ****[GET]****

- In the headers add: 
``` json
   {"token":"k782qW65U6sUyCqHACorMjAIcw-Xt9tAIxCr4VhkuLofmhy80lwfd"}
```





