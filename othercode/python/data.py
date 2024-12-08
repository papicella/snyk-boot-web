
# Simple example of sending and receiving values from Adafruit IO with the REST
# API client.
# Author: Tony Dicola, Justin Cooper

# https://github.com/adafruit/Adafruit_IO_Python/blob/ecefb29ad7a6080c1839c507abbcaef05d5e01d2/examples/api/data.py#L12

# Import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, Data, RequestError
import datetime

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'b780002b85d6411ca0ad9f9c60195f72'

ADAFRUIT_IO_KEY_2 = 'b780002b85d6411cb0ad9c9c60195f79'


SAMPLE_JWT = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'


SAMPLE_JWT_SPLIT = """eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"""


SAMPLE_JWT2 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2OTAzMzczNTEsImV4cCI6MTcyMTg3MzM1MSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSIsIkdpdmVuTmFtZSI6IkpvaG5ueSIsIlN1cm5hbWUiOiJSb2NrZXQiLCJFbWFpbCI6Impyb2NrZXRAZXhhbXBsZS5jb20iLCJSb2xlIjpbIk1hbmFnZXIiLCJQcm9qZWN0IEFkbWluaXN0cmF0b3IiXX0.gJVDcJwzAxbNjeaebn4v8PIv5QIs6tUxs2YU7zxIX84'

SAMPLE_JWT2_SPLIT = """eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.
eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2OTAzMzczNTEsImV4cCI6MTcyMTg3MzM1MSwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSIsIkdpdmVuTmFtZSI6IkpvaG5ueSIsIlN1cm5hbWUiOiJSb2NrZXQiLCJFbWFpbCI6Impyb2NrZXRAZXhhbXBsZS5jb20iLCJSb2xlIjpbIk1hbmFnZXIiLCJQcm9qZWN0IEFkbWluaXN0cmF0b3IiXX0.
gJVDcJwzAxbNjeaebn4v8PIv5QIs6tUxs2YU7zxIX84"""


# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'YOUR_AIO_USERNAME'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
try:
    temperature = aio.feeds('temperature')
except RequestError:
    feed = Feed(name="temperature")
    temperature = aio.create_feed(feed)

#
# Adding data
#

aio.send_data(temperature.key, 42)
# works the same as send now
aio.append(temperature.key, 42)

# setup batch data with custom created_at values
yesterday = (datetime.datetime.today() - datetime.timedelta(1)).isoformat()
today = datetime.datetime.now().isoformat()
data_list = [Data(value=50, created_at=today), Data(value=33, created_at=yesterday)]
# send batch data
aio.send_batch_data(temperature.key, data_list)

#
# Retrieving data
#

data = aio.receive_next(temperature.key)
print(data)

data = aio.receive(temperature.key)
print(data)

data = aio.receive_previous(temperature.key)
print(data)