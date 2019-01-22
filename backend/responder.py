import json

class Responder:
    server = None
    client = None 
    request = None

    def __init__(self, client, server, request):
        self.server = server
        self.client = client

        self.request = request

        if request['request'] == 'signin':
            self.signin()

    def signin(self):
        # TODO: implement
        pass

    def send(self, message):
        message['response_id'] = self.request['request_id']
        string_message = json.dumps(message)
        self.server.send_message(self.client, string_message)