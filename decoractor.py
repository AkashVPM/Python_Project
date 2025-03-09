import time 
import logging

def clock (func):
      def warp ():
            s_t = time.time()   # s_t = start_time 
            res = func()
            e_t = time.time()   # e_t = End_time
            return (f"runstart time is {s_t} run end time is {e_t} The time to run the function is {(e_t - s_t)} seconds")
      return warp

def log_call (func):
      def warp():
            res = func()
            log = logging.info(f"Function {func.__name__} was called")
            return log
      return warp

@clock
@log_call

def fun ():
      file = open ("Actuator_Body.stl", "r")
      return file.read ()
print (fun())


# def fun (file):
#       with open (file, "r")as file:
#             return file.read ()

# print (fun("Actuator_Body.stl"))