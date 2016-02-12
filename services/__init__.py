"""
A collection of APIs.

Services is a library of services used throughout the trackerSpend application.
Although the intent of each service differs, the wrapping infrastructure is
consistent across the library. The basic usage is as follows:

    >>> import services
    >>> service = services.ExampleService()
    >>> service.start()
    The example service has started successfully.

The intention is that the usage of each service can be understood using
Python's help function. To ensure this is the case, a best-practice guide will
be developed along side this library and will cover architectural rules to
follow when contributing to this library. The guide can be found at:

http://trackerspend.readthedocs.org/en/latest/best_practice/services/

"""

__version__ = '0.1'
__author__ = 'Jacob Gillespie'

from .expenditure_feed_generation import ExpenditureFeedGeneration
