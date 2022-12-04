# MerossApi

This application provide REST API using flask to control your meross devices,
this application integrates the lastes meross-iot library.

With this app yuo can Load and Toggle your devices.

the authentication is guaranteed by a token, and the output is a json, so you
can implement you front-end tho manage your devices.

This is my first project in python, so please have a mercy on me! =)

in the future i will release a front-end, maybe in Vue or React, 
and improvements for the back-end .

Remind this is a work in progress project.

# Usage Examples

###  /auth route:
- Request type POST 
- in the body add:
{
    "user": "yourRealMerossEmailAccount@xxxx.xxx",
    "password": "YourPassword"
}
- This return the token for other HTTP request

### /loaddevices route:
- Request type GET
- in the body add:
[
    {"model":"mss710"},
    {"model":"mssXXX"}
]
- in Headers add: 
   - token='your token here'

### /toggleDevice route 
- Request type POST 
- in the body add:
[    
    {
        "deviceId": "20062807XXXX get from loaddevices",
        "enabled": false
    },
    {
        "deviceId": "220062807XXXX get from loaddevices",
        "enabled": false
    }
]
- in Headers add: 
   - token='your token here'

### /logout route:
in Headers add: 
   - token='your token here'

Enjoy



