class Quadratic_equations:
    try:
        a = float(input("Enter a (number before x^2): "))
        b = float(input("Enter b (number before x): "))
        c = float(input("Enter c (free member): "))
    except ValueError:
        a = 1
        b = 1
        c = 1
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def calculations(self):
        D = self.b ** 2 - 4 * self.a * self.c # formula of discriminant
        def x1():
            x1 = (-self.b + D ** 0.5) / (self.a * 2) # formula for first root of quadratic equation
            return x1
        def x2():
            x2 = (-self.b - D ** 0.5) / (self.a * 2) # formula for second root of quadratic equation
            return x2
        if type(x1()) == complex or type(x2()) == complex: # check type of roots
            print('Roots not found!')
        elif len(str(x2())) <= 5 and len(str(x1())) <= 5: # we are weeding of (отсеиваем) long float numbers
            print(f'''X1 is {x2()} and X2 is {x1()}.''')
w = Quadratic_equations(a=Quadratic_equations.a, b=Quadratic_equations.b, c=Quadratic_equations.c)
w.calculations()

print('I did it! Finally!')
