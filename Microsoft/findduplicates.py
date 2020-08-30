def find_duplicates(array):
  bv = [0] * 512
  duplicates = set()
  for n in array:
    bit = 1 << (n % 64)
    if bv[n // 64] & bit:
      duplicates.add(n)
    else:
      bv[n // 64] |= bit
  return duplicates
array = [1, 2, 3, 4, 55, 20000, 20001, 20002, 20003, 17, 18, 19, 20, 22, 23,
             7, 2, 3, 3, 55, 20002, 20004, 20005, 20006, 16, 18, 22, 24, 25, 26]
print(find_duplicates(array))


