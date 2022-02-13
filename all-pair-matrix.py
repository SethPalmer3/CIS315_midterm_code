from matrix import matrix


def all_pair_matrix(m: matrix, hops: int) -> matrix:

    for i in range(hops):
        m = m * m
    return m

def main():

    #n0 -> n1 w:1
    #n0 -> n2 w:1
    m = matrix(4, 4)
    m.setitem(0, 1, 1)
    m.setitem(0, 2, 1)
    m.setitem(1, 3, 1)
    #print(m)
    m = all_pair_matrix(m, 1)
    print(m)

if __name__ == "__main__":
    main()