#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Brent
#
# Created:     03/08/2016
# Copyright:   (c) Brent 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import array

#blinkLED_f6459.txt

f = open('blinkLED_f6459.txt', 'r')

mem_addr_index = []
section_data_index = []
file_program_hex = f.read()

def ParseTiTxtHexFile(input_file):
    datasections = input_file.split('@')
    datasections.pop(0) #remove empty first index

    #remove memory addresses and separate data in each section
    for i in range(0, len(datasections)):
        #Parse and strip TI-TXT format
        a = datasections[i].replace('\n', '')
        a = a.replace(' ', '')
        mem_addr = str(a[0:4]).decode('hex')
        section_data = str(a[4:]).replace('q', '')#remove end of file
        #Ouput
        mem_addr_index.append(mem_addr)
        section_data_index.append(section_data.decode('hex'))

def CalcTiTxtCrc16(databytes):
    data_array = array.array('B', databytes)
    chk = 0xffff
    for item in data_array:
        calc = 0
        calc = ((chk>>8)^item) & 0xff
        calc ^= calc>>4
        chk = (chk <<8)^(calc<<12)^(calc<<5)^calc
        chk = chk % 2**16
    return chk


def CreateOutputFile():
    textfile = open("Program_CRC_Calculations.txt", 'w')
    for i in range(0, len(mem_addr_index)):
        final_addr = mem_addr_index[i].encode('hex')
        final_len = hex(len(section_data_index[i]))
        final_crc = hex(CalcTiTxtCrc16(section_data_index[i]))
        textfile.writelines(("Memory Address: 0x", final_addr,"\n"))
        textfile.writelines(("Data Length: ", final_len,"\n"))
        textfile.writelines(("CRC: ", final_crc))
        textfile.writelines(("\nCRC_CHECK ", "0x", final_addr, ' ', final_len, ' ', final_crc))
        textfile.writelines('\n\n')

ParseTiTxtHexFile(file_program_hex)
CreateOutputFile()

