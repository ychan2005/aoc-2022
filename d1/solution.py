#part 1
sums = []
i = 0
with open('input', 'r') as f:
  lines = f.readlines()
  for line in lines:
    if line.strip() == '':
      i += 1
    else:
      if i < len(sums):
        sums[i] += int(line)
      else:
        sums.append(int(line))
print(max(sums))

# part 2
sums.sort(reverse=True)
ans = sums[0] + sums[1] + sums[2]
print(ans)