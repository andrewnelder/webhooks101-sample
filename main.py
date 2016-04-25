from flask import Flask, request
from json_parser import parse_event_data
from ngrok import start_ngrok

app = Flask(__name__)

@app.route('/', methods=["POST"])
def webhook():
    '''
    The endpoint for your webhook events.  Point your dashboard here.
    If you're running this locally, you'll need to use the ngrok tunnel
    provided.  Normally this endpoint would be <http://localhost:5000/>;
    however, with the tunnel, it will look more like
    <http://abcd1234.ngrok.io/>.  Put this URL in your dashboard when testing.
    '''

    # Step 1
    #print request.get_data()

    # Step 2
    #parse_event_data(request.get_data())
    return "OK"

if __name__ == '__main__':
    '''
    Turn on the web server.
    '''

    start_ngrok()
    app.run(use_reloader=True)
