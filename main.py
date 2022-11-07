import os
from app import create_app


settings_module = os.getenv('APP_SETTINGS_MODULE')
if not settings_module:
    settings_module = os.environ.get('APP_SETTINGS_MODULE', 'config.default')

app = create_app(settings_module)



@app.route('/pings', methods=['GET'])
def ping():
    """
        Check if server is alive
        :return: "pong"
    """
    return "pong"


@app.route('/', methods=['GET'])
def ok():
    """
        Check if server is alive
        :return: "ok"
    """
    return "ok"


if __name__ == "__main__":
    app.run(debug=True)
