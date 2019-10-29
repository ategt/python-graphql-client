import json

class GraphQLException(Exception):
	def __init__(self, sourceException):
		super(GraphQLException, self).__init__("Errors occured, see response property for details.")
		self.sourceException = sourceException
		self._loadException()

	def _loadException(self):
		self.data = self.sourceException.read()
		self.response = json.loads(self.data)