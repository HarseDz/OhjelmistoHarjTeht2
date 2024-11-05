from flask import Flask

app = Flask(__name__)
@app.route('/alkuluku/<luku>)
def alkuluku(luku):
    x = int(luku)
    y = 2
    while x>y:
        if x%y== 0
            z=false
            break
        else:y=y+1
    if x ==y:
        z=vastaus