[![Documentation Status](https://readthedocs.org/projects/ziwia/badge/?version=latest)](http://ziwia.readthedocs.io/en/latest/?badge=latest)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php)

# ziwia
Ziwia is an API client for Kraken cryptocurrency exchange website. Is supports the version 0 of the API as described on https://www.kraken.com/help/api. 

## Prerequisites

As of version 0.2, ziwia requires ``requests`` library.

```
> pip install requests
```

## Installation

See [Documentation](http://ziwia.readthedocs.io/en/latest/).

## Examples

Following code connects to your Kraken Account and returns your balance held in ZCASH.

```python
import ziwia

# Add your public and private keys
api = ziwia.Api("public-key", "private-key")
# Edit currency you use
balance = ziwia.private("Balance")["result"]["XZEC"]
# See all $ you have :)
print(balance)
```

Alternatively you can use new method introduced in version 0.2:

```python
import ziwia

# Create API client
api = ziwia.Api("public-key", "private-key")
# Get your account balance
balance = api.balance()
print(balance)
```
