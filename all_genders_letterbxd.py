from letterboxdscrapping import MovieDataProcessorLetter
import threading
from queue import Queue
import time

class MovieDataProcessorLetterboxdAll:
    def allgenders(self,file):
        DataProcessor = MovieDataProcessorLetter()

        DataProcessor.readCSV(file)
        

        LetterboxdURI = DataProcessor.ReturnAllURILetterbox()

        max_threads = 10
        thread_semaphore = threading.Semaphore(max_threads)

        def process_uri(uri, result_queue):
            genders = DataProcessor.getgenders(DataProcessor.getdata(uri))
            result_queue.put(genders)
            thread_semaphore.release()


        result_queue = Queue()
        threads = []




        def process_uri_in_thread(uri):
            thread_semaphore.acquire()
            thread = threading.Thread(target=process_uri, args=(uri, result_queue))
            threads.append(thread)
            thread.start()

        for uri in LetterboxdURI:
            process_uri_in_thread(uri)


        for thread in threads:
            thread.join()

        genders = []
        while not result_queue.empty():
            genders.extend(result_queue.get())

        return genders



    def allruntimes(self,file):
        DataProcessor = MovieDataProcessorLetter()

        DataProcessor.readCSV(file)
        

        LetterboxdURI = DataProcessor.ReturnAllURILetterbox()

        max_threads = 10
        thread_semaphore = threading.Semaphore(max_threads)

        def process_uri(uri, result_queue):
            runtimes = DataProcessor.getruntime(DataProcessor.getdata(uri))
            result_queue.put(runtimes)
            thread_semaphore.release()


        result_queue = Queue()
        threads = []




        def process_uri_in_thread(uri):
            thread_semaphore.acquire()
            thread = threading.Thread(target=process_uri, args=(uri, result_queue))
            threads.append(thread)
            thread.start()

        for uri in LetterboxdURI:
            process_uri_in_thread(uri)


        for thread in threads:
            thread.join()

        runtimes = []
        while not result_queue.empty():
            runtimes.append(int(result_queue.get()))
       
        return runtimes
    
    