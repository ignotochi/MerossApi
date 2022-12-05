# MerossApi

This application provide REST API using flask to control your meross devices,
this application integrates the latest meross-iot library.

With this app you can Load and Toggle your devices.

The authentication is guaranteed by a token, and the output is a json, so you
can implement you front-end to manage your devices.

This is my first project in python, so please have a mercy on me! =)

in the future i will release a front-end, maybe in Vue or React, 
and improvements for the back-end.

Remind this is a work in progress project.

# Routes usage examples

###  localhost:4449/auth:
- Request type ****[POST]****
- in the body add:
``` json
{
    "user": "yourRealMerossEmailAccount@xxxx.xxx",
    "password": "YourPassword"
}
```
****Return a token****
``` json 
"k782qW65U6sUyCqHACorMjAIcw-Xt9tAIxCr4VhkuLofmhy80lwfd"
```

### localhost:4449/loaddevices:
- Request type ****[GET]****
- In the body add:
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
        "deviceUid": "20062805773015",
        "firmwareVersion": "3.1.6",
        "hardwareVersion": "3.0.0",
        "model": "mss710",
        "status": "ONLINE"
    },
    {
        "deviceName": "Luce Ufficio Dx",
        "deviceUid": "20062807349678258",
        "firmwareVersion": "3.1.6",
        "hardwareVersion": "3.0.0",
        "model": "mss710",
        "status": "ONLINE"
    },
    {
        "deviceName": "Luce Ufficio Sx",
        "deviceUid": "2006284947008625",
        "firmwareVersion": "3.1.6",
        "hardwareVersion": "3.0.0",
        "model": "mss710",
        "status": "ONLINE"
    }
]
```

![Red text]### localhost:4449/toggledevice 
- Request type ****[POST]****
- In the body add:
``` json 
[    
    {
        "deviceId": "20062807XXXX",
        "enabled": false
    },
    {
        "deviceId": "220062807XXXX",
        "enabled": true
    }
]
```

- In the headers add: 
``` json 
   {"token":"k782qW65U6sUyCqHACorMjAIcw-Xt9tAIxCr4VhkuLofmhy80lwfd"}
``` 

****Return a list of enabled/disabled device id:****
``` json 
[
    "20062807349678258h1",
    "20062849470086258h1"
]
```

### localhost:4449/logout:
- Request type ****[GET]****

- In the headers add: 
``` json
   {"token":"k782qW65U6sUyCqHACorMjAIcw-Xt9tAIxCr4VhkuLofmhy80lwfd"}
```





