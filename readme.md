# Messpusher
A lightweight Python tool for sending messages

## Support
- ✅ [PushPlus](http://www.pushplus.plus/)
- comming soon

## Installation
``` bash
uv pip install .
```

## Requirements
- python 3.7+
- requests

## Usage
### Step 1: Configure
Create a config dictionary
``` python
config = {
    "pushplus": {
        "token": "your_pushplus_token_here"
    }
}
```
### Step 2: Send message
``` python
from messpusher import Messpusher

mp = Messpusher(config)
mp.send_all("Test Title", "This is a test message from messpusher.")
```