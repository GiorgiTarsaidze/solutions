def accum(st):
    final = ""

    for i in range(len(st)):
        final += st[i].upper()
        final += st[i].lower() * i + "-"

    return final[:-1]