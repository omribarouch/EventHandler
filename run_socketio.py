from app.socketio import socketio
from factory import create_app


create_app()

if __name__ == '__main__':
    socketio.run()
