import csv
import sys
from datetime import date, timedelta
from google.cloud import bigquery as bq

class Fetcher:
    '''Provides batches of images'''
    #TODO TODO - you probably want to modify this to implement data augmentation
    def __init__(self,stockfile):
        self.startyear = 1974
        self.nextyear = 1975
        self.current = date(self.startyear,12,10)
        self.curend = date(self.nextyear,12,10)
        self.cache = {}
        self.stocks = None
        self.qclient = bq.Client()
        #Load stock data, it's small enough to keep it all in memory
        with open(stockfile) as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(1024))
            csvfile.seek(0)
            reader = csv.reader(csvfile, dialect)
            first = True
            for row in reader:
                if first:
                    first = False
                    continue
                tdate = row[0]
                tdate = int(date.replace("-",""))
                diff = float(row[4]) - float(row[1])
                self.stocks[tdate] = diff
        print("Loaded " + stockfile + ".")


    def load_next(self):
        #Load current event data 1 year at a time
        print("I want to get stocks[" + str(self.current) + "]")
        start_date = date(1974, 12, 10)
        for n in range(364):
            delt = start_date + timedelta(n)
            rep = str(delt).replace("-","")

        #Implement a cache for mysql
        events = []
        stockchange = 0
        sys.exit(0);
        x_batch = []
        y_batch = []
        for i in xrange(batchsize):
            label, files = self.examples[(self.current+i) % len(self.examples)]
            label = label.flatten()
            # If you are getting an error reading the image, you probably have
            # the legacy PIL library installed instead of Pillow
            # You need Pillow
            channels = [ misc.imread(file_io.FileIO(f,'r')) for f in files]
            x_batch.append(np.dstack(channels))
            y_batch.append(label)

        self.current = (self.current + batchsize) % len(self.examples)
        return np.array(x_batch), np.array(y_batch)

f = Fetcher("DOW.csv")
f.load_next()
