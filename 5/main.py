DIFF_THRESHOLD = 1e-40


class Fixed:
    FREE = 0
    A = 1
    B = 2


class Node:
    def __init__(self, v=0.0, f=Fixed.FREE):
        self.voltage = v
        self.fixed = f


def set_boundary(m):
    m[1][1] = Node(1.0, Fixed.A)
    m[6][7] = Node(-1.0, Fixed.B)


def calc_difference(m, d):
    height = len(m)
    width = len(m[0])
    total = 0

    for i in range(height):
        for j in range(width):
            v = 0
            n = 0
            if i != 0:
                v += m[i - 1][j].voltage
                n += 1
            if j != 0:
                v += m[i][j - 1].voltage
                n += 1
            if i < height - 1:
                v += m[i + 1][j].voltage
                n += 1
            if j < width - 1:
                v += m[i][j + 1].voltage
                n += 1
            v = m[i][j].voltage - v / n

            d[i][j].voltage = v
            if m[i][j].fixed == Fixed.FREE:
                total += v ** 2
    return total


def iter(m):
    height = len(m)
    width = len(m[0])
    difference = [[Node() for _ in range(width)] for _ in range(height)]

    while True:
        set_boundary(m)
        if calc_difference(m, difference) < DIFF_THRESHOLD:
            break
        for i, di in enumerate(difference):
            for j, dij in enumerate(di):
                m[i][j].voltage -= dij.voltage

    cur = [0] * 3
    for i, di in enumerate(difference):
        for j, dij in enumerate(di):
            cur[m[i][j].fixed] += (dij.voltage *
                                   (bool(i) + bool(j) + (i < height - 1) + (j < w - 1)))

    return (cur[Fixed.A] - cur[Fixed.B]) / 2.0


w = h = 10
mesh = [[Node() for j in range(w)] for i in range(h)]
print(f'R = {2 / iter(mesh):.16f}')
