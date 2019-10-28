from six.moves import urllib
import json

class GraphQLClient:
    def __init__(self, endpoint, parseResponse = True):
        self.endpoint = endpoint
        self.token = None
        self.headername = None
        self.parseResponse = parseResponse

    def execute(self, query, variables=None):
        return json.loads(self._send(query, variables)) if self.parseResponse else self._send(query, variables)

    def inject_token(self, token, headername='Authorization'):
        self.token = token
        self.headername = headername

    def _send(self, query, variables):
        data = {'query': query,
                'variables': variables}
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}

        if self.token is not None:
            headers[self.headername] = '{}'.format(self.token)

        req = urllib.request.Request(self.endpoint, json.dumps(data).encode('utf-8'), headers)

        try:
            response = urllib.request.urlopen(req)
            return response.read().decode('utf-8')
        except urllib.error.HTTPError as e:
            print((e.read()))
            print('')
            raise e
