# -*- coding: utf-8 -*-
"""

@author: Ali Pourgholami Jirandehi
@Email: ali.pourgholami@inform-software.com

"""
import subprocess

from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

import argparse



        
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
        
    except Exception as e: print(e)

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
        
    except Exception as e: print(e)
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
        
    except Exception as e: print(e)
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
        
    
    except Exception as e: print(e)
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
   
        
   
    except Exception as e: print(e)
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
      
   
    except Exception as e: print(e)
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

    except Exception as e: print(e)
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
                 
      
    except Exception as e: print(e)
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
        
        
        
      

    
    
        
        
    except Exception as e: print(e)
    
    
    return tempdata , intervals, labels

def plott():
    
    try:  #plotting
        
        
        #os.makedirs(r'/Performance/'+inputdate)
    
        plt.figure(dpi=200,frameon=True);
        for i in range(0,len(datalist)):
             
            plt.rcParams.update({'font.size': 7});
            plt.title(labels[i], fontsize=11)
            
            labels[i]=labels[i].replace(':', ')');
            labels[i]=labels[i].replace('\'', '');
                    
            myFmt = mdates.DateFormatter('%H:%M')
            plt.gca().xaxis.set_major_formatter(myFmt);
            
            plt.xlabel('Time HH:MM', fontsize=8);
            plt.grid(True);
             
            plt.plot(timeIntervals,datalist[i], 'bo',markersize=1.5)  ; 
            plt.savefig(r'./('+labels[i].replace('/',' in ')+r'.png') ;
            plt.clf();
            labels[i]=labels[i].replace(')', ':')
            
            if len(plt._pylab_helpers.Gcf.get_all_fig_managers())>99:
                plt.close(fig='all');
            
    except Exception as e: print(e)




#%%+++++++++++++++++++++++OPTIONs AND ARGUMENTS++++++++++++++++++++++
inputdate=''
# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser

#linux
ap.add_argument("-u", "--linuxlog", required=False,
    help="[DD] (day of month) generates the png file from sar file for the specified date")
args = vars(ap.parse_args())



try:
        
    if len(args) != 0:
        
        if 'linuxlog' in args and args['linuxlog']!=None and len(args['linuxlog'])==2:
            inputdate=args['linuxlog'] #find the days and split the string
            
        elif len(args['linuxlog'])!=2:
            print('wrong input! \nplease enter the day numer with two digits (e.g. 09)')
            exit()
            
except Exception as e: print(e)


#%%









#%%

datalist, timeIntervals, labels = getdataset(inputdate)

plott()



#%%


with open('./list.txt', "w") as output:
    for i in labels:
        output.write(str(i).replace('(','')+'\n')
    
    
    
    
    
    
    
    
    
    