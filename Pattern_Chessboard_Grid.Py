def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def do_eight(f):
    do_four(f)
    do_four(f)

def beam():
    print('+----',end='')

def beams():
    do_eight(beam)
    print('+')

def post():
    print('|    ',end='')

def posts():
    do_eight(post)
    print('|')

def row():
    beams()
    do_twice(posts)

def chessboard():
    do_eight(row)
    beams()

chessboard()
