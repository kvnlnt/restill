from resources import Resource
from resources.fields import Field


class Properties(Resource):

    def __init__(self, method, data):
        Resource.__init__(self, method, data)

        self.definition = {
            'id': Field(type=int),
            'property': Field(type=str)
        }
