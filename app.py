import flask
from sortedcontainers import SortedSet
import werkzeug.exceptions
from datetime import datetime, timedelta
from collections import deque
app = flask.Flask(__name__)
app.config['DEBUG'] = True
books = SortedSet([(2, 'two'), (1, 'one'), (3, 'three')])
que = deque()


@app.route('/', methods=['GET'])
def home():
    return '<h1> Hello There</h1><p> This is a prototype</p>'


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/books', methods=['GET'])
def get_method():
    id = flask.request.args.get('id')
    id = int(id)
    # print(id)
    for key in que:
        curr = datetime.now() - key[1]
        if curr.total_seconds() > 0:
            que.pop()
            books.discard((key, key[2]))
    # print(books)
        # print(book)
    c = 0
    for book in books:
        if id not in book:
            c += 1
    if c == len(books):
        return "<h1>Item Expired</h1>"

    # print(id)
    results = []
    l, r = 0, len(books) - 1
    while l <= r:
        mid = (l + r) // 2
        if books[mid][0] == id:
            results.append(books[mid][1])
            break
        elif books[mid][0] < id:
            l = mid + 1
        else:
            r = mid - 1
    if len(results) == 0:
        results.append('nil')

    return flask.jsonify(results)


@app.route('/api/v1/books/time', methods=['GET'])
def expire_check():
    key = flask.request.args.get('value')
    key = int(key)
    t = int(flask.request.args.get('life'))
    curr_now = datetime.now()
    curr_now += timedelta(seconds=t)
    print(curr_now)
    que.append((key, curr_now,))
    l, r = 0, len(books) - 1
    while l <= r:
        mid = (l + r) // 2
        if books[mid][0] == key:
            que.append((key, curr_now, books[mid][1]))
        elif books[mid][0] < key:
            l = mid + 1
        else:
            r = mid - 1
        return "<h1>TTL ADDED</h1>"



@app.route('/api/v1/books/search', methods=['GET'])
def z_rank():
    key = flask.request.args.get('value')
    key = int(key)
    l, r = 0, len(books) - 1
    while l <= r:
        mid = (l + r) // 2
        if books[mid][0] == key:
            return flask.jsonify(mid)
        elif books[mid][0] < key:
            l = mid + 1
        else:
            h = mid - 1
    return "<h1>Item not present</h1>"


@app.route('/api/v1/books/update', methods=['GET'])
def z_add():
    NX, CH, XX, INCR = False, False, False, False
    id_1 = flask.request.args['id_1']
    val_1 = flask.request.args['val_1']
    id_2 = flask.request.args['id_2']
    val_2 = flask.request.args['val_2']
    mode = flask.request.args['mode']
    id_1, id_2, c = int(id_1), int(id_2), 0
    l, r = 0, len(books) - 1
    ind1, ind2 = False, False
    while l <= r:
        mid = (l + r) // 2
        if books[mid][0] == id_1:
            if books[mid][1] != val_1:
                ind1 = mid
                books.discard((books[mid][0], books[mid][1]))
                books.add((id_1, val_1))
                c += 1
                break
        elif books[mid][0] < id:
            l = mid + 1
        else:
            r = mid - 1
    l, r = 0, len(books) - 1
    while l <= r:
        mid = (l + r) // 2
        if books[mid][0] == id_2:
            if books[mid][1] != val_2:
                ind2 = mid
                books.discard((books[mid][0], books[mid][1]))
                books.add((id_2, val_2))
                break
        elif books[mid][0] < id_2:
            l = mid + 1
        else:
            r = mid - 1

    if mode.lower() == 'xx':
        if ind1:
            books.discard((books[ind1][0], books[ind1][1]))
            books.add((id_1, val_1))
            c += 1
        if ind2:
            books.discard((books[ind2][0], books[ind2][1]))
            books.add((id_2, val_2))
            c += 1
    if mode.lower() == 'nx':
        if not ind1:
            books.add((id_1, val_1))
            c += 1
            if not ind2:
                books.add((id_2, val_2))
                c += 1
    if mode == 'ch':
        c = 2

    return flask.jsonify('{} items updated'.format(c))


@app.route('/api/v1/books/set', methods=['GET'])
def set_method():
        id = flask.request.args['id']
        id = int(id)
        val = flask.request.args['value']
        books.add((id, val))
        return "<h1>Item Added</h1>"


@app.route('/api/v1/books/add/find', methods=['GET'])
def z_range():
    start = flask.request.args.get('param1')
    end = flask.request.args.get('param2')
    ans = []
    for book in books:
        ans.append(book[1])
    if start and end is None:
        return flask.jsonify()
    start, end = int(start), int(end)
    ans2 = ans[start: end]
    return flask.jsonify(ans2)




app.run()

