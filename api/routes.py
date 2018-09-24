from flask import Flask
import json
app = Flask(__name__)

@app.route('/api/test', methods=['GET'])
def test_route():
  return 'hello!'


if __name__ == '__main__':
  app.debug = True
  app.run(host='0.0.0.0', port=3001)
