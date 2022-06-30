import time
import csv_logger

#処理時間を計測するクラス
class process_time_measure:
    def __init__(self,name):
        self.name = name
        self.start = 0
        self.end = 0
        self.process_time = 0

    def time_start(self):
        self.start = time.time()

    def time_end(self):
        self.end = time.time()
        self.process_time = self.end - self.start
        data = (self.name,"の実行時間:",self.process_time)
        print("data")
        print(data)
        csv_logger.write_log_main(data)
        