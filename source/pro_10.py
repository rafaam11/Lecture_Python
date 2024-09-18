class Shp:

    def __init__(self,garo,sero):
        self.garo = garo
        self.sero = sero
        self.area = garo * sero

    def show(self):
        print("도형의 가로는 {} , 세로는 {} 입니다.".format(self.garo,self.sero))

    def getArea(self):
        print("도형의 넓이는 {} 입니다.".format(self.area))

class Rec(Shp):

    def __init__(self, garo, sero):
        Shp.__init__(self,garo,sero)

    def show(self):
        print("도형의 가로는 {} , 세로는 {} 입니다.".format(self.garo, self.sero))

    def getArea(self):
        print("도형의 넓이는 {} 입니다.".format(self.area))

class Tri(Shp):

    def __init__(self, garo, sero):
        Shp.__init__(self,garo,sero)
        self.area = 0.5 * garo * sero

    def show(self):
        print("도형의 가로는 {} , 세로는 {} 입니다.".format(self.garo, self.sero))

    def getArea(self):
        print("도형의 넓이는 {} 입니다.".format(self.area))

class Cir(Shp):

    def __init__(self,radius):
        Shp.__init__(self, radius, radius)
        self.radius = radius
        self.area = radius * radius

    def show(self):
        print("도형의 반지름은 {} 입니다.".format(self.radius))

    def getArea(self):
        print("도형의 넓이는 {} pi 입니다.".format(self.area))

shp = Shp(3,4)
rec = Rec(2,5)
tri = Tri(4,5)
cir = Cir(7)

shp.show()
shp.getArea()
rec.show()
rec.getArea()
tri.show()
tri.getArea()
cir.show()
cir.getArea()

