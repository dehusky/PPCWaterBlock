import time

class Stopwatch:
    stopwatches = []

    def __init__(self, name="Stopwatch", stopPin=40):
        # setup a stopwatch
        self.stopwatches.append(name)
        self.name = name
        self.start_time = 0
        self.stopTime = self.start_time
        self.running = False
        self.currentDuration = 0
        self.tgtTime = 1 * 24 * 60 * 60  # 1 day
        self.statusText = ["Ready", "Running", "Paused", "Passed", "Failed"]
        self.testStatus_int = 0  # "Ready",
        self.remainingTestTime = self.tgtTime - self.currentDuration
        self.failed = False

    def start(self):
        print("Stopwatch>Start")
        # Implement your starting of the timer code here
        self.start_time = time.time()
        self.running = True
        self.testStatus_int = 1  # running

    def stop(self):
        print("Stopwatch>Stop")
        now = time.time()
        # Implement your stop timer logic
        self.currentDuration = self.currentDuration + (now - self.start_time)
        self.running = False
        self.stopTime = now

    def reset(self):
        # Implement your watch reset logic here
        self.currentDuration = 0
        self.start_time = time.time()
        self.failed = False
        if not self.running:
            self.remainingTestTime = self.tgtTime
            self.testStatus_int = 0  # ready
        else:
            self.remainingTestTime = self.tgtTime - self.getCurrentDuration()
            self.testStatus_int = 1  # running

    def getCurrentDuration(self, gcd_now=time.time()):
        duration = self.currentDuration
        if self.running == True:
            duration = duration + (gcd_now - self.start_time)
        return duration

    def getRemainingTestTime(self, grtt_now=time.time()):
        tgt = self.getTargetTime()
        dur = self.getCurrentDuration(gcd_now=grtt_now)
        remaining = tgt - dur
        self.remainingTestTime = remaining
        return remaining

    def display_elapsedTime(self, dt_now=time.time()):
        elapsed = self.getCurrentDuration(gcd_now=dt_now)
        display = self.sec2time(elapsed, 0)
        return display

    def update_test_status(self, remainingTestTime):
        if self.failed:
            result = 4 # failed
        elif self.running:
            if remainingTestTime >= 1:
                result = 1 # running
            else:
                result = 3 # passed
        else:
            if self.getCurrentDuration() > 0:
                if remainingTestTime < 1:
                    result = 3 # passed
                else:
                    result = 2 # paused
            else:
                result = 0 # ready
        self.testStatus_int = result
        return result


    def display_remainingTime(self, drt_now=time.time()):
        remainingTime = self.getRemainingTestTime(grtt_now=drt_now)
        if remainingTime < 1:
            remainingTime = 0
        self.update_test_status(remainingTime)
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

    def setTargetTime(self, secs):
        self.tgtTime = secs
        self.remainingTestTime = self.tgtTime - self.currentDuration

    def getTargetTime(self):
        return self.tgtTime

    def getStatus_int(self):
        status = self.testStatus_int
        return status

    def getStatusText(self):
        status = self.getStatus_int()
        txt = self.statusText[status]
        return txt

    def getName(self):
        return str(self.name)
