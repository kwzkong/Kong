from eth_abi import decode_abi

original_response = "0x27d0cf76bfc1dde"
revised_response = "0x027d0cf76bfc1dde"
#
# bytes.fromhex()转换str需要满两位16进制(8 bits)否则会报错
# print(response[2:])


#怎么样decode呢？
a = bytes.fromhex(revised_response[2:])

print(result)
