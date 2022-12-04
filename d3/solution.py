def parse(data):
    f = open(data).read()
    return [line for line in f.splitlines()]

def get_prio(letter):
  if letter.isupper():
    return ord(letter) - 38
  return ord(letter) - 96

# part 1 
def dup_sum(data):
  mid = len(data) // 2
  first, second = set(data[:mid]), set(data[mid:])
  dup = first & second
  return sum(get_prio(i) for i in dup)

def p1(data):
  sum = 0
  for x in data:
    sum += dup_sum(x)
  return sum

# part 2
def get_dup(group):
  sets = [set(g) for g in group]
  dup = sets[0]
  for x in sets[1:]:
    dup &= x
  return list(dup)[0]

def p2(data):
  sum = 0
  group = []
  for x in data:
    group.append(x)
    if len(group) == 3:
      badge = get_dups(group)
      sum += get_prio(badge)
      group.clear()
  return sum


data = parse('input')
print(p1(data))
print(p2(data))
