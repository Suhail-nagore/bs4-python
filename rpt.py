start = 258523222222
size = 100000

i_start = int(start/size)
i_end=i_start+1
j_start=start%size
j_end=j_start+(int(size/10))

print(i_start)
print(i_end)
print(j_start)
print(j_end)


j_start=j_end+1
j_end=j_start+(int(size/10))

print(i_start+1)
print(i_end+1)
print(j_start+1)
print(j_end+1)

print("\n\n\n\n\n\n\n\n")


j_start=j_end+2
j_end=j_start+(int(size/10))

print(i_start+2)
print(i_end+2)
print(j_start+1)
print(j_end+1)