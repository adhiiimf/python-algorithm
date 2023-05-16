def cariPermutasi(x,y):
    hasil = []
    ylen = len(y[0])
    h = len(y)
    z = len(y[0])
    for i in range(len(x)):
        for j in range(h):
            # print("j: ",j)
            b = j
            # print(h-1)
            if j <= h-1:
                if x[i:z] == y[j]:
                    # print(x[i:z])
                    b = j + 1
                    # print(y[b])
                    for c in range(h):
                        # print("txt: ",x[z:z+ylen])
                        # print("cmp: ",y[c])
                        if x[z:z+ylen] == y[c] and x[z:z+ylen]!=x[i:z]:
                             hasil.append(i)
                            #  print("index: ", i)
        z = z + 1
    print(hasil)

cariPermutasi("blablabloblobla", ["bla", "blo"])
cariPermutasi("testtosttosttest", ["test", "tost"])
cariPermutasi("lololilaloli", ["la", "li", "lo"])
cariPermutasi("hahahohohohohahahahahoho", ["haha", "hoho"])
cariPermutasi("hahahohohohohahahahahohohehehahahehehehehaha", ["haha", "hoho","hehe"])