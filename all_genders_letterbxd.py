from letterboxdscrapping import MovieDataProcessorLetter
import threading
from queue import Queue
import time
"""
Most of this is outdated since i'm not getting the data from the letterbxd website anymore
I am now using my own API
"""
class MovieDataProcessorLetterboxdAll:
    def scanAPI(self, file):
        DataProcessor = MovieDataProcessorLetter()
        DataProcessor.readCSV(file)
        movies_names = DataProcessor.ReturnAllMovieLetterbox()
        Tout = []
        count = 0
        for movie in movies_names:
            movie = movie.replace("'","")
            data = DataProcessor.GetDataFromMyAPI(movie)
            data = data.replace("[","")
            data = data.replace("]","")
            data = data.split(",")
            Tout.append(data)
            count += 1
            if count == 20:
                break
        return Tout
    """
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

        runtimes_with_names = {}
        while not result_queue.empty():
            data = result_queue.get()
            runtimes_with_names.update({data[0][0]: int(data[0][1])})
       
        return runtimes_with_names
    
    """