# https://uk.mathworks.com/help/thingspeak/use-raspberry-pi-board-that-runs-python-websockets-to-publish-to-a-channel.html


# Include the libraries paho.mqtt.publish as publish, psutil, and string in your Python code.
import paho.mqtt.publish as publish
import psutil
import string
import credentials


# Define the variables for communicating with ThingSpeak. Edit the channel ID and MQTT device credentials.

# The ThingSpeak Channel ID.
# channel_ID = '<YOUR-CHANNEL-ID>'
# include in credentials.py

# The hostname of the ThingSpeak MQTT broker.
mqtt_host = 'mqtt3.thingspeak.com'

# Your MQTT credentials for the device
# mqtt_client_ID = '<YOUR-CLIENT-ID>'
# mqtt_username  = '<YOUR-USERNAME>'
# mqtt_password  = '<YOUR-MQTT-PASSWORD>'
# include in cradentials.py


# Define the connection type as websockets, and set the port to 80.

t_transport = 'websockets'
t_port = 80


# Create a topic string in the form shown in Publish to a Channel Feed that updates field 1 and field 2 of the specified channel simultaneously.

# Create the topic string.
topic = 'channels/' + credentials.channel_ID + '/publish'


# Run a loop that calculates the system RAM and CPU performance every 20 seconds and publishes the calculated values. Publish to fields 1 and 2 of the specified channel simultaneously using WebSockets.

def thinSpeakWrite(adjusted_CPM):

    # build the payload string.
    payload = 'field1=' + str(adjusted_CPM) # + '&field2=' + str(example2)

    # attempt to publish this data to the topic.
    try:
        # print ("Writing Payload = ', payload,' to host: ', mqtt_host, ' clientID= ', credentials.mqtt_client_ID, ' User ', credentials.mqtt_username, ' PWD ', credentials.mqtt_password)
        publish.single(topic, payload, hostname=mqtt_host, transport=t_transport, port=t_port, client_id=credentials.mqtt_client_ID, auth={'username':credentials.mqtt_username,'password':credentials.mqtt_password})
    except KeyboardInterrupt:
        print('pff...')
    except Exception as e:
        print (e)


# Run the program and watch the channel for regular updates from your device.