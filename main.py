import random
import math
import matplotlib.pyplot as plt


SCREEN_HEIGHT = 200
SCREEN_WIDTH = 200


class Triangle:
    def __init__(self):
        self.A = [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)]
        self.B = [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)]
        self.C = [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)]

    def check_triangle(self):
        area = 0.5*(self.A[0]*(self.B[1]-self.C[1]) + self.B[0]*(self.C[1]-self.A[1])+ self.C[0]*(self.A[1]-self.B[1]))
        if area!=0:
            return
        else:
            self.A = [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)]
            self.B = [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)]
            self.C = [random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)]
            self.check_triangle()

def midpoint(p1, p2):
    return [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2]

def construct(triangle, point):
    ls = [triangle.A, triangle.B, triangle.C]
    for i in range(0, 100):
        j = random.randint(0, 2)
        np = midpoint(ls[j],point)
        plt.plot(np[0], np[1], marker = 'o', color = 'black', markersize = 0.3)
        point = np
    plt.show()



if __name__ == '__main__':
    triangle = Triangle()
    x_min = min(triangle.A[0], triangle.B[0], triangle.C[0])
    x_max = max(triangle.A[0], triangle.B[0], triangle.C[0])
    y_min = min(triangle.A[1], triangle.A[1], triangle.C[1])
    y_max = max(triangle.A[1], triangle.A[1], triangle.C[1])
    #point = [random.randint(x_min, x_max), random.randint(y_min, y_max)]
    point = [(triangle.A[0]+triangle.B[0]+triangle.C[0])/3,(triangle.A[1]+triangle.B[1]+triangle.C[1])/3 ]
    print(triangle.A)
    print(triangle.B)
    print(point)
    #plt.plot(point[0], point[1], marker='o', color='red')
    plt.plot(triangle.A[0],triangle.A[1], marker = 'o', color = 'black')
    plt.plot(triangle.B[0], triangle.B[1], marker = 'o', color='black')
    plt.plot(triangle.C[0], triangle.C[1], marker = 'o', color='black')
    #plt.show()
    construct(triangle, point)
    print("done")