import time

class Stopwatch:
    stopwatches = []

    def __init__(self, name="Stopwatch", stopPin=40):
        # setup a stopwatch
        self.stopwatches.append(name)
        self.name = name
        self.start_time = 0
        self.running = False
        self.duration = 0
        self.tgtTime = 1 * 24 * 60 * 60  # 1 day
        self.states = ["Not Started", "Running", "Stopped", "Failed", "Passed"]
        self.testStatus = 0  # "Not Started",
        self.remainingTestTime = self.tgtTime - self.getCurrentDuration()

    def getName(self):
        return str(self.name)

    def getCurrentDuration(self, now=time.time()):
        duration = self.duration
        if self.running:
            duration = duration + (now - self.start_time)
        return duration

    def getTargetTime(self):
        return self.tgtTime

    def setTargetTime(self, secs):
        self.tgtTime = secs
        print("stopwatch tgtTime: " + str(self.tgtTime))

    def getRemainingTestTime(self, now=time.time()):
        tgt = self.getTargetTime()
        dur = self.getCurrentDuration(now=now)
        remaining = tgt - dur
        self.remainingTestTime = remaining
        return remaining

    def getRunning(self):
        return self.running

    def start(self):
        # Implement your starting of the timer code here
        self.start_time = time.time()
        self.running = True

    def stop(self):
        print("Stopwatch>Stop")
        # Implement your stop timer logic
        self.duration = self.duration + (time.time() - self.start_time)
        self.running = False

    def reset(self):
        # Implement your watch reset logic here
        self.duration = 0
        self.start_time = time.time()
        if not self.getRunning():
            self.remainingTestTime = self.tgtTime
        else:
            self.remainingTestTime = self.tgtTime - self.getCurrentDuration()

    def display_time(self):
        # Return the time to display on the GUI
        now = time.time()
        if not self.running:
            self.startTime = now
        elapsed = self.duration + (time.time() - self.start_time)
        display = self.sec2time(elapsed, 0)
        return display

    def display_remainingTime(self, now=time.time()):
        now = now
        remainingTime = self.getRemainingTestTime(now=now)
        if remainingTime < 0:
            remainingTime = 0
            self.testStatus = "Passed"
        display = self.sec2time(remainingTime, 0)
        return display

    def sec2time(self, sec, n_msec=3):
        ''' Convert seconds to 'D days, HH:MM:SS.FFF' '''
        if hasattr(sec, '__len__'):
            return [self.sec2time(s) for s in sec]
        m, s = divmod(sec, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        # if n_msec > 0:
        pattern = '%%02d:%%02d:%%0%d.%df' % (n_msec + 2, n_msec)
        return ('%d:' + pattern) % (d, h, m, s)
