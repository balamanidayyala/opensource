input_data=input().strip()
X, Y, Z=map(int, input_data.split())
remaining_weight=Z-Y
if remaining_weight<0:
    print(0)
else:
    max_mangoes=remaining_weight // X
    print(max_mangoes)
