import socket
import json


def connect_to_socket_server(port):
    # class SocketClientOnCamera
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', port)
    sock.connect(server_address)
    print("connect to server success!")

    socket_information_template = '{"cameraOK":false,"direction":0,"firstDistanceBetweenSpecimenAndIgnitor":0,' \
                                    '"command":"try","ignitorFlameLength":0,"ignitorFlamed":false,' \
                                    '"secondDistanceBetweenSpecimenAndIgnitor":0,"specimenBurnTime":0,' \
                                    '"specimenBurnoffLength":0,"specimenFlameLength":0,"specimenFlamed":false,' \
                                    '"specimenLength":0} '
    parsed_information = json.loads(socket_information_template)
    parsed_information['command'] = 'socketInitOk'
    json_information_will_send = json.dumps(parsed_information)
    sock.sendall(bytes(json_information_will_send + '\n', encoding="utf-8"))
    sz_buf = sock.recv(1024)
    information_from_server = str(sz_buf, 'utf-8')

    parsed_information = json.loads(information_from_server)

    command = parsed_information['command']

    return command, sock
