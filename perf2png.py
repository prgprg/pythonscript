import os
import argparse
import matplotlib.pyplot as plt
import csv
from datetime import datetime
import matplotlib.dates as mdates

#-------linuximport:
import subprocess


#%%-------------Functions-----------------
def cleardata(datalist):
    
      #%%------------------filtering the labels and removing unnececery texts------------------------------
    try: 
        timeIntervals=[]
        labels=[]
        txtlog=[]
        for i in range(0,len(datalist)):
            
            slashindex=[pos for pos, char in enumerate(datalist[i][0]) if char == '\\']
            if len(slashindex)>2:
                txtlog.append(datalist[i][0])
                datalist[i][0] = datalist[i][0][slashindex[2]+1:]
         
        
        for i in range(0,len(datalist)):
            
            #if ':' in datalist[i][0] or '?' in datalist[i][0] or '\"' in datalist[i][0] or '|' in datalist[i][0] or '*' in datalist[i][0] or ':' in datalist[i][0] or ':' in datalist[i][0] or ':' in datalist[i][0]:
            
            #-----------------removing undefined chars--------------------------
            
            
            datalist[i][0]= datalist[i][0].replace(':','')
            datalist[i][0]= datalist[i][0].replace('?','')
            datalist[i][0]= datalist[i][0].replace('*','')
            datalist[i][0]= datalist[i][0].replace('/',' per ')
            datalist[i][0]= datalist[i][0].replace('\"','')
            datalist[i][0]= datalist[i][0].replace('>','')
            datalist[i][0]= datalist[i][0].replace('<','')
            datalist[i][0]= datalist[i][0].replace(':','')
             
            #------------------------------------------------------------------    
            labels.append(datalist[i][0].replace('\\','_'))
            datalist[i].pop(0)
            
        timeIntervals=datalist[0]
        datalist.pop(0)
        labels.pop(0)
        
        
        print('\n \n -------------Configuring the Dataset: -------------  \n')
        printProgressBar(0, len(datalist), prefix = 'Progress:', suffix = 'Complete', length = 50)
       
        for i in range(len(datalist)):
            
         
            for j in range(len(datalist[i])):
            
                if datalist[i][j].strip() == "": #or j.strip() == '0':
                    #datalist[datalist.index(i)][datalist[datalist.index(i)].index(j)+1]=float(datalist[datalist.index(i)][datalist[datalist.index(i)].index(j)+1])
                    datalist[i][j]=float("nan")
                    #datalist[datalist.index(i)].pop(i.index(j))
                    #i.pop(i.index(j))
                else:
                    #print(len(datalist),len(i))
                    datalist[i][j]=float(datalist[i][j])
          
        # update progress bar
            printProgressBar(i+1, len(datalist), prefix = 'Progress:', suffix = 'Complete', length = 50)
         
        for i in timeIntervals:
                timeIntervals[timeIntervals.index(i)]=datetime.strptime(i,"%m/%d/%Y %H:%M:%S.%f")
    except Exception as e: print(e,'14')         

    return datalist , timeIntervals, labels, txtlog
    
def getdataset(date):
    
    
    
    try:
        
        
        tempdata=[];
        #inputstr=[]
        checkpoint=0
        avglist=[]
        # timeintervals=[]
        # ampm=[]
    
    #==========================================   1   ==================================================    
        R=subprocess.run(['sar', '-u', '-f','/var/log/sa/sa' + date ], stdout=subprocess.PIPE)  #read from terminal line
        inputstr=[]
        
        
        for i in R.stdout.splitlines():
            inputstr.append(list(filter(None,str(i).split(' '))))   
                
        inputstr.pop(0)    
        inputstr.pop(0)     
        avglist.append(inputstr.pop(-1))
    
    
        for i in range(len(inputstr[0])): 
            tempdata.append([])        
            
        for i in inputstr:
            for j in range(len(i)):
                
                if len(tempdata[checkpoint+j])==0 and checkpoint+j>1:
                    tempdata[checkpoint+j].append('Processor: ' + i[j])
                else:
                    tempdata[checkpoint+j].append(i[j])
        
         
        tempdata.pop(2)       
        checkpoint=len(tempdata)
        
    except Exception as e: print(e, '1')

    try:
    #============================================   2   ===================================================    
        R=subprocess.run(['sar', '-b', '-f','/var/log/sa/sa' + date ], stdout=subprocess.PIPE)
        inputstr=[]
        
        for i in R.stdout.splitlines():
            inputstr.append(list(filter(None,str(i).split(' '))))
                
        inputstr.pop(0)    
        inputstr.pop(0)     
        avglist.append(inputstr.pop(-1))
        
    
    
        for i in range(len(inputstr[0])): 
            tempdata.append([])        
            
        for i in inputstr:
            for j in range(len(i)):
                
                if len(tempdata[checkpoint+j])==0 and checkpoint+j>1:
                    tempdata[checkpoint+j].append('Physical Disk: ' + i[j])
                else:
                    tempdata[checkpoint+j].append(i[j])
        
        
        #-------------to prevent from savin time intervals twice--------------
        tempdata.pop(checkpoint)
        tempdata.pop(checkpoint)  
        #---------------------------------------------------------------------
    
          
        checkpoint=len(tempdata)
        
    except Exception as e: print(e, '2')
    try:
    #==========================================   3   =====================================================    
        R=subprocess.run(['sar', '-B', '-f','/var/log/sa/sa' + date ], stdout=subprocess.PIPE)
        inputstr=[]
        
        
        for i in R.stdout.splitlines():
            inputstr.append(list(filter(None,str(i).split(' '))))
                
        inputstr.pop(0)    #unneccesary data
        inputstr.pop(0)     
        avglist.append(inputstr.pop(-1))
    
    
        for i in range(len(inputstr[0])): 
            tempdata.append([])        
            
        for i in inputstr:
            for j in range(len(i)):
                
                if len(tempdata[checkpoint+j])==0 and checkpoint+j>1:
                    tempdata[checkpoint+j].append('Memory: ' + i[j])
                else:
                    tempdata[checkpoint+j].append(i[j])
        
        #-------------to prevent from savin time intervals twice--------------
        tempdata.pop(checkpoint)
        tempdata.pop(checkpoint)  
        #---------------------------------------------------------------------
    
           
        checkpoint=len(tempdata)
        
    except Exception as e: print(e, '3')
    try:    
    #============================================   4   ===================================================    
        R=subprocess.run(['sar', '-q', '-f','/var/log/sa/sa' + date ], stdout=subprocess.PIPE)
        inputstr=[]
        
        
        for i in R.stdout.splitlines():
            inputstr.append(list(filter(None,str(i).split(' '))))
                
        inputstr.pop(0)    
        inputstr.pop(0)     
        avglist.append(inputstr.pop(-1))
    
    
        for i in range(len(inputstr[0])): 
            tempdata.append([])        
            
        for i in inputstr:
            for j in range(len(i)):
                
                if len(tempdata[checkpoint+j])==0 and checkpoint+j>1:
                    tempdata[checkpoint+j].append('Processor: ' + i[j])
                else:
                    tempdata[checkpoint+j].append(i[j])
                    
                    
        #-------------to prevent from savin time intervals twice--------------
        tempdata.pop(checkpoint)
        tempdata.pop(checkpoint)  
        #---------------------------------------------------------------------    
                
        
        checkpoint=len(tempdata)
        
    
    except Exception as e: print(e, '4')
    try:        
    #============================================   5   ===================================================    
        R=subprocess.run(['sar', '-r', '-f','/var/log/sa/sa' + date ], stdout=subprocess.PIPE)
        inputstr=[]
        
        
        for i in R.stdout.splitlines():
            inputstr.append(list(filter(None,str(i).split(' '))))
                
        inputstr.pop(0)    
        inputstr.pop(0)     
        avglist.append(inputstr.pop(-1))
    
    
        for i in range(len(inputstr[0])): 
            tempdata.append([])        
            
        for i in inputstr:
            for j in range(len(i)):
                
                if len(tempdata[checkpoint+j])==0 and checkpoint+j>1:
                    tempdata[checkpoint+j].append('Memory: ' + i[j])
                else:
                    tempdata[checkpoint+j].append(i[j])
        
        
        #-------------to prevent from savin time intervals twice--------------
        tempdata.pop(checkpoint)
        tempdata.pop(checkpoint)  
        #---------------------------------------------------------------------
                
        
        checkpoint=len(tempdata)
   
        
   
    except Exception as e: print(e, '5')
    try:
    #============================================   6   ===================================================    
        R=subprocess.run(['sar', '-w', '-f','/var/log/sa/sa' + date ], stdout=subprocess.PIPE)
        inputstr=[]
        
        
        for i in R.stdout.splitlines():
            inputstr.append(list(filter(None,str(i).split(' '))))
                
        inputstr.pop(0)    
        inputstr.pop(0)     
        avglist.append(inputstr.pop(-1))
    
    
        for i in range(len(inputstr[0])): 
            tempdata.append([])        
            
        for i in inputstr:
            for j in range(len(i)):
                
                if len(tempdata[checkpoint+j])==0 and checkpoint+j>1:
                    tempdata[checkpoint+j].append('System: ' + i[j])
                else:
                    tempdata[checkpoint+j].append(i[j])
        
        
        #-------------to prevent from savin time intervals twice--------------
        tempdata.pop(checkpoint)
        tempdata.pop(checkpoint)  
        #---------------------------------------------------------------------
                
       
        checkpoint=len(tempdata)
      
   
    except Exception as e: print(e,'6')
    try: 
 #==========================================  -n DEV ==================================================    
        R=subprocess.run(['sar', '-n', 'DEV', '-f','/var/log/sa/sa' + date ], stdout=subprocess.PIPE)
        inputstr=[]
        devnames=[]
        #print(R.stdout)
        # l=R.stdout.splitlines()
        
        
        
        for i in R.stdout.splitlines():
            inputstr.append(list(filter(None,str(i).split(' '))))
                
        inputstr.pop(0)    
        inputstr.pop(0)     
        #avglist.append(inputstr.pop(-1))
        
        for i in inputstr:
            #print(i[2])
            if i[2]!='IFACE' and (i[2] in devnames) == False and i[0]!='b\'Average:':
                devnames.append(i[2])
                inputstr.pop(-1)


    
        for i in range(len(inputstr[0])*len(devnames)): 
            tempdata.append([])        
          
        
        for e in devnames:   #seperating different devices
            
            for i in inputstr:
                
                if (e in i)==True or ('IFACE' in i)==True:
                    
                    for j in range(len(i)):
                        
                        if len(tempdata[checkpoint+j])==0 and checkpoint+j>1:
                            tempdata[checkpoint+j].append('Network (' + e +'): ' + i[j])
                        else:
                            tempdata[checkpoint+j].append(i[j])

            checkpoint+=len(inputstr[0])
            
            #-------------to prevent from savin time intervals twice--------------
            tempdata.pop(checkpoint-len(inputstr[0]))
            tempdata.pop(checkpoint-len(inputstr[0])) 
            tempdata.pop(checkpoint-len(inputstr[0]))         
            checkpoint-=3
         
        #tempdata.pop(2)       
        checkpoint=len(tempdata)

    except Exception as e: print(e,'7')
    try:        
    
 #==========================================  -d -p ==================================================    
        R=subprocess.run(['sar', '-d', '-p', '-f','/var/log/sa/sa' + date ], stdout=subprocess.PIPE)
        inputstr=[]
        devnames=[]
        #print(R.stdout)
        # l=R.stdout.splitlines()
        
        
        
        for i in R.stdout.splitlines():
            inputstr.append(list(filter(None,str(i).split(' '))))
                
        inputstr.pop(0)    
        inputstr.pop(0)     
        #avglist.append(inputstr.pop(-1))
        
        for i in inputstr:
            #print(i[2])
            if i[2]!='DEV' and (i[2] in devnames) == False and i[0]!='b\'Average:':
                devnames.append(i[2])
                inputstr.pop(-1)


    
        for i in range(len(inputstr[0])*len(devnames)): 
            tempdata.append([])        
          
        
        for e in devnames:
            
            for i in inputstr:
                
                if (e in i)==True or ('DEV' in i)==True:
                    
                    for j in range(len(i)):
                        
                        if len(tempdata[checkpoint+j])==0 and checkpoint+j>1:
                            tempdata[checkpoint+j].append('Device ('+ e+ '): ' + i[j])
                        else:
                            tempdata[checkpoint+j].append(i[j])

            checkpoint+=len(inputstr[0])
            
            #-------------to prevent from savin time intervals twice--------------
            tempdata.pop(checkpoint-len(inputstr[0]))
            tempdata.pop(checkpoint-len(inputstr[0])) 
            tempdata.pop(checkpoint-len(inputstr[0]))         
            checkpoint-=3
         
        #tempdata.pop(2)       
        checkpoint=len(tempdata)
                 
      
    except Exception as e: print(e,'8')
    #intervals=[]
    
    
    try:  
        
        #---------------------------changing time format----------------------------------
        intervals=[]
        for i in range(len(tempdata[1])):
            tempdata[0][i]=tempdata[0][i][2:]+ ' ' + tempdata[1][i]
            intervals.append(datetime.strptime(tempdata[0][i],'%I:%M:%S %p'))
        
        
        tempdata.pop(0);
        tempdata.pop(0);
        
        #----------------------------seperating labels------------------------------------
        labels=[]
        for i in range(len(tempdata)):
            labels.append(tempdata[i].pop(0))
        
        intervals.pop(0)
        
        for i in range(len(tempdata)):
            for j in range(len(tempdata[i])):
                
                tempdata[i][j]=float(tempdata[i][j].replace('\'', ''))
        
        
        
      

    
    
        
        
    except Exception as e: print(e, '9')
    
    
    return tempdata , intervals, labels

def plott():
    
    try:  #plotting
        
        # Initial call to print 0% progress
        printProgressBar(0, len(datalist), prefix = 'Progress:', suffix = 'Complete', length = 50)
        os.makedirs(r'./'+sardate+'/')
    
        plt.figure(dpi=200,frameon=True);
        for i in range(0,len(datalist)):
             
            plt.rcParams.update({'font.size': 7});
            plt.title(labels[i], fontsize=11)
            
            labels[i]=labels[i].replace(':', ')');
            labels[i]=labels[i].replace('\'', '');
                    
            myFmt = mdates.DateFormatter('%H:%M')
            plt.gca().xaxis.setmajor_formatter(myFmt);
            
            plt.xlabel('Time HH:MM', fontsize=8);
            plt.grid(True);
             
            plt.plot(timeIntervals,datalist[i], 'bo',markersize=1.5)  ; 
            plt.savefig(r'./'+sardate+'/('+labels[i].replace('/',' in ')+r'.png') ;
            plt.clf();
            labels[i]=labels[i].replace(')', ':')
            
            if len(plt._pylab_helpers.Gcf.get_all_fig_managers())>99:
                plt.close(fig='all');
                                
            # Update Progress Bar
            printProgressBar(datalist.index(i) + 1, len(datalist), prefix = 'Progress:', suffix = 'Complete', length = 50)
            
    except Exception as e: print(e, '10')

def getfiledate(date):
    
    R=subprocess.run(['sar', '-u', '-f','/var/log/sa/sa'+ date ], stdout=subprocess.PIPE)  #read from terminal line
    inputstrr=[]
    
    
    for i in R.stdout.splitlines():
        inputstrr.append(list(filter(None,str(i).split(' '))))   
            
    sardate=inputstrr.pop(0)[3][2:].replace('/','-') 
    d= datetime.strptime(sardate, '%m-%d-%Y')    
    sardate=str(d.strftime('%Y-%m-%d'))
    
    return sardate

def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def winget():
    try:
        
        datalist=[]
        with open("out.csv", 'r') as csvfile:
            templist = []
            d = []
            plots= csv.reader(csvfile, delimiter=',')
         
            for row in plots:
                templist.append(row)
           
            for i in range(0,len(templist[0])):
                for j in range(0,len(templist)):
                    d.append(templist[j][i])
                datalist.append(d)
                d=[]
            
    except Exception as e: print(e,'13')        
            
    return datalist       

def createdir(timeIntervals):
    try: 
        directory=''
        #%%----------creating directory-----------------
        if timeIntervals[0].strftime('%d.%m.%Y')==timeIntervals[-1].strftime('%d.%m.%Y'):
    
    
            directory=timeIntervals[0].strftime('%Y-%m-%d')  
            #directory="\""+directory+"\""
           # print(directory)
            #directory=timeIntervals[0].strftime('%Y-%m-%d')+' '+timeIntervals[-1].strftime('%Y-%m-%d')
            os.mkdir(directory)
        else:
            directory=timeIntervals[0].strftime('%Y-%m-%d')+' '+timeIntervals[-1].strftime('%Y-%m-%d')
    #        directory=timeIntervals[0].strftime('%Y-%m-%d')        
            os.mkdir(directory)
            

    except Exception as e: print(e,'15')  
    
    return directory
    
def winplot(datalist , timeIntervals , labels , directory):

    try:

    #%%+++++++++++++++++++PLOTTING+++++++++++++++++++++++++  
        #multi()  
        #plott()
        
        # Initial call to print 0% progress
        
        print('\n \n -------------Creating Files: -------------  \n')
        printProgressBar(0, len(datalist), prefix = 'Progress:', suffix = 'Complete', length = 50)
        plt.figure(dpi=200,frameon=True)
        for i in range(len(datalist)):
            
            plt.plot(timeIntervals,datalist[i], 'bo',markersize=1.5) 
            plt.rcParams.update({'font.size': 7})
            plt.title(labels[i], fontsize=11)
            
                    
            myFmt = mdates.DateFormatter('%H:%M')
            plt.gca().xaxis.set_major_formatter(myFmt)
            
            plt.xlabel('Time HH:MM', fontsize=8)
            plt.grid(True)
               
            plt.savefig(directory+r'/'+labels[i].replace('/',' in ')+r'.png') 
            plt.clf()
            
            
            if len(plt._pylab_helpers.Gcf.get_all_fig_managers())>99:
                plt.close(fig='all')
                
            # Update Progress Bar
            printProgressBar(i + 1, len(datalist), prefix = 'Progress:', suffix = 'Complete', length = 50)
                
                
    except Exception as e: print(e,'16')  
    
def saveextrafiles(directory, txtlog):
    try:                
            
        #%%----------saving the csv file if wanted--------------------
    
        if len(args) != 0:
            
            if 'savecsv' in args and args['savecsv']!=None and args['savecsv'][-4:]=='.csv':
                os.system('copy out.csv \"%cd%\\'+directory+'\"')
                os.system('ren \"%cd%\\'+directory+'\\out.csv\" '+ str(args['savecsv']))
                os.system('del out.csv')
            elif args['savecsv']!=None and args['savecsv'][-4:]!='.csv':
                print('wrong input! \nplease enter full .csv filename with extension.')
            elif args['savecsv']==None:
                os.system('del out.csv')
            
        #%%----------saving the log.txt file if wanted--------------------
        
        if len(args) != 0:
            
            if 'log' in args and args['log']!=None and args['log'][-4:]=='.txt':
                
                with open(directory+'\\'+args['log'], "w") as output:
                    for i in txtlog:
                        output.write(str(i)+'\n')
                    
            elif args['log']!=None and args['log'][-4:]!='.txt':
                print('wrong input! \nplease enter full .txt filename with extension.')
            
        
        
    except Exception as e: print(e,'17')  
    
    
    
    
    
#%%+++++++++++++++++++++++OPTIONs AND ARGUMENTS++++++++++++++++++++++
# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser

#relog
ap.add_argument("-r", "--relog", required=False,
   help="[file name] convert .blg file to .csv")


ap.add_argument("-l", "--log", required=False,
   help="[file name] creates a log file with specific name if given")



ap.add_argument("-s", "--savecsv", required=False,
   help="[.csv output filename] keeps the .csv file")


#linux
ap.add_argument("-u", "--linuxlog", required=False,
    help="[DD] (day of month) generates the png file from sar file for the specified date.\nAlso creates a log.txt file with names of plotted arguments")
args = vars(ap.parse_args())

#%%+++++++++++++++++++VARIABLES++++++++++++++++++


#DATA

winflag = True


#SYSTEM FILE



#%%+++++++++++++++++++++++++ relog COMMANDS++++++++++++++++++++++++++++++
try:
        
    #print(args['relog']) 
    #
    if len(args) != 0:
        
        if 'relog' in args and args['relog']!=None and args['relog'][-4:]=='.blg':
            
            print('\n \n -------------Converting Data:-------------')
            
            os.system("relog " + str(args['relog']) + " -o \"%cd%\out.csv\" -f csv")
            
            winflag = True;
            
        elif args['relog'][-4:]!='.blg':
            print('wrong input! \nplease enter full .blg filename.')
            
            
except Exception as e: print(e, '11')



#%%-----------------------linux:----------------------------------------------

inputdate=''

try:
       
    #print(str(type(args['linuxlog'])))
    if len(args) != 0:
        
        if 'linuxlog' in args and str(type(args['linuxlog']))!="<class \'NoneType\'>" and args['linuxlog']!=None:
            if len(args['linuxlog'])==2:
                inputdate=args['linuxlog'] #find the days and split the string
                sardate=getfiledate(inputdate)
                datalist, timeIntervals, labels = getdataset(inputdate)
                plott()
                
    
                with open('./'+sardate+'/log.txt', "w") as output:
                    for i in labels:
                        output.write(str(i).replace('(','')+'\n')
                winflag = False        
                        
                    
        elif args['linuxlog']!=None:
            if len(args['linuxlog'])!=2:
                print('wrong input! \nplease enter the day numer with two digits (e.g. 09)')
                exit()
            
except Exception as e: print(e,'12')

#%%++++++++++++++++++Windows+++++++++++++++++

if winflag==True:

    datalist = winget()
    
    datalist , timeIntervals , labels, txtlog = cleardata(datalist)
    
    directory = createdir(timeIntervals)
    
    winplot(datalist,timeIntervals,labels,directory)
    
    saveextrafiles(directory, txtlog)
    
else:
    print("Nothing to do here!")
    exit()
    
    
    
    
    