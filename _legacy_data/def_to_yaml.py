#!/usr/bin/env python3
# .def to YAML converter, specifically for irc-def files
# Written by Daniel Oaks <daniel@danieloaks.net>, under CC0 license

from collections import OrderedDict
from glob import glob
import re
import textwrap

RE_FORM_LINE = re.compile(r'(?P<name>[a-z_]+)\s+= "\<?(?P<description>[^\>"]+)')
RE_INFO_LINE = re.compile(r'(?P<key>[a-z_]+)\s*= "\$[^\:]+\:(?P<value>[^\$]+)')
RE_VALUES_LINE = re.compile(r'(?P<key>[a-z_]+)\s*= "(?P<value>[^"]+)"')
RE_VALUE_CONTINUATION_LINE = re.compile(r'"(?P<value>[^"]+)"')
RE_URL = re.compile(r'(https?://[^\s]+)', re.IGNORECASE)


def parse_def_file(name, text):
    """Parse the given irc def file into an output file."""
    # parse initial comment
    initial_comment, text = text.split('*/', 1)

    initial_comment = initial_comment.split('\n')[2:-1]
    initial_comment = '\n'.join(['#' + x.lstrip().lstrip('*') for x in initial_comment])

    # extract format comment
    form, text = text.split('*/', 1)

    form_lines = form.strip().split('\n')[2:-1]
    form_comment = ''
    while True:
        line = form_lines.pop(0)

        if ' = {' in line:
            form_comment = form_comment.rstrip('\n# \n')
            break

        form_comment += '# ' + line.strip().lstrip('/* ') + '\n'

    # parse format string
    args = OrderedDict()

    for line in form_lines:
        line = line.lstrip('* ')

        data = RE_FORM_LINE.search(line)
        if data:
            if data.group('description') == 'yes':
                args[data.group('name')] = 'true'
            else:
                args[data.group('name')] = data.group('description')

    # parse out file info
    file = OrderedDict()
    info_lines, text = text.lstrip().split('\n\n', 1)
    info_lines = info_lines.split('\n')

    for line in info_lines:
        data = RE_INFO_LINE.search(line)
        if data and data.group('key') != 'lastupdated':
            file[data.group('key')] = data.group('value').strip()

    # parse out values string
    values_str = []
    for info in text.split('\n\n'):
        info = info.strip().split('\n')[1:-1]
        values = OrderedDict()

        last_key = ''
        for line in info:
            data = RE_VALUES_LINE.search(line)
            if data:
                last_key = data.group('key')
                values[last_key] = data.group('value')
            else:
                data = RE_VALUE_CONTINUATION_LINE.search(line)
                if data:
                    values[last_key] += data.group('value')

        value_str = '-\n'
        for key, value in values.items():
            if len(value) < 60 or key in ['format']:
                if ',' in value or ':' in value or key in ['format', 'prefixchar']:
                    value = '"{}"'.format(value.replace('"', '\\"'))
                if value.casefold().strip() == 'yes':
                    value = 'true'
                value_str += '    {k}: {v}\n'.format(k=key, v=value)
            else:
                wrapped_value = ''
                wrap_text = True
                for part in RE_URL.split(value):
                    if wrap_text:
                        text = '\n'.join(textwrap.wrap(part, width=64))
                    else:
                        text = part

                    if text.strip():
                        wrapped_value += textwrap.indent(text, '        ') + '\n'

                    wrap_text = not wrap_text

                value_str += '    {k}: >\n{v}\n'.format(k=key, v=wrapped_value)

        if value_str.strip() != '-':
            values_str.append(value_str.strip())

    values_str = '\n\n'.join(values_str)

    # yaml file
    return("""# {name}.yaml
#
{initial_comment}

file:
    type: "{name}"
{file}

{form_comment}

format:
{form_args}

values:
{values}
""".format(name=name,
           initial_comment=initial_comment,
           file='\n'.join(['    {k}: "{v}"'.format(k=k, v=v) for k, v in file.items()]),
           form_comment=form_comment,
           form_args='\n'.join(['    {k}: "{v}"'.format(k=k, v=v) if ',' in v else '    {k}: {v}'.format(k=k, v=v) for k, v in args.items()]),
           values=textwrap.indent(values_str, '    ')))

filenames = glob('*.def')

for def_filename in filenames:
    with open(def_filename, 'r') as def_file:
        data = parse_def_file(def_filename.split('.def')[0], def_file.read())

        with open(def_filename.replace('.def', '.yaml'), 'w') as yaml_file:
            yaml_file.write(data)
