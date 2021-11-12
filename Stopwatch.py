"""
   @ Author - Deepak Kumar
   @ Date - 10-NOV-2021
   @ Time - 14:56
   @ Title - Write a Stopwatch Program for measuring the time that elapses between
             the start and end clicks
"""
import time
class StopWatch:
  @staticmethod
  def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

input("Press Enter to start: ")
start_time = time.time()
print("Timer Started")
input("Press Enter to stop: ")
end_time = time.time()
print("Timer Stop")
time_lapsed = end_time - start_time
stopWatch = StopWatch()
stopWatch.time_convert(time_lapsed)