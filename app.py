from flask import Flask

app = Flask(__name__)

# Setup logger handlers
app.logger.addHandler()

if __name__ == '__main__':
    app.run()
