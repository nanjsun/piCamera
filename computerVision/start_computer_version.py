from connect_to_socket_server import connect_to_socket_server
from measure_specimen_length import measure_specimen_length
from start_camera import start_camera


def start_computer_version():
    # connect to socket server
    command, sock = connect_to_socket_server(8999)
    if command == 'measure_specimen_length':
        measure_length = measure_specimen_length()




