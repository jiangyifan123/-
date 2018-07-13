import random
class Random:#验证码
    def Random(self, len):
        ans = ''
        len = int(len)
        for i in range(len):
            d = random.randint(0, 300)
            if d % 3 == 0:
                d %= 26
                ans += chr(d + 65)
            elif d % 3 == 1:
                d %= 26
                ans += chr(d + 97)
            elif d % 3 == 2:
                ans += str(d % 10)
        return ans
