data = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽'
#''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
decoded = ''
for i in range(len(data)):
        decoded += chr(ord(data[i])>>8)
        decoded += chr((ord(data[i]))-((ord(data[i])>>8)<<8))
print(decoded)