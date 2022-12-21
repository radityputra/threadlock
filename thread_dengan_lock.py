import threading
import urllib.request, urllib.parse, urllib.error

class FetchUrls(threading.Thread):
    #Thread checking URLs.
    def __init__(self, urls, output, lock):
        """
        Contructor.
        @param urls list of urls to check
        @param output file to write urls ourtput
        """ 
        threading.Thread.__init__(self)
        self.urls = urls
        self.output = output
        # add code here
        self.lock = lock

    def run(self):
        #Thread run method. Check URLs one by one.
        while self.urls:
            url = self.urls.pop()

            try:
                d = urllib.request.urlopen(url)
            except Exception as e:
                print ("URL %s failed" %url)

            self.lock.acquire()
            print ('lock acquire by %s' % self.name)

            self.output.acquire(d.read().decode())
            print ('write done by %s' % self.name)

            print ('lock released by %s' % self.name)
            self.lock.release()

            print('URL %s fetched by %s' % (url, self.name))

    def main():
        lock = threading.Lock()
    
        #list 1 of urls to fecth
        urls1 = ['http://www/google.com', 'http://www.facebook.com']
        #list 2 of urls to fecth
        urls2 = ['http://www.yahoo.com', 'http://www.youtube.com']
        f = open('output_not_correct.txt', 'w+', encoding='utf-8')
        t1 = FetchUrls(urls1, f, lock)
        t2 = FetchUrls(urls2, f, lock)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        f.close()

    if __name__ == '__main__':
        main()
    
        
