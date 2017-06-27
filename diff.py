
def gen_diff(text1, text2):

    newLines = ''
    changedLines = ''

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

        if key not in file1Contents:
          changed += line + '\n'
        if key in file1Contents and val != file1Contents[key]:
          newLines += line + '\n'

    return '<< NEW >>\n\n' + newLines + '\n\n<< CHANGED >>\n\n' + changed
