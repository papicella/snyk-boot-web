
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