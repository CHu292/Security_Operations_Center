# Define the mapping based on the table
bit_mapping = {
    '0000': '11110',
    '0001': '01001',
    '0010': '10100',
    '0011': '10101',
    '0100': '01010',
    '0101': '01011',
    '0110': '01110',
    '0111': '01111',
    '1000': '10010',
    '1001': '10011',
    '1010': '10110',
    '1011': '10111',
    '1100': '11010',
    '1101': '11011',
    '1110': '11100',
    '1111': '11101',
}

# Function to map input string in chunks of 4 bits
def map_bit_string(input_str):
    # Check if the length of the string is a multiple of 4
    if len(input_str) % 4 != 0:
        print("Chuỗi bit không phải là bội số của 4. Vui lòng nhập lại.")
        return None

    output_str = ""
    # Process the input in chunks of 4 bits
    for i in range(0, len(input_str), 4):
        chunk = input_str[i:i + 4]
        if chunk in bit_mapping:
            output_str += bit_mapping[chunk]
        else:
            print(f"Chuỗi bit '{chunk}' không hợp lệ.")
            return None
    
    # Insert space after every 8 bits
    spaced_output = ' '.join([output_str[i:i + 8] for i in range(0, len(output_str), 8)])

    return spaced_output

# Get the bit string input from the user
input_bit = input("Nhập chuỗi bit (bội số của 4 ký tự): ")

# Map the input bit string and print the result
output_bit = map_bit_string(input_bit)

if output_bit:
    print(f"Chuỗi kết quả là: {output_bit}")

