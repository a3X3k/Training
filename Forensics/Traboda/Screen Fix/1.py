import binascii

def compute_crc(w, h):
    hexw = "{:08x}".format(w)
    hexh = "{:08x}".format(h)
    return hex(binascii.crc32(bytes.fromhex("49484452{}{}0802000000".format(hexw, hexh))))


for w in range(2000):
    for h in range(2000):
        crc = compute_crc(w,h)
        if crc == "0x22e513da":
            print(hex(w),hex(h))
