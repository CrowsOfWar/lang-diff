
def gen_diff(text1, text2):

    changed = ''

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

        keyChanged = key in file1Contents and val != file1Contents[key]
        keyAdded = key not in file1Contents
        if keyChanged or keyAdded:
          # changed value of (key) from (file1Contents[key]) -> (val)
          changed += line + '\n'

    return changed
