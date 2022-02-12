# dump roms in binary and octal format
# import io

# rom_in: str = input('Select rom binary: ')
rom_in = "1816-0420.bin"

print(rom_in)

# raw = io.BytesIO()
with open("rom_in","rb") as rom_bin:
    rom_out = rom_bin.read()
    print(rom_out)
