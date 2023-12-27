# input_string = "Hello World"

# # Function to perform bitwise operations
# def perform_bitwise_operations(string, operator):
#     result = ""
#     for char in string:
#         if operator == 'AND':
#             result += chr(ord(char) & 127)
#         elif operator == 'OR':
#             result += chr(ord(char) | 127)
#         elif operator == 'XOR':
#             result += chr(ord(char) ^ 127)
#     return result

# # Perform AND operation
# result_and = perform_bitwise_operations(input_string, 'AND')
# print(f'AND Result: "{result_and}"')

# # Perform OR operation
# result_or = perform_bitwise_operations(input_string, 'OR')
# print(f'OR Result: "{result_or}"')

# # Perform XOR operation
# result_xor = perform_bitwise_operations(input_string, 'XOR')
# print(f'XOR Result: "{result_xor}"')

def ANDOperation(s:str):
    return[(ord(i) & 127) for i in s]
def OROperation(s:str):
    return[(ord(i) | 127) for i in s]
def XOROperation(s:str):
    return[(ord(i) ^ 127) for i in s]
if __name__ == "__main__":
    input_string = "Hello World"
    print("AND: ", ANDOperation(input_string),"Characters: ","".join(chr(i) for i in ANDOperation(input_string)))
    print("OR: ", OROperation(input_string),"Characters: ","".join(chr(i) for i in OROperation(input_string)))
    print("/XOR: ", XOROperation(input_string),"Characters: ","".join(chr(i) for i in XOROperation(input_string)))