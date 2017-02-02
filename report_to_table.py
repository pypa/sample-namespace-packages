import io
import json


with io.open('report.json', 'r') as f:
    data = json.load(f)

with io.open('table.md', 'w') as f:
    f.write(u'| Type | Interpreter | Package A command | Package B command | Status |\n')
    f.write(u'| --- | --- | --- | --- | --- |\n')
    for session in data['sessions']:
        f.write(u'| {} | {} | {} | {} | {} |\n'.format(
            session['name'],
            session['args']['interpreter'],
            ' '.join(session['args']['command_a']),
            ' '.join(session['args']['command_b']),
            'pass' if session['result'] else 'fail'
        ))
