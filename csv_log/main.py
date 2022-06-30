import  get_processing_time

def main():
    processTimeMeasure = get_processing_time.process_time_measure(name="example")
    processTimeMeasure.time_start()
    for i in range(100):
        print("")
    processTimeMeasure.time_end()

main()