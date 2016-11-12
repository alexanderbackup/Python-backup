# solution.py
import sys

sys.argv[0] = 'solution.py'
try:
    problem = sys.argv[1]
except:
    problem = False
    examples = ['2x^3+x', '1', 'x^4+10x^3', '1+x^2', '3x^2']

class PolynomsAndDerivates:
    
    def __init__(self, polynom):
        self.polynom = polynom.split('+')
        self.equation = []

    def highest_degree(self):
        for i in self.polynom:
            if '^' in i:
                self.equation.append((i, int(i[i.index('^')+1:])))
            elif 'x' in i and '^' not in i:
                self.equation.append((i, 1))
            else:
                self.equation.append((i, 0))
        self.equation = sorted(self.equation, key=lambda x: x[1], reverse=True)
        return self.equation # self.equation = [('', 0), ]
    
    def repr_derivative(self):
        new = 'The derivative of f(x) = '
        #smth = sorted(self.equation_degree(), key=lambda x: x[1], reverse=True)
        for ss in self.equation:
            if ss[1] == 0:
                new += ss[0]
            else:
                new += self.placing_stars(ss)
            if ss != self.equation[-1]:
                new += ' + '
        return new + ' is:'


    def placing_stars(self, ss): # ss is a tuple: ('x^2', 2)
        if ss[0].index('x') == 0:
            return ss[0]
        else:
            return ss[0][:ss[0].index('x')] + '*' + ss[0][ss[0].index('x'):]


class CalculatePolynoms(PolynomsAndDerivates):

    def __init__(self, *args):
        super().__init__(*args)
        self._equation = self.highest_degree()

    def calculate_derivative(self):
        temp_equations = [] # = [i for i in self._equation if i[1] != 0]
        for i in self._equation:
            if temp_equations == []:
                temp_equations.append(i)
            elif i[1] == temp_equations[-1][1] and i[1] != 0:
                try:
                    s_int = int(i[0][:i[0].index('x')])
                except:
                    s_int = 1
                try:
                    temp_int = int(temp_equations[-1][0][:temp_equations[-1][0].index('x')])
                except:
                    temp_int = 1
                temp_equations[-1] = (str(s_int+temp_int)+i[0][i[0].index('x'):], i[1])
            else:
                temp_equations.append(i)
        self._equation = temp_equations
        return self._equation

    def repr_calculated_derivative(self):
        new = "f'(x) = "
        count = len(self._equation)
        for el in self._equation:
            if count < len(self._equation) and el[1] != 0:
                new += ' + '
            if el[1] == 0:
                if len(self._equation) == 1:
                    new += el[0]
            elif el[1] == 1:
                if el[0].index('x') == 0:
                    new += '1'
                else:
                    new += el[0][:el[0].index('x')]
            elif el[1] == 2:
                if el[0].index('x') == 0:
                    new += '2x'
                else:
                    temp = int(el[0][:el[0].index('x')]) * el[1]
                    new += str(temp) + 'x'
            else:
                if el[0].index('x') == 0:
                    new += str(el[1]) + '*' + 'x^' + str(el[1]-1)
                else:
                    temp = int(el[0][:el[0].index('x')]) * el[1]
                    new += str(temp) + '*' + 'x^' + str(el[1]-1)
            count -= 1
        return new

if __name__ == '__main__':
    if problem:
        foo = PolynomsAndDerivates(problem)
        bar = CalculatePolynoms(problem)
        foo.highest_degree()
        print(foo.repr_derivative())
        print(bar.calculate_derivative())
        print(bar.repr_calculated_derivative())
        #print(foo.calculate_derivative())
    else:
        for _problem in examples:
            foo = PolynomsAndDerivates(_problem.strip("'"))
            foo.highest_degree()
            print(foo.repr_derivative())
            print(foo.calculate_derivative())


# Old calculating method
#
#    def calculate_derivative(self):
#        new = "f'(x) = "
#        for el in self.equation:
#            if el != self.equation[0] and el[1] != 0:
#                new += ' + '
#            if el[1] == 0:
#                if len(self.equation) == 1:
#                    new += el[0]
#            elif el[1] == 1:
#                if el[0].index('x') == 0:
#                    new += '1'
#                else:
#                    new += el[0][:el[0].index('x')]
#            elif el[1] == 2:
#                if el[0].index('x') == 0:
#                    new += '2x'
#                else:
#                    temp = int(el[0][:el[0].index('x')]) * el[1]
#                    new += str(temp) + 'x'
#            else:
#                if el[0].index('x') == 0:
#                    new += str(el[1]) + '*' + 'x^' + str(el[1]-1)
#                else:
#                    temp = int(el[0][:el[0].index('x')]) * el[1]
#                    new += str(temp) + '*' + 'x^' + str(el[1]-1)

#        return new
