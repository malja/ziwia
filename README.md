[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# ziwia
Ziwia is an API client for Kraken cryptocurrency exchange website. Is supports the version 0 of the API as described on https://www.kraken.com/help/api. 

## Prerequisites

As of version 0.2, ziwia requires ``requests`` library.

```
> pip install requests
```

## Installation

See [Documentation](http://readthedocs.io).

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
