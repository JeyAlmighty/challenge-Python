s = "aabbcdde"

# Output:
# "c"
t = ""

for i in s:
    if s.count(i) == 1:
       print(i)
       break
