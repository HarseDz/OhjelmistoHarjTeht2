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
#def onko_alkuluku(n):
  #  if n <= 1:
  #      return False
 #   for i in range(2, int(n**0.5) + 1):
 #       if n % i == 0:
   #         return False
#    return True

# Flask-reitti
#@app.route('/alkuluku/<int:luku>', methods=['GET'])
#def tarkista_alkuluku(luku):
  #  tulos = {
   #     "Number": luku,
    #    "isPrime": onko_alkuluku(luku)
  #  }
 #   return jsonify(tulos)

# Sovelluksen käynnistäminen
#if __name__ == '__main__':
   # app.run(debug=True, port=3000)
  #      from flask import Flask, request

    #    app = Flask(__name__)

      #  @app.route('/summa')
    #    def summa():
        #    args = request.args
        #    luku1 = float(args.get("luku1"))
        #    luku2 = float(args.get("luku2"))
        #    summa = luku1 + luku2
       #     return str(summa)

     #   if __name__ == '__main__':
      #      app.run(use_reloader=True, host='127.0.0.1', port=3000)