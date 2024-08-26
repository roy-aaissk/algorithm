op = ["+", "-", "*", "/", ""]
for i in range(1000, 10000):
    l = [a for a in str(i)]
    for j in op:
        for o in op:
            for r in op:
                val = l[0] + j + l[1] + o + l[2] + r + l[3]
                try:
                    if i == eval(val) and  len(val) > 4:
                        print(i)
                except (ZeroDivisionError, SyntaxError):
                    continue
