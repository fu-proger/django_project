from flask import Flask, jsonify
import argparse
import csv

app = Flask(__name__)


@app.route('/false')
def get_false():
    dc = {}
    for _, sname, name, text, status in table:
        key = f'{sname} {name}'
    if key not in dc:
        dc[key] = {
            "sname": sname,
            "name": key,
            "lie": [],
            "truth": []
        }
    if status == 'lie':
        dc[key]['lie'].append(text)
    elif status == 'truth':
        dc[key]['truth'].append(text)
        answer = list(dc.values())
        answer.sort(key=lambda x: x['sname'])
        for x in answer:
            del x['sname']
    return jsonify(answer)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port')
    parser.add_argument('--server')
    parser.add_argument('--filename')
    args = parser.parse_args()
    with open(args.filename, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='+')
    next(reader)
    table = list(reader)
    app.run(host=args.server, port=args.port)
