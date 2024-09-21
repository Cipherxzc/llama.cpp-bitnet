def generate_table():
    map = {
        0: 0x00,
        1: 0x01,
        2: 0x00,
        3: 0xff
    }
    
    table = []
    
    for x in range(256):
        hex_value = 0
        for i in range(4):
            quad_digit = (x >> (i * 2)) & 0x3
            hex_value |= (map[quad_digit] << (i * 8))
        
        table.append(hex_value)
    
    for i in range(0, 256, 4):
        print(f"    0x{table[i]:08x}, 0x{table[i+1]:08x}, 0x{table[i+2]:08x}, 0x{table[i+3]:08x},")

generate_table()