from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('asr.yandex.net', 80))
sock.send(b'GET /asr_partial HTTP/1.1\r\nUser-Agent: KeepAliveClient\r\nHost: asr.yandex.net:80\r\nUpgrade: dictation\r\n\r\n')
print(sock.recv(1024))
with open('connection_request.proto', 'rb') as request_protobuf:
	message = request_protobuf.read()

sock.send(bytes(hex(len(message))[2:], 'utf8'))
sock.send(bytes('\r\n', 'utf8'))
sock.send(bytes(message))
print(sock.recv(1024))
sock.close()