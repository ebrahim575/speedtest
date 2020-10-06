import speedtest
import time
from datetime import datetime


    
def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]

def main():
    # write to csv
    with open('file2.xlsx', 'a') as f:
        f.write('Download,Upload,Ping\n')
        #for i in range(3):
        #print('Making test #{}'.format(i+1))
        print('Starting SpeedTest.')
        start_time = time.time()
        d, u, p = test()
        end_time = time.time()
        #main()
        print('Execution time : %.2fs' % (end_time - start_time))
        f.write('{},{},{}\n'.format(d/1024000, u/1024000, p))
        #print('Task #{} done.'.format(i+1))
        print('SpeedTest Done.\n')
        
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        
        print('Date and Time = ', dt_string)
        print('Download: {:.2f} Mb/s'.format(d / 1024000))
        print('Upload: {:.2f} Mb/s'.format(u / 1024000))
        print('Ping: {}'.format(p))
            
    with open('file.txt', 'a') as f:
        #for i in range(3):
        #print('Making test #{}'.format(i+1))
        #d, u, p = test()
        #f.write('Test #{}\n'.format(i+1))
         
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        
        f.write('Date and Time = ' + dt_string)
        f.write('\nDownload: {:.2f} Mb/s\n'.format(d / 1024000))
        f.write('Upload: {:.2f} Mb/s\n'.format(u / 1024000))
        f.write('Ping: {}\n\n'.format(p))
                
    #for i in range(3):
    #d, u, p = test()
    #print('Speedtest #{}'.format(i+1))
    #print('Download: {:.2f} Mb/s'.format(d / 1024000))
    #print('Upload: {:.2f} Mb/s'.format(u / 1024000))
    #print('Ping: {}\n\n'.format(p))
    #if i == 0:
        #alpha = d
    #elif i == 1:
        #beta = d
    #else:
        #charlie = d
    #avg = (((alpha/1024000) + (beta/1024000) + (charlie/1024000)) / 3)
    #print('Average : ',avg)


if __name__ == '__main__':
    main()

