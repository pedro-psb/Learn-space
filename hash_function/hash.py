depth = 7
buckets_per_level = 20
array_size = buckets_per_level ** depth

hash_code = 0
for i in range(depth):
    char_number = (ord('z') - ord('a')) % buckets_per_level
    hash_code += char_number ** depth - i - 1


print(f"{array_size:,d}")
print(f"{hash_code:,d}")