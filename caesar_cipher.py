def caesar_cipher(text, key):
    result = ""
    for char in text:  # 遍历文本中的每个字符
        if char.isalpha():  # 检查字符是否全为字母
            offset = ord('A') if char.isupper() else ord('a')  # 确定字符的偏移量（大写字母或小写字母）
            # 计算加密或解密后的字符的ASCII值
            encrypted_char = chr((ord(char) - offset + key) % 26 + offset)
            # 将加密或解密后的字符添加到结果字符串中
            result += encrypted_char
        else:
            # 如果字符不是字母，则直接添加到结果字符串中
            result += char
    return result 
print(caesar_cipher('cryptography',3)) #加密
print(caesar_cipher(caesar_cipher('cryptography',3),-3))  #解密