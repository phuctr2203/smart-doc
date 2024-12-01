from flask import Flask
from flask_restx import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        """
        Hello World endpoint
        ---
        responses:
          200:
            description: Returns a hello world message
        """
        return {'message': 'Hello, World!'}

if __name__ == '__main__':
    app.run(debug=True)
