.. _basic_usage:

===========
Basic Usage
===========

Install ziwia package as described in :ref:`installation`.

After successful installation, import ziwia into your project.

.. code-block:: python

    import ziwia

    api = ziwia.Api()
    server_time = api.time()
    print( server_time["unixtime"] )

This example shows simple API call to public Kraken API. Public API means, you do not have to authorize yourself with 
private and public API key. Data accessible in public API is mostly about server.

We create an API class instance. You will always start API calls with this line. Next, we call :py:meth:`ziwia.Api.time`
which connects to Kraken API and returns server time in two formats. First one is `Unix timestamp <https://en.wikipedia.org/wiki/Unix_time>`_
and the second one is `RFC 1123 <http://freesoft.org/CIE/RFC/1945/14.htm>`_.

Last line just prints out server time as unix timestamp. 

**Note:** Beside :py:meth:`ziwia.Api.time`, every API address Kraken exposes has its corresponding method in ziwia. For example address
*/0/public/Ticker* is mapped to :py:meth:`ziwia.Api.ticker` method. 
As you can see, method name is made up of the part after last slash in address. Name is all lower-case and if address contains more than
one word, words are separated by underscore. For example */0/public/AssetPairs* translates as :py:meth:`ziwia.Api.asset_pairs`.

Private and public
------------------

Kraken API is divided into two sections - public and private. Public API is accessible without any authorization and
limits.

For accessing private API, you have to provide your private and public API keys. They should be passed as parameters to :py:class:`ziwia.Api` constructor.

.. code-block:: python

    import ziwia

    api = ziwia.Api( "public_key", "private_key" )
    print( api.balance() )

This code retrives your account balance. To use it, change ``public_key`` and ``private_key`` to keys from your Kraken
Account settings.

Timeout and proxy
-----------------

Since version 0.2, ziwia supports proxy settings. All you have to do is to pass HTTP and HTTPS specific settings to
fourth parameter of :py:class:`ziwia.Api` constructor.

.. code-block:: python

    import ziwia

    proxy = {
        "http": "your_proxy",
        "https": "hattps_proxy"
    }

    api = ziwia.Api( "public_key", "private_key", 30, proxy )

The third parameter is number of seconds before timeout.
