import logging
import sys


class ExpenditureFeedGeneration(object):
    """ Generate expenditure feeds as a service. """
    def __init__(self):
        """ Instantiate the class logger. """
        handler = logging.StreamHandler(stream=sys.stdout)
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level='DEBUG')
        self.logger.addHandler(handler)

    def start(self):
        """ Start the expenditure feed generation service.

        Currently, "starting" the expenditure feed generation service simply
        logs a message to stdout indicating (falsely) that the service has
        started. In the future, I'd like to adjust this so that the service
        sets up the appropriate exchanges, queues and binds, waits for a
        message to say the feed should be generated, generates the feed and
        then sends a message to say the feed has been generated.

        Usage::

        >>> import services
        >>> service = services.ExpenditureFeedGeneration()
        >>> service.start()
        The expenditure feed generation service has started successfully.

        """
        self.logger.info('The expenditure feed generation service has started successfully.')
