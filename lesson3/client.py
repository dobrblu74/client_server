import settings
import function

client_name = input('Введите имя: ')

parser = function.create_parser()
namespace = parser.parse_args()

sock = function.get_client_socket(namespace.addr, namespace.port)

serv_addr = sock.getpeername()
print(f'Connected to server: {serv_addr[0]}:{serv_addr[1]}')

settings.PRESENCE['user']['account_name'] = client_name
function.send_data(sock, settings.PRESENCE)

while True:
    data = function.get_data(sock)

    if data['response'] != '200':
        break

    msg = input('Введите сообщение ("exit" для выхода): ')
    settings.MESSAGE['message'] = msg
    function.send_data(sock, settings.MESSAGE)

sock.close()