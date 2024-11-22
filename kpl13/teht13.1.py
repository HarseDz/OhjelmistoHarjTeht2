from flask import Flask, jsonify


app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    try:
        x = int(luku)
        if x <= 1:
            z = False
        else:
            z = True
            y = 2
            while y * y <= x:
                if x % y == 0:
                    z = False
                    break
                y += 1

        return jsonify({
            "Number": x,
            "isPrime": z
        })
    except ValueError:
        return jsonify({"error": "invalid input!"}), 400

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
