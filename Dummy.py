def mul (num):
      def warp():
            value = num()
            return value * 2
      return warp

def square (num):
      def warp ():
            value = num()
            return value**2
      return warp


@square
@mul
def test_1():
      return 2

@mul
@square
def test_2():
      return 2

print(test_1())
print (test_2())
