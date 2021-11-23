cust = 10
col = 2
row = cust/col

if (cust % col) == 0:
    row == cust//col
else:
    row == (cust//col) + 1


if i in range (0, row):
    if j in range (1, col + 1):
       seat = i * col + j
    if seat > cust:
        break
    print("seat"+str(seat),end='')
print()
