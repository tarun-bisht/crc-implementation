from crc import CRC
data=input("Enter Binary Data: ")
crc_polynomial=input("Enter CRC Polynomial: ")
crc=CRC(data,crc_polynomial)
print(crc)
