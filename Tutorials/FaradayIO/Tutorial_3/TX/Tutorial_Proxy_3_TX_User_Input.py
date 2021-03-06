#Imports - General

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../../")) #Append path to common tutorial FaradayIO module

#Imports - Faraday Specific
from FaradayIO import faradaybasicproxyio
from FaradayIO import faradaycommands


#Variables
local_device_callsign = 'kb1lqd'
local_device_node_id = 7
transmit_proxy_flask_port = 8099

#Start the proxy server after configuring the configuration file correctly
#Setup a Faraday IO object
faraday_1 = faradaybasicproxyio.proxyio(transmit_proxy_flask_port)
faraday_cmd = faradaycommands.FaradayCommands()
#faraday_parser = telemetryparser.TelemetryParse()

# This example will show how to command Faraday using the basic command application.
# Make sure to turn UART TELEM BOOT Bitmask to 0 to turn OFF telemetry update automatically


##############
## TOGGLE Remote Device ++GPIO
##############

#Remote device information
remote_callsign = 'KB1LQC' #case independant
remote_id = 1

#NOTE: This TX program MUST operate on a different proxy TCP port than RX

#Use the predefined experimental message command (singled packet) function to send an RF message to a remote unit
#general_command.SendRfMsgExperimental('kb1lqd', 23, "Testing This Message 1!")

user_input = ''

while(user_input != "quit"):
    user_input = raw_input("Text To Transmit:")
    command = faraday_cmd.CommandLocalExperimentalRfPacketForward(remote_callsign, remote_id, str(user_input))
    print "Transmitting message:", user_input
    faraday_1.POST(local_device_callsign, local_device_node_id, faraday_1.CMD_UART_PORT, command)

##message = "Testing RF Packet 1"
##command = faraday_cmd.CommandLocalExperimentalRfPacketForward(remote_callsign, remote_id, message)
##print "Transmitting message:", message
##faraday_1.POST(local_device_callsign, local_device_node_id, faraday_1.CMD_UART_PORT, command)
##
##message = "Testing RF Packet 2"
##command = faraday_cmd.CommandLocalExperimentalRfPacketForward(remote_callsign, remote_id, message)
##print "Transmitting message:", message
##faraday_1.POST(local_device_callsign, local_device_node_id, faraday_1.CMD_UART_PORT, command)
###Uncomment to send multiple concecutive messages!
##general_command.SendRfMsgExperimental('kb1lqd', 23, "Testing This Message 2!")
##general_command.SendRfMsgExperimental('kb1lqd', 23, "Testing This Message 3!")
##general_command.SendRfMsgExperimental('kb1lqd', 23, "Testing This Message 4!")
##general_command.SendRfMsgExperimental('kb1lqd', 23, "Testing This Message 5!")
