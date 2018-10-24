#!/usr/bin/env python
# -*- coding: utf-8 -*-

from threading import Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect


async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

socketio = SocketIO(app, async_mode=async_mode)

thread = None
thread_lock = Lock()

def background_thread():
	count = 0 
	while True:
		socketio.sleep(10)
		count += 1
		socketio.emit('my response', {'data': 'Server generated event', 'count': count}, namespace='/test')

@app.route('/')
def index():
	return render_template('index.html', async_mode=socketio.async_mode)


@socketio.on('my_event', namespace='/test')
def test_message(message):
	print session
	session['receive_count'] = session.get('receive_count', 0) + 1
	emit('my_response', {'data': message['data'], 'count': session['receive_count']})

@socketio.on('my_broadcast_event', namespace='/test')
def test_broadcast_message(message):
	session['receive_count'] = session.get('receive_count', 0) + 1
	emit('my_response', {'data': message['data'], 'count': session['receive_count']}, broadcast=True)


@socketio.on('join', namespace='/test')
def join(message):
	join_room(message['room'])
	session['receive_count'] = session.get('receive_count', 0) + 1
	emit('my_response', {'data': 'In rooms: ' + ', '.join(rooms()), 'count': session['receive_count']})

@socketio.on('leave', namespace='/test')
def leave(message):
	leave_room(message['room'])
	session['receive_count'] = session.get('receive_count', 0) + 1
	emit('my_response', {'data': 'In rooms: ' + ', '.join(rooms()), 'count': session['receive_count']})

@socketio.on('close_room', namespace='/test')
def close(message):
	session['receive_count'] = session.get('receive_count', 0) + 1
	emit('my_response', {'data': message['data'], 'count': session['receive_count']}, room=message['room'])


@socketio.on('my_room_event', namespace='/test')
def send_room_message(message):
	session['receive_count'] = session.get('receive_count', 0) + 1
	emit('my_response', {'data': message['data'], 'count': session['receive_count']}, room=message['room'])

@socketio.on('disconnect_request', namespace='/test')
def disconnect_request():
	session['receive_count'] = session.get('receive_count', 0) + 1
	emit('my_response', {'data': 'Disconnected!', 'count': session['receive_count']})
	disconnect()

@socketio.on('my_ping', namespace='/test')
def ping_pong():
	emit('my_pong')


@socketio.on('connect', namespace='/test')
def test_connect():
	print 'connect...'
	global thread
	with thread_lock:
		if thread is None:
			thread = socketio.start_background_task(target=background_thread)
	emit('my_response', {'data':'Connected', 'count':0})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
	print('Client disconnected', request.sid)

if __name__ == '__main__':
	print 'start...'
	socketio.run(app, debug=True)


