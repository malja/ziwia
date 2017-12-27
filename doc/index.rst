ziwia documentation
=====================

`ZIWIA <https://github.com/malja/ziwia>`_ is an API client for Kraken Bitcoin exchange site. It fully supports version 0 of Kraken's API. Main goal of
this project is to make it as easy as possible to contact Kraken, get information you need and return data in readable
format.

**WARNING**: At the moment, ziwia is still in early development stage. I would really appreciate any bug report or idea how to improve it.

Features:

    - Data returned as JSON.
    - Parameters are checked before connection.
    - Proxy support.

Requires:

Ziwia requires ``requests`` library to work properly. See: :ref:`installation`.

User guide
----------

.. toctree::
    :maxdepth: 2

    installation
    basic_usage
    reference
    todo

Reference
---------

.. autosummary::
    :nosignatures:

    ziwia.Api
    ziwia.Api.__init__
    ziwia.Api.public
    ziwia.Api.time
    ziwia.Api.assets
    ziwia.Api.asset_pairs
    ziwia.Api.ticker
    ziwia.Api.ohlc
    ziwia.Api.depth
    ziwia.Api.trades
    ziwia.Api.spread
    ziwia.Api.private
    ziwia.Api.balance
    ziwia.Api.trade_balance
    ziwia.Api.open_orders
    ziwia.Api.closed_orders
    ziwia.Api.query_orders
    ziwia.Api.trades_history
    ziwia.Api.query_trades
    ziwia.Api.open_positions
    ziwia.Api.ledgers
    ziwia.Api.query_ledgers
    ziwia.Api.trade_volume
    ziwia.Api.add_order
    ziwia.Api.cancel_order


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`