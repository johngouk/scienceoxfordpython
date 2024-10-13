"""

    Demonstrates an alternative LogRecord that allows the (msecs) param to work
    and relies on the micropython-lib version of time.py that includes strftime()

"""

import logging, ntptime, network
from NetworkCredentials import NetworkCredentials
from ESPLogRecord import ESPLogRecord

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)06d %(levelname)s - %(name)s - %(message)s')
logger = logging.getLogger('MyName')

logger.info('Connecting to AP...')
logger.info('Note that the time hasn\'t been set yet...')
w = network.WLAN(network.STA_IF)
w.active(True)
w.connect(NetworkCredentials.ssid, NetworkCredentials.password)
while not (w.isconnected()):
    pass
ipaddr = w.ifconfig()[0]
print('Connected! IP: ' + ipaddr)   # Need this to connect!!
print('Hostname:', network.hostname())
print('Setting network time...')
logger.info('Setting time...')
ntptime.settime()
logger.info('And now it has!')

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
logger.setLevel(logging.INFO)
print('\nlogging level at INFO - no DEBUG shown')
sendMessages()

logger.setLevel(logging.ERROR)
print('\nlogging level at ERROR - only ERROR messages shown')
sendMessages()

print('\nLet\'s change the LogRecord to one that sets up msecs correctly, and try again')
logger.record = ESPLogRecord()
logger.setLevel(logging.DEBUG)
print('Logging level at DEBUG...')
sendMessages()

logger.setLevel(logging.INFO)
print('\nlogging level at INFO - no DEBUG shown')
sendMessages()

logger.setLevel(logging.ERROR)
logging.basicConfig(level=logging.ERROR, force=True, format='%(asctime)s.%(msecs)06d %(levelname)s - %(name)s - %(message)s')
print('\nlogging level at ERROR - only ERROR messages shown')
sendMessages()
