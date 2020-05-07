class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        running_total = 0
        for i in range(1, n+1):
            if n%i == 0:
                running_total += i
        return running_total        


