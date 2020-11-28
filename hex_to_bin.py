def hex_to_bin(hex_inp_str):
    """ Return binary string, given a hex string input """
    bin_result = bin(int(hex_inp_str, 16)).zfill(8) 
    bin_result = (bin_result).split("0b")[1]
    while len(bin_result) != (len(hex_inp_str)*4):
        bin_result = "0" + bin_result 
    return bin_result

# Declaring example hex strings
hex_a = "BE432E89CEAF5147"
hex_b = "9C8B342FEC159584"
hex_c = "8855F8CFD965CCBB"

# Convert each hex string to binary
bin_a = hex_to_bin(hex_a)
bin_b = hex_to_bin(hex_b)
bin_c = hex_to_bin(hex_c)

print('\n'+bin_a)
