from Tkinter import *
import time, os
import thread
from datetime import datetime
import threading



current_milli_time = lambda: int(round(time.time() * 1000))

print current_milli_time
