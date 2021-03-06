import struct

class TelemetryParse(object):
    def __init__(self):
        self.datagram_struct = struct.Struct('>3B 118s 1H') #Struct format definition for the generice telemetry packet format datagram
        self.flash_config_info_d_struct = struct.Struct('<1B 9s 5B 9x 4B 21x 9s 1s 10s 1s 8s 1s 1B 21x 1B 2H 10x')
        self.flash_config_info_d_struct_len = 116
        self.packet_1_struct = struct.Struct('4B')
        self.packet_1_len = 4
        self.packet_2_struct = struct.Struct('<1H 12B')
        self.packet_2_len = 14
        self.packet_3_struct = struct.Struct('>9s 2B 9s 8B 1H 9s 1s 10s 1s 8s 1s 5s 1c 4s 3B 9H 2B 2H')
        self.packet_3_len = 97


    def UnpackDatagram(self, packet, debug):
        """
        Unpacks a telemetry datagram from the raw packet supplied in the function argument. The raw unpacked list is returned. If debug is True
        then the function prints information about the packet as received. See Faraday packet definition guide for information.

        --- RETURNS LIST ---
        Index[0]: Packet Type
        Index[1]: RF Source
        Index[2]: Payload Length
        Index[3]: Payload Data
        Index[4]: 16 Bit Checksum
        """
        #Unpack the packet
        parsed_packet = self.datagram_struct.unpack(packet)

        #Perform debug actions if needed
        if(debug == True):
            print "\n--- Telemetry Datagram ---"
            print "Telemetry Packet Type:", parsed_packet[0]
            print "Telemetry RF Source:", parsed_packet[1]
            print "Telemetry Payload Length:", parsed_packet[2]
            print "Telemetry Packet 16 Bit Checksum:", parsed_packet[4]
            print "Telemetry Packet Payload Data:", repr(parsed_packet[3])
            print "\n"
        else:
            pass

        #Return parsed packet list
        return parsed_packet




    def UnpackPacket_3(self, packet, debug):
        """
        Unpacks a telemetry packet type 3 (Telemetry) from the raw packet supplied in the function argument. The raw unpacked list is returned. If debug is True
        then the function prints information about the packet as received. See Faraday packet definition guide for information.

        --- RETURNS LIST ---
        Index[0]: Source Callsign
        Index[1]: Source Callsign Length
        Index[2]: Source Callsign ID
        Index[3]: Destination Callsign
        Index[4]: Destination Callsign Length
        Index[5]: Destination Callsign ID
        Index[6]: RTC Second
        Index[7]: RTC Minute
        Index[8]: RTC Hour
        Index[9]: RTC Day
        Index[10]: RTC Day Of Week
        Index[11]: RTC Month
        Index[12]: Year
        Index[13]: GPS Lattitude
        Index[14]: GPS Lattitude Direction
        Index[15]: GPS Longitude
        Index[16]: GPS Longitude Direction
        Index[17]: GPS Altitude
        Index[18]: GPS Altitude Units
        Index[19]: GPS Speed
        Index[20]: GPS Fix
        Index[21]: GPS HDOP
        Index[22]: GPIO State Telemetry
        Index[23]: RF State Telemetry
        Index[24]: ADC 0
        Index[25]: ADC 1
        Index[26]: ADC 2
        Index[27]: ADC 3
        Index[28]: ADC 4
        Index[29]: ADC 5
        Index[30]: ADC 6
        Index[31]: CC430 Temperature
        Index[32]: ADC 8
        Index[33]: N/A Byte
        Index[34]: HAB Automatic Cutdown Timer State Machine State
        Index[35]: HAB Cutdown Event State Machine State
        Index[36]: HAB Automatic Cutdown Timer Trigger Time
        Index[37]: HAB Automatic Cutdown Timer Current Time
        """
        #Unpack the packet
        parsed_packet = self.packet_3_struct.unpack(packet)

        #Perform debug actions if needed
        if(debug == True):
            print "--- Telemetry Packet #3 ---"
            print "Index[0]: Source Callsign", parsed_packet[0]
            print "Index[1]: Source Callsign Length", parsed_packet[1]
            print "Index[2]: Source Callsign ID", parsed_packet[2]
            print "Index[3]: Destination Callsign", parsed_packet[3]
            print "Index[4]: Destination Callsign Length", parsed_packet[4]
            print "Index[5]: Destination Callsign ID", parsed_packet[5]
            print "Index[6]: RTC Second", parsed_packet[6]
            print "Index[7]: RTC Minute", parsed_packet[7]
            print "Index[8]: RTC Hour", parsed_packet[8]
            print "Index[9]: RTC Day", parsed_packet[9]
            print "Index[10]: RTC Day Of Week", parsed_packet[10]
            print "Index[11]: RTC Month", parsed_packet[11]
            print "Index[12]: Year", parsed_packet[12]
            print "Index[13]: GPS Lattitude", parsed_packet[13]
            print "Index[14]: GPS Lattitude Direction", parsed_packet[14]
            print "Index[15]: GPS Longitude", parsed_packet[15]
            print "Index[16]: GPS Longitude Direction", parsed_packet[16]
            print "Index[17]: GPS Altitude", parsed_packet[17]
            print "Index[18]: GPS Altitude Units", parsed_packet[18]
            print "Index[19]: GPS Speed", parsed_packet[19]
            print "Index[20]: GPS Fix", parsed_packet[20]
            print "Index[21]: GPS HDOP", parsed_packet[21]
            print "Index[22]: GPIO State Telemetry", parsed_packet[22]
            print "Index[23]: RF State Telemetry", parsed_packet[23]
            print "Index[24]: ADC 0", parsed_packet[24]
            print "Index[25]: ADC 1", parsed_packet[25]
            print "Index[26]: ADC 2", parsed_packet[26]
            print "Index[27]: ADC 3", parsed_packet[27]
            print "Index[28]: ADC 4", parsed_packet[28]
            print "Index[29]: ADC 5", parsed_packet[29]
            print "Index[30]: ADC 6", parsed_packet[30]
            print "Index[31]: CC430 Temperature", parsed_packet[31]
            print "Index[32]: ADC 8", parsed_packet[32]
            print "Index[33]: N/A Byte", parsed_packet[33]
            print "Index[34]: HAB Automatic Cutdown Timer State Machine State", parsed_packet[34]
            print "Index[35]: HAB Cutdown Event State Machine State", parsed_packet[35]
            print "Index[36]: HAB Automatic Cutdown Timer Trigger Time", parsed_packet[36]
            print "Index[37]: HAB Automatic Cutdown Timer Current Time", parsed_packet[37]
        else:
            pass

        #Return parsed packet list
        return parsed_packet

    def ExtractPaddedPacket(self, packet, packet_len):
        """
        This function simply extracts and returns a packet from a longer byte array. This is useful to extract ONLY the intended packet to be parsed from
        a longer padded "payload" packet of a frame or encapsulation.

        WARNING: This function does not ensure that the returned packet is the intended data packet, it only corrects byte array length!
        """
        return packet[0:packet_len]

    def UnpackPacket_2(self, packet, debug):
        """
        Unpacks a telemetry packet type 2 (Debug Flash) from the raw packet supplied in the function argument. The raw unpacked list is returned. If debug is True
        then the function prints information about the packet as received. See Faraday packet definition guide for information.

        --- RETURNS LIST ---
        Index[0]: Boot Count
        Index[1]: Reset Count
        Index[2]: Brownout reset counter
        Index[3]: Reset / Non-maskable Interust counter
        Index[4]: PMM Supervisor Low counter
        Index[5]: PMM Supervisor High counter
        Index[6]: PMM Supervisor Low - OVP counter
        Index[7]: PMM Supervisor High - OVP counter
        Index[8]: Watchdog timeput counter
        Index[9]: Flash key violation counter
        Index[10]: FLL Unlock counter
        Index[11]: Peripheral / Config counter
        Index[12]: Access violation counter
        """
        #Unpack the packet
        parsed_packet = self.packet_2_struct.unpack(packet)

        #Perform debug actions if needed
        if(debug == True):
            print "--- Telemetry Packet #2 ---"
            print "Index[0]: Boot Count", parsed_packet[0]
            print "Index[1]: Reset Count", parsed_packet[1]
            print "Index[2]: Brownout reset counter", parsed_packet[2]
            print "Index[3]: Reset / Non-maskable Interust counter", parsed_packet[3]
            print "Index[4]: PMM Supervisor Low counter", parsed_packet[4]
            print "Index[5]: PMM Supervisor High counter", parsed_packet[5]
            print "Index[6]: PMM Supervisor Low - OVP counter", parsed_packet[6]
            print "Index[7]: PMM Supervisor High - OVP counter", parsed_packet[7]
            print "Index[8]: Watchdog timeput counter", parsed_packet[8]
            print "Index[9]: Flash key violation counter", parsed_packet[9]
            print "Index[10]: FLL Unlock counter", parsed_packet[10]
            print "Index[11]: Peripheral / Config counter", parsed_packet[11]
            print "Index[12]: Access violation counter", parsed_packet[12]
        else:
            pass

        #Return parsed packet list
        return parsed_packet

    def UnpackPacket_1(self, packet, debug):
        """
        Unpacks a telemetry packet type 1 (Faraday System Settings) from the raw packet supplied in the function argument. The raw unpacked list is returned. If debug is True
        then the function prints information about the packet as received. See Faraday packet definition guide for information.

        --- RETURNS LIST ---
        Index[0]: RF Freq 2
        Index[1]: RF Freq 1
        Index[2]: RF Freq 0
        Index[3]: RF Power Bitmask
        """
        #Unpack the packet
        parsed_packet = self.packet_1_struct.unpack(packet)

        #Perform debug actions if needed
        if(debug == True):
            print "--- Telemetry Packet #1 ---"
            print "Index[0]: RF Freq 2", parsed_packet[0]
            print "Index[1]: RF Freq 1", parsed_packet[1]
            print "Index[2]: RF Freq 0", parsed_packet[2]
            print "Index[3]: RF Power Bitmask", parsed_packet[3]
        else:
            pass

        #Return parsed packet list
        return parsed_packet

    def UnpackConfigFlashD(self, packet, debug):
        """
        Unpacks a Flash memory info segment D "Packet" structure (Faraday Flash Memory non-volitile defaults) from the raw packet supplied in the function argument. The raw unpacked list is returned. If debug is True
        then the function prints information about the packet as received. See Faraday packet definition guide for information.

        --- RETURNS LIST ---
            Index[0]: Flash Config Bitmask
            Index[1]: Local Callsign
            Index[2]: Local Callsign Length
            Index[3]: Local Callsign ID
            Index[4]: Default Port 3 GPIO Bitmask
            Index[5]: Default Port 4 GPIO Bitmask
            Index[6]: Default Port 5 GPIO Bitmask
            Index[7]: Default Boot Frequency [0]
            Index[8]: Default Boot Frequency [1]
            Index[9]: Default Boot Frequency [2]
            Index[10]: Default RF Power Amplifier Setting (PA Table)
            Index[11]: Default GPS Lattitude
            Index[12]: Default GPS Lattitude Direction
            Index[13]: Default GPS Longitude
            Index[14]: Default GPS Longitude Direction
            Index[15]: Default GPS Altitude
            Index[16]: Default GPS Altitude Units
            Index[17]: Default GPS Boot Bitmask
            Index[18]: Default Telemetry Boot Bitmask
            Index[19]: Default UART Telemetry Interval
            Index[20]: Default RF Telemetry Interval
        """
        #Unpack the packet
        parsed_packet = self.flash_config_info_d_struct.unpack(packet)

        #Perform debug actions if needed
        if(debug == True):
            print "--- Flash Information Segment D ---"
            print "Index[0]: Flash Config Bitmask", format(parsed_packet[0], '#010b')
            print "Index[1]: Local Callsign", parsed_packet[1]
            print "Index[2]: Local Callsign Length", parsed_packet[2]
            print "Index[3]: Local Callsign ID", parsed_packet[3]
            print "Index[4]: Default Port 3 GPIO Bitmask", format(parsed_packet[4], '#010b')
            print "Index[5]: Default Port 4 GPIO Bitmask", format(parsed_packet[5], '#010b')
            print "Index[6]: Default Port 5 GPIO Bitmask", format(parsed_packet[6], '#010b')
            print "Index[7]: Default Boot Frequency [0]", parsed_packet[7]
            print "Index[8]: Default Boot Frequency [1]", parsed_packet[8]
            print "Index[9]: Default Boot Frequency [2]", parsed_packet[9]
            print "Index[10]: Default RF Power Amplifier Setting (PA Table)", parsed_packet[10]
            print "Index[11]: Default GPS Lattitude", parsed_packet[11]
            print "Index[12]: Default GPS Lattitude Direction", parsed_packet[12]
            print "Index[13]: Default GPS Longitude", parsed_packet[13]
            print "Index[14]: Default GPS Longitude Direction", parsed_packet[14]
            print "Index[15]: Default GPS Altitude", parsed_packet[15]
            print "Index[16]: Default GPS Altitude Units", parsed_packet[16]
            print "Index[17]: Default GPS Boot Bitmask", format(parsed_packet[17], '#010b')
            print "Index[18]: Default Telemetry Boot Bitmask", format(parsed_packet[18], '#010b')
            print "Index[19]: Default UART Telemetry Interval", parsed_packet[19]
            print "Index[20]: Default RF Telemetry Interval", parsed_packet[20]
        else:
            pass

        #Return parsed packet list
        return parsed_packet
