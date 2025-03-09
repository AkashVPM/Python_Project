import time 
import logging

def clock (func):
      def warp ():
            s_t = time.time()   # s_t = start_time 
            res = func()
            time.sleep (2)
            e_t = time.time()   # e_t = End_time
            return f"The time to run the function is {(e_t - s_t):.2f} seconds"
      return warp

def log_call (func):
      def warp():
            print (func())
            print(logging.info(f"Function {func.__name__} was called"))
            # num = func ()
            return func()
      return warp

@clock
@log_call
def fun ():
      file = open ("Actuator_Body.stl", "r")
      # print(file.read())
      return file.read ()
      # return 5

print(fun())