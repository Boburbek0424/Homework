#savol biroz tushunarsiz ekan shuning uchun map ishlatdim
x1, y1, x2, y2 = map(int, input("Enter coordinates in this format without brackets (x1 y1 x2 y2): ").split())
p = 2*(abs(y2-y1)+abs(x2-x1))
a = abs(y2-y1)*abs(x2-x1)
print(f"Perimeter: {p}\nArea: {a}")
