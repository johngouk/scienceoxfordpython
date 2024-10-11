import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(name)s - %(message)s')
logger = logging.getLogger('MyName')


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
logging.basicConfig(level=logging.INFO, force=True)
print('\nlogging level at INFO - no DEBUG shown')
sendMessages()

logging.basicConfig(level=logging.ERROR, force=True)
print('\nlogging level at ERROR - only ERROR messages shown')
sendMessages()



logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)06d %(levelname)s - %(name)s - %(message)s')
