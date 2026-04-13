nums1 = { 1, 2, 3 }
nums2 = { 3, 4, 5 }

pares1 = { 2, 4, 6, 8 }
pares2 = { 2, 4 }

intersection = nums1 & nums2
union = nums1 | nums2
difference1 = nums1 - nums2
difference2 = nums2 - nums1
symmetric_difference = nums1 ^ nums2

issubset1 = pares1 < pares2 # 1 é sub de 2 False
issuperset1 = pares1 > pares2 # 1 NÃO é sub de 2 True

issubset2 = pares2 < pares1 # 2 é sub de 1 True
issuperset2 = pares2 > pares1 # 2 NÃO é sub de 1 False

print(f"intersection: ", intersection)
print(f"union: ", union)
print(f"difference1: ", difference1)
print(f"difference2: ", difference2)
print(f"symmetric_difference: ", symmetric_difference)
print(f"issubset1: ", issubset1)
print(f"issuperset1: ", issuperset1)
print(f"issubset2: ", issubset2)
print(f"issuperset2: ", issuperset2)
