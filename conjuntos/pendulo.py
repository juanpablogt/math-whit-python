from sympy import FiniteSet,pi

def periodo(lenght,g):
    g = 9.8
    t = 2*pi*(lenght/g)**0.5

    return t

if __name__ == '__main__':

    L = FiniteSet(15,2,3,4,5,6,7,8,9,10,11,2,22,22,33,444,5556,77)
    g_values = FiniteSet(9.8, 9.78, 9.83)
    print('{0:^15}{1:^15}{2:^15}'.format('Length(cm)', 'Gravity(m/s^2)', 'Time Period(s)'))
    for elem in L*g_values:
        l = elem[0]
        g = elem[1]
        t = periodo(l/100, g)
        print('{0:^15}{1:^15}{2:^15.3f}'.format(float(l), float(g), float(t)))