#!/usr/bin/python
# -*- coding: utf-8 -*-

import io
import json


with io.open('report.json', 'r') as f:
    data = json.load(f)

with io.open('table.md', 'w') as f:
    f.write('| Type | Interpreter | Package A command | Package B command | Status |\n')
    f.write('| --- | --- | --- | --- | --- |\n')
    for session in data['sessions']:
        session_name = session['name']
        session_detailled_name = session['signatures'][-1]
        session_interpreter = session_detailled_name.replace(session_name + "-", "python")
        # TODO: Replace with `str.removeprefix()` in Python 3.12
        session_name = session_name[len("session_") :]

        f.write('| {} | {} | {} | {} | {} |\n'.format(
            session_name,
            session_interpreter,
            ' '.join(session['args']['command_a']),
            ' '.join(session['args']['command_b']),
            '✅' if session['result_code'] else '❌'
        ))
