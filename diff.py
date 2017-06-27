
def gen_diff(text1, text2):

    new_lines = ''
    changed_lines = ''

    file1Contents = dict()
    for line in text1.split('\n'):
      if '=' in line:
        key = line[:line.index('=')]
        val = line[line.index('=') + 1:]
        file1Contents[key] = val

    for line in text2.split('\n'):
      if '=' in line:
        key = line[:line.index('=')]
        val = line[line.index('=') + 1:]

        print('Lookat line ' + line)
        print(' key ' + key)
        print(' file1Contents[' + key + '] == ' + file1Contents[key])

        if key not in file1Contents:
          changed_lines += line + '\n'
        if key in file1Contents and val != file1Contents[key]:
          new_lines += line + '\n'

    diff = ''
    if new_lines:
        diff += '<<    Added    >>\n\n'
        diff += new_lines
    if changed_lines:
        diff += '<<   Changed   >>\n\n'

    return diff
