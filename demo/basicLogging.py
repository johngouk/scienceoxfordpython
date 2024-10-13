import logging

# Setup logging level
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('MyName') # Get a logger, with a name for the (name) parameter


def sendMessages():
    print('INFO level...')
    logger.info('This is an INFO level message')
    print('DEBUG level...')
    logger.debug('This is a DEBUG level message')
    print('ERROR level...')
    logger.error('This is an ERROR level message')

print('Logging level at DEBUG...')
sendMessages()

# Have to use force = TRUE to override the initial setting
# Note: if you provided other config values e.g. filename, format that are non-default,
# they must be provided again in this command
logging.basicConfig(level=logging.INFO, force=True)
print('\nlogging level at INFO - no DEBUG shown')
sendMessages()

# Have to use force = TRUE to override the initial setting
logging.basicConfig(level=logging.ERROR, force=True)
print('\nlogging level at ERROR - only ERROR messages shown')
sendMessages()

# Much more time info - but does it work fully?
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)06d %(levelname)s - %(name)s - %(message)s', force=True)
print('Logging level at DEBUG with time info')
sendMessages()

# Check betterLogging.py for improved time accuracy to millisecs