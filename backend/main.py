import json
import sys
import os

from threading import Thread
from time import sleep


from libs.websocket_server import WebsocketServer


def message_received(client, server, message):
    request = json.loads(message)
    def start_responder(client, server, message):
        try:
            Responder(client, server, request)
        except json.JSONDecodeError as e:
            server.send_message(client, 'Invalid request. {}'.format(e))
        except KeyError as e:
            server.send_message(client, 'Invalid request. {}'.format(e))

    p = Thread(target=start_responder, args=(client, server, message))
    p.daemon = True
    p.start()

def start_server():
    server = WebsocketServer(9001, host='0.0.0.0')
    server.set_fn_message_received(message_received)
    print("Started\n")
    server.run_forever()


if __name__ == '__main__':
    try:
        start_server()
        while True: sleep(100)
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)