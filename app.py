from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    f = open("count.txt","r")
    count = int(f.read())
    f.close()

    count += 1

    f = open("count.txt","w")
    f.write(str(count))
    f.close()

    return render_template('index.html', count=count)

if __name__ == '__main__':
    app.run()