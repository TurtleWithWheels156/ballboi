from app import app

@app.route('/')
def no_word():
        return "Hello!"
@app.route('/direction/<direction>')
def direction(direction):
        if direction == "back":
            return "back"
        if direction == 'forward':
            return 'forward'
        if direction == 'left':
            return 'left'
        if direction == 'right':
            return 'right'
