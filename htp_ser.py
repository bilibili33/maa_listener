from flask import Flask

app = Flask(__name__)


@app.route("/maa_stat")
def foo():
    try:
        with open("stat.log") as f:
            d = f.read()
        if d == "yes":
            return d, 200
        else:
            return d, 418
    except FileNotFoundError:
        return "file not found", 404


if __name__ == '__main__':
    print("Flask.app Listening:0.0.0.0:17777 Route:maa_stat IndexFile:stat.log\n")
    app.run(host="0.0.0.0", port=17777)
