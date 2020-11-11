# OKEx Client

Python client for OKEx API.

Original code from
https://github.com/okex/V3-Open-API-SDK/tree/master/okex-python-sdk-api


### How to use?

`python version: 3.6+`

`WebSocketAPI: The recommended websockets library version is 6.0`


#### Step 1: Download SDK, install related required libraries

1.1 Download `python SDK`
* Move the SDK directory `Clone` or `Download` to the local, choose to use ʻokex-python-sdk-api`

1.2 Install required libraries
```python
pip install requests
pip install websockets==6.0
```


#### Step 2: Configure personal information

2.1 If there is no API yet, you can [click](https://www.okex.com/account/users/myApi) to apply on the official website

2.2 Fill in various information in ʻexample.py (RestAPI)` and `websocket_example.py (WebSocketAPI)`
```python
api_key = ""
secret_key = ""
passphrase = ""
```


#### Step 3: Call the interface

* RestAPI
    
    * Run ʻexample.py`
    
    * Untie the comment of the corresponding method, pass the parameter and call each interface
    
* WebSocketAPI
    
    * Run `websocket_example.py`
        
    * Select the corresponding startup method according to the personal/public channel, and uncomment the corresponding channel
    
    ```python
    # Public data does not need to log in (markets, candlesticks, transaction data, capital rate, price limit range, depth data, marked prices and other channels)
    loop.run_until_complete(subscribe_without_login(url, channels))
    
    # Personal data requires login (user accounts, user transactions, user positions, etc. channels)
    loop.run_until_complete(subscribe(url, api_key, passphrase, secret_key, channels))
    ```

postscript:

* If you don’t know the API yet, it is recommended to refer to the official OKEx [API document](https://www.okex.com/docs/zh/)

* If you encounter problems with `WebSocketAPI`, please refer to the relevant link

    * ʻAsyncio`, `websockets` document/`github`:
    
            https://docs.python.org/3/library/asyncio-dev.html
            https://websockets.readthedocs.io/en/stable/intro.html
            https://github.com/aaugustin/websockets
    
    * About `code=1006`:
    
            https://github.com/Rapptz/discord.py/issues/1996
            https://github.com/aaugustin/websockets/issues/587
