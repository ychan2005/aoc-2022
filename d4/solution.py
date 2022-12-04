

def parse(data):
    f = open(data).read()
    return [line for line in f.splitlines()]

def is_sub(r1, r2):
  return r1.issubset(r2) or r2.issubset(r1)

def p1(args):
  total = 0
  for line in args:
    pair = line.split(',')
    r = pair[0].split('-')
    l1 = [i for i in range(int(r[0]), int(r[1]) + 1)]
    r = pair[1].split('-')
    l2 = [i for i in range(int(r[0]), int(r[1]) + 1)]
    if is_sub(set(l1), set(l2)):
      total += 1
  return total

def p2(args):
  total = 0
  for line in args:
    pair = line.split(',')
    r = pair[0].split('-')
    l1 = [i for i in range(int(r[0]), int(r[1]) + 1)]
    r = pair[1].split('-')
    l2 = [i for i in range(int(r[0]), int(r[1]) + 1)]
    if set(l1).intersection(set(l2)):
      total += 1
  return total

data = parse('input')
print(p1(data))
print(p2(data))
