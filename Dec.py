def call (func):
      def warp (*args,**kwgs):
            i = func(*args,**kwgs)
            print ("okay")
            def warp_2 (*args, **kwgs):
                  i = func(*args, **kwgs)
                  print ("not okay")
                  return i 
            return i 
      return warp 

@call
def sum ():
      print ("call")

print(sum())