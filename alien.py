import matplotlib.pyplot as plt

d1 = int(input("Enter value of d1:"))
d2 = int(input("Enter value of d2:"))
d3 = int(input("Enter value of d3:"))
d4 = int(input("Enter value of d4:"))
x = int(input("Enter x coordinate"))
y = int(input("Enter y coordinate"))
a = 0
b = 0
plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
         marker='*', markerfacecolor='blue', markersize=2)


plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('Path followed by the aliens')


def pos_pos(a, b):
    ne = 0
    nw = 0
    se = 0
    sw = 0
    while (a != x) and (b != y):
        if x < y:
            while a != x:
                if ne <= d1 - 1:
                    a += 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    ne += 1
                    nw = 0
                    se = 0
                else:
                    a -= 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    nw += 1

                    a += 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    se = 1

                    ne = 0
            while b != y:
                if (y - b) % 2 == 0:
                    while b <= y - 1:
                        a -= 1
                        b += 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                        a += 1
                        b += 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                else:
                    while b <= y - 2:
                        a -= 1
                        b += 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                        a += 1
                        b += 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                    a -= 0.5
                    b += 0.5
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    a += 0.5
                    b += 0.5
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
        if x > y:
            while b != y:
                if ne <= d1 - 1:
                    a += 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    ne += 1
                    nw = 0
                    se = 0
                else:
                    a -= 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    nw += 1

                    a += 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    se = 1

                    ne = 0
            while a != x:
                if (x - a) % 2 == 0:
                    while a <= x - 1:
                        a += 1
                        b += 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                        a += 1
                        b -= 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                else:
                    while a <= x - 2:
                        a += 1
                        b += 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                        a += 1
                        b -= 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                    a += 0.5
                    b += 0.5
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    a += 0.5
                    b -= 0.5
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
        if x == y:
            while b != y:
                if ne <= d1 - 1:
                    a += 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    ne += 1
                    nw = 0
                    se = 0
                else:
                    a -= 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    nw += 1

                    a += 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    se = 1

                    ne = 0

    plt.show()


def neg_pos(a, b):
    ne = 0
    nw = 0
    se = 0
    sw = 0
    while (a != x) and (b != y):
        if -x < y:
            while a != x:
                if nw <= d2 - 1:
                    a -= 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    nw += 1
                    ne = 0
                    sw = 0
                else:
                    a += 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    ne += 1

                    a -= 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    sw = 1

                    nw = 0
            while b != y:
                if (y - b) % 2 == 0:
                    while b <= y - 1:
                        a += 1
                        b += 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                        a -= 1
                        b += 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                else:
                    while b <= y - 2:
                        a += 1
                        b += 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                        a -= 1
                        b += 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                    a += 0.5
                    b += 0.5
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    a -= 0.5
                    b += 0.5
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
        if -x > y:
            while b != y:
                if nw <= d2 - 1:
                    a -= 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    nw += 1
                    ne = 0
                    sw = 0
                else:
                    a += 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    ne += 1

                    a -= 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    sw = 1

                    nw = 0
            while a != x:
                if (x - a) % 2 == 0:
                    while a >= x + 1:
                        a -= 1
                        b -= 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                        a -= 1
                        b += 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                else:
                    while a >= x + 2:
                        a -= 1
                        b -= 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                        a -= 1
                        b += 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                    a -= 0.5
                    b -= 0.5
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    a -= 0.5
                    b += 0.5
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
        if -x == y:
            while b != y:
                if nw <= d2 - 1:
                    a -= 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    nw += 1
                    ne = 0
                    sw = 0
                else:
                    a += 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    ne += 1

                    a -= 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    sw += 1

                    nw = 0

    plt.show()


def neg_neg(a, b):
    ne = 0
    nw = 0
    se = 0
    sw = 0
    while (a != x) and (b != y):
        if -x < -y:
            while a != x:
                if sw <= d3 - 1:
                    a -= 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    sw += 1
                    se = 0
                    nw = 0
                else:
                    a += 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    se += 1

                    a -= 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    nw = 1

                    sw = 0
            while b != y:
                if (y - b) % 2 == 0:
                    while b >= y + 1:
                        a += 1
                        b -= 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                        a -= 1
                        b -= 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                else:
                    while b >= y + 2:
                        a += 1
                        b -= 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                        a -= 1
                        b -= 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                    a += 0.5
                    b -= 0.5
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    a -= 0.5
                    b -= 0.5
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
        if -x > -y:
            while b != y:
                if sw <= d3 - 1:
                    a -= 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    sw += 1
                    se = 0
                    nw = 0
                else:
                    a += 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    se += 1

                    a -= 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    nw = 1

                    sw = 0
            while a != x:
                if (x - a) % 2 == 0:
                    while a >= x + 1:
                        a -= 1
                        b += 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                        a -= 1
                        b -= 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                else:
                    while a >= x + 2:
                        a -= 1
                        b += 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                        a -= 1
                        b -= 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                    a -= 0.5
                    b += 0.5
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    a -= 0.5
                    b -= 0.5
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
        if x == y:
            while b != y:
                if sw <= d3 - 1:
                    a -= 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    sw += 1
                    se = 0
                    nw = 0
                else:
                    a += 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    se += 1

                    a -= 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    nw += 1

                    sw = 0

    plt.show()


def pos_neg(a, b):
    ne = 0
    nw = 0
    se = 0
    sw = 0
    while (a != x) and (b != y):
        if x < -y:
            while a != x:
                if se <= d4 - 1:
                    a += 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    se += 1
                    sw = 0
                    ne = 0
                else:
                    a -= 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    sw += 1

                    a += 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    ne = 1

                    se = 0
            while b != y:
                if (y - b) % 2 == 0:
                    while b >= y + 1:
                        a -= 1
                        b -= 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                        a += 1
                        b -= 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                else:
                    while b >= y + 2:
                        a -= 1
                        b -= 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                        a += 1
                        b -= 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                    a -= 0.5
                    b -= 0.5
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    a += 0.5
                    b -= 0.5
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
        if x > y:
            while b != y:
                if se <= d4 - 1:
                    a += 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    se += 1
                    sw = 0
                    ne = 0
                else:
                    a -= 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    sw += 1

                    a += 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    ne += 1

                    se = 0
            while a != x:
                if (x - a) % 2 == 0:
                    while a <= x - 1:
                        a += 1
                        b += 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                        a += 1
                        b -= 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                else:
                    while a <= x - 2:
                        a += 1
                        b += 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                        a += 1
                        b -= 1
                        plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                                 marker='*', markerfacecolor='blue', markersize=2)
                    a += 0.5
                    b += 0.5
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    a += 0.5
                    b -= 0.5
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
        if -x == y:
            while b != y:
                if se <= d4 - 1:
                    a += 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    se += 1
                    sw = 0
                    ne = 0
                else:
                    a -= 1
                    b -= 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    sw += 1

                    a += 1
                    b += 1
                    plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                             marker='*', markerfacecolor='blue', markersize=2)
                    ne += 1

                    se = 0

    plt.show()

def pos_zero(a,b):
    while a != x:
        if (x - a) % 2 == 0:
            while a <= x - 1:
                a += 1
                b += 1
                plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                         marker='*', markerfacecolor='blue', markersize=2)
                a += 1
                b -= 1
                plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                         marker='*', markerfacecolor='blue', markersize=2)
        else:
            while a <= x - 2:
                a += 1
                b += 1
                plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                         marker='*', markerfacecolor='blue', markersize=2)
                a += 1
                b -= 1
                plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                         marker='*', markerfacecolor='blue', markersize=2)
            a += 0.5
            b += 0.5
            plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                     marker='*', markerfacecolor='blue', markersize=2)
            a += 0.5
            b -= 0.5
            plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                     marker='*', markerfacecolor='blue', markersize=2)
    plt.show()
def neg_zero(a,b):
    while a != x:
        if (x - a) % 2 == 0:
            while a >= x + 1:
                a -= 1
                b -= 1
                plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                         marker='*', markerfacecolor='blue', markersize=2)
                a -= 1
                b += 1
                plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                         marker='*', markerfacecolor='blue', markersize=2)
        else:
            while a >= x + 2:
                a -= 1
                b -= 1
                plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                         marker='*', markerfacecolor='blue', markersize=2)
                a -= 1
                b += 1
                plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                         marker='*', markerfacecolor='blue', markersize=2)
            a -= 0.5
            b -= 0.5
            plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                     marker='*', markerfacecolor='blue', markersize=2)
            a -= 0.5
            b += 0.5
            plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                     marker='*', markerfacecolor='blue', markersize=2)
    plt.show()
def zero_pos(a,b):
    while b != y:
        if (y - b) % 2 == 0:
            while b <= y - 1:
                a -= 1
                b += 1
                plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                         marker='*', markerfacecolor='blue', markersize=2)
                a += 1
                b += 1
                plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                         marker='*', markerfacecolor='blue', markersize=2)
        else:
            while b <= y - 2:
                a -= 1
                b += 1
                plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                         marker='*', markerfacecolor='blue', markersize=2)
                a += 1
                b += 1
                plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                         marker='*', markerfacecolor='blue', markersize=2)
            a -= 0.5
            b += 0.5
            plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                     marker='*', markerfacecolor='blue', markersize=2)
            a += 0.5
            b += 0.5
            plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                     marker='*', markerfacecolor='blue', markersize=2)
    plt.show()
def zero_neg(a, b):
    while b != y:
        if (y - b) % 2 == 0:
            while b >= y + 1:
                a += 1
                b -= 1
                plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                         marker='*', markerfacecolor='blue', markersize=2)
                a -= 1
                b -= 1
                plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                         marker='*', markerfacecolor='blue', markersize=2)
        else:
            while b >= y + 2:
                a += 1
                b -= 1
                plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                         marker='*', markerfacecolor='blue', markersize=2)
                a -= 1
                b -= 1
                plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                         marker='*', markerfacecolor='blue', markersize=2)
            a += 0.5
            b -= 0.5
            plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                     marker='*', markerfacecolor='blue', markersize=2)
            a -= 0.5
            b -= 0.5
            plt.plot(a, b, color='green', linestyle='dashed', linewidth=3,
                     marker='*', markerfacecolor='blue', markersize=2)
    plt.show()

if x > 0 and y > 0:
    plt.xlim(-(x + 5), x + 5)
    plt.ylim(-(y + 5), y + 5)
    pos_pos(a, b)
elif x < 0 and y > 0:
    plt.xlim(x - 5, -(x - 5))
    plt.ylim(-(y + 5), y + 5)
    neg_pos(a, b)
elif x < 0 and y < 0:
    plt.xlim(x - 5, -(x - 5))
    plt.ylim(y - 5, -(y - 5))
    neg_neg(a, b)
elif x > 0 and y < 0:
    plt.xlim(-(x+5), x+5)
    plt.ylim(y-5, -(y-5))
    pos_neg(a, b)
elif x > 0 and y == 0:
    plt.xlim(-(x + 5), x + 5)
    plt.ylim(y - 5, -(y - 5))
    pos_zero(a, b)
elif x < 0 and y == 0:
    plt.xlim(x - 5, -(x - 5))
    plt.ylim(y - 5, (y + 5))
    neg_zero(a, b)
elif x == 0 and y > 0:
    plt.xlim(x-5, x+5)
    plt.ylim(-(y+5), y+5)
    zero_pos(a, b)
elif x == 0 and y < 0:
    plt.xlim(x-5, x+5)
    plt.ylim(y-5, -(y-5))
    zero_neg(a, b)

