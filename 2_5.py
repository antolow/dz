print('a b c')
for a in range (2):
    for b in range (2):
        for c in range (2):
            if (not(a) or b or not(c)) and (b or not(c)):
                 print(a, b, c)
            
