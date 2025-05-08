import socket
import struct

HOST = '0.0.0.0'
PORT = 65431

print(f"Starting server at {HOST}:{PORT}")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print("Connected at", addr)

    with conn:
        buffer = b''
        while True:
            data = conn.recv(1024)
            if not data:
                break
            buffer += data

            # 处理完整的2字节数据
            while len(buffer) >= 2:
                key_bytes = buffer[:2]
                buffer = buffer[2:]

                # 解析为16位整数（大端 or 小端根据STM32设定，默认小端）
                key_value = struct.unpack('<H', key_bytes)[0]  # 小端：<H；大端：>H

                print(f"Key Value: 0x{key_value:08x}")
