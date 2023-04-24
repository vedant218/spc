import re

macro_defs = {}
labels = {}
output = []


def add_label(name):
    if name not in labels:
        labels[name] = len(labels)


def replace_macro_invocation(line):
    parts = line.strip().split()
    if parts and parts[0] in macro_defs:
        macro_name = parts[0]
        macro_args = parts[1:]
        macro_label = labels[macro_name]
        return f'L{macro_label} {macro_name} {" ".join(macro_args)}'
    else:
        return line.strip()


def process_line(line):
    if re.match(r'\s*MACRO\s+', line):
        parts = line.strip().split()
        macro_name = parts[1]
        macro_args = parts[2:]
        macro_defs[macro_name] = macro_args
        add_label(macro_name)
    else:
        output.append(replace_macro_invocation(line))


with open('input.asm') as f:
    for line in f:
        process_line(line)

with open('output.asm', 'w') as f:
    for i, line in enumerate(output):
        f.write(f'L{i} {line}\n')
