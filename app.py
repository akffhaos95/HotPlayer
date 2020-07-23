from redis import Redis
from flask import Flask

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route("/")
def home():
    redis.incr('hits')
    return "You hits %s"%redis.get('hits')


if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0")