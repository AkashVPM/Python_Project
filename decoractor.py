import time 
import logging

def clock (func):
      def warp (*args, **kwgs):
            s_t = time.time()   # s_t = start_time 
            res = func(*args, **kwgs)
            e_t = time.time()   # e_t = End_time
            print (f"runstart time is {s_t} run end time is {e_t} The time to run the function is {(e_t - s_t)} seconds")
            return res
      return warp

def log_call (func):
<<<<<<< HEAD
      def warp():
            res = func(*args, **kwgs)
            log = logging.info(f"Function {func.__name__} was called")
            print (log)
=======
      def warp(*args, **kwgs):
            res = func(*args, **kwgs)
            log = logging.info(f"Function {func.__name__} was called")
            print(log)
>>>>>>> f85d56b0e0ec0d14d29a8b68ac0deefe3b834167
            return res
      return warp

@clock
@log_call

def fun ():
      file = open ("Actuator_Body.stl", "r")
      return file

print (fun())


# def fun (file):
#       with open (file, "r")as file:
#             return file.read ()

# print (fun("Actuator_Body.stl"))
