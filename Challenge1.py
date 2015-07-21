#input_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

input_str = "map"
new_str = ""

for index in range(0,len(input_str)):
    n = ord(input_str[index])
    if input_str[index] <= 'z' and input_str[index] >= 'a':
        n = n + 2
        if n > ord('z'):
            n = ord('a') + n - ord('z') - 1
    new_str += chr(n)

print(new_str+".html")

