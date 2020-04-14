
import os
import argparse
import time
import matplotlib.pyplot as plt
import csv
#import copy
from datetime import datetime
import multiprocessing
import atexit

import matplotlib.dates as mdates

ss=time.time()


#%%+++++++++++++++++++VARIABLES++++++++++++++++++


#DATA

counter_1 = 0


datalist = []
labels = []
txtlog=[]
timeIntervals=[]

#SYSTEM FILE
directory=''
file_name=''

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
args = vars(ap.parse_args())



#%%+++++++++++++++++++++++++ relog COMMANDS++++++++++++++++++++++++++++++
try:
        
    #print(args['relog']) 
    #
    if len(args) != 0:
        
        if 'relog' in args and args['relog']!=None and args['relog'][-4:]=='.blg':
            os.system("relog " + str(args['relog']) + " -o \"%cd%\out.csv\" -f csv")
            
        elif args['relog'][-4:]!='.blg':
            print('wrong input! \nplease enter full .blg filename.')
            
            
except Exception as e: print(e)


#%%++++++++++++++++++LOADING DATA+++++++++++++++++

try:
    
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
        
except Exception as e: print(e)        
        
        
#%%++++++++++++++++++CONFIGURING THE DATASET AND ELEMENTS++++++++++++        
        
try:
    #%%------------------filtering the labels and removing unnececery texts------------------------------
    
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
        datalist[i][0]= datalist[i][0].replace('/','')
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
    
    #%%--------------------------clearing data----------------------------------
    
    #templist=copy.deepcopy(datalist)
    for i in datalist:
        for j in i:
            
            if j.strip() == '': #or j.strip() == '0':
                #datalist[datalist.index(i)][datalist[datalist.index(i)].index(j)+1]=float(datalist[datalist.index(i)][datalist[datalist.index(i)].index(j)+1])
                datalist[datalist.index(i)][datalist[datalist.index(i)].index(j)]=float("nan")
                #datalist[datalist.index(i)].pop(i.index(j))
                #i.pop(i.index(j))
            else:
                datalist[datalist.index(i)][datalist[datalist.index(i)].index(j)]=float(j)
    
    
    
    #%%-----------------------converting time interavls-------------------------------
    
    for i in timeIntervals:
        timeIntervals[timeIntervals.index(i)]=datetime.strptime(i,"%m/%d/%Y %H:%M:%S.%f")

         
except Exception as e: print(e)      
 
 

  
 
try: 
    
    #%%----------creating directory-----------------
    if timeIntervals[0].strftime('%d.%m.%Y')==timeIntervals[-1].strftime('%d.%m.%Y'):


        directory=timeIntervals[0].strftime('%Y-%m-%d')        
        #directory=timeIntervals[0].strftime('%Y-%m-%d')+' '+timeIntervals[-1].strftime('%Y-%m-%d')
        os.system('mkdir '+directory)
    else:
        directory=timeIntervals[0].strftime('%Y-%m-%d')+' '+timeIntervals[-1].strftime('%Y-%m-%d')
#        directory=timeIntervals[0].strftime('%Y-%m-%d')        
        os.system('mkdir '+directory)
        
#%%+++++++++++++++++++PLOTTING+++++++++++++++++++++++++  
    #multi()    
    plt.figure(dpi=200,frameon=True)
    for i in range(0,len(datalist)):
         
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
        
    #%%----------saving the csv file if wanted--------------------
    
    if len(args) != 0:
        
        if 'savecsv' in args and args['savecsv']!=None and args['savecsv'][-4:]=='.csv':
            os.system('copy out.csv \"%cd%\\'+directory+'\"')
            os.system('ren \"%cd%\\'+directory+'\\out.csv\" '+ str(args['savecsv']))
            os.system('del out.csv')
        elif args['savecsv'][-4:]!='.csv':
            print('wrong input! \nplease enter full .csv filename with extension.')
        
    #%%----------saving the log.txt file if wanted--------------------
    
    if len(args) != 0:
        
        if 'log' in args and args['log']!=None and args['log'][-4:]=='.txt':
            
            with open(directory+'\\'+args['log'], "w") as output:
                for i in txtlog:
                    output.write(str(i)+'\n')
                
        elif args['log'][-4:]!='.txt':
            print('wrong input! \nplease enter full .txt filename with extension.')
        
    
    
except Exception as e: print(e)  


# def endlog():
#     print(time.time()-ss)

# atexit.register(endlog)



