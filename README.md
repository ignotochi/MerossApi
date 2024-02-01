# MerossApi

Welcome to **MerossApi** - your gateway to controlling Meross devices using a REST API built with Flask. 
This application seamlessly integrates the latest meross-iot library, providing you with the power to load and toggle your devices with multiple accounts simultaneously.

## Features

- **Multi-Account Control:** Effortlessly manage your Meross devices with multiple accounts concurrently.
- **Token-based Authentication:** Security is paramount. This application ensures authentication through tokens, keeping your devices and data safe.
- **JSON Output:** The application outputs data in JSON format, allowing you to implement a custom front-end for a personalized device management experience.

**Note:** This is my inaugural Python project, so your understanding and mercy are greatly appreciated! 😊 
I have plans to release a front-end, possibly using Vue or React, along with ongoing improvements to the back-end.

**Project Status:** Work in progress. Expect exciting updates and enhancements in the future!

## Installation

To get started with MerossApi, follow these steps:

1. **Install python:**

   see [see Python Downloads for Windows](https://www.python.org/downloads/windows/)

3. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/MerossApi.git
   cd MerossApi

4. **Install Dependencies:**

   ```bash 
   pip install -r requirements.txt

5. **Running the Application**
    Once you've completed the installation, running MerossApi is a breeze:
   
   ```python
    python main.py

This will start the Flask development server, and you'll be ready to interact with your Meross devices through the provided API.

Note: For production use, consider deploying with a production-ready server like Gunicorn or uWSGI.

Feel free to explore, contribute, and provide feedback! Together, we'll shape the future of MerossApi.

Feel free to customize this README further to suit your project's specific needs and style!

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





