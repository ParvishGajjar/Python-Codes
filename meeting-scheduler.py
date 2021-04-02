# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 23:40:21 2021

@author: Parvish
"""

"""Coding challenge to take 2 peoples schedules and find a time for an interview"""

l1=[]
l2=[]
midl=[]
output=[]
m=0
w=None
x=None
y=None
z=None

# Converts time from "18:30" to seconds and returns it
def time_conversion(t1,t2):
    th1, tm1=t1.split(':')
    th2,tm2 = t2.split(':')
    time1=int(th1)*60+int(tm1)
    time2=int(th2)*60+int(tm2)
    return time1, time2

# Takes two times and compares them
def time_comparison(time1,time2):
    t1, t2 = time_conversion(time1,time2)
    if t1<t2:
        return 1
    elif t1>t2:
        return -1
    else:
        return 0

# Sorts times from l1 and l2    
def list_sorting(l1,l2,st1,st2):
    if st1==len(l1) and st2==len(l2):
        return midl
    if ((time_comparison(l1[st1][0],l2[st2][0]) == 1) and (time_comparison(l1[st1][1],l2[st2][0])==-1)):
        midl.append([str(l1[st1][0]),str(l1[st1][1])])
        midl.append([str(l2[st2][0]),str(l2[st2][1])])
    else:
        midl.append([str(l2[st2][0]),str(l2[st2][1])])
        midl.append([str(l1[st1][0]),str(l1[st1][1])])
    if st1<len(l1):
        st1+=1
    if st2<len(l2):
        st2+=1
    return list_sorting(l1,l2,st1,st2) 
        
def finalize_output(output,minutes):
    for i in range(len(output)):
        t1,t2 = time_conversion(output[i][0],output[i][1])
        if t2-t1<minutes:
            output.pop(i)
    return output
        
# Time Scheduler function finds free time common for both candidates    
def time_scheduler(c1,c2,b1,b2):
    if time_comparison(b2[0],c2[0][0]):
        l2.append([str(b2[0]),str(c2[0][0])])
    for i in range(len(c2)):
        if i==len(c2)-1:
            if time_comparison(c2[i][1],b2[1]):
                l1.append([str(c2[i][1]),str(b2[1])])
        elif time_comparison(c2[i][1],c2[i+1][0]):
            l1.append([str(c2[i][1]),str(c2[i+1][0])])
            
    #l1 = [[11:30,12:30],[15:16:00],[17:00,18:30]]

    if time_comparison(b1[0],c1[0][0]):
        l2.append([str(b1[0]),str(c1[0][0])])
    for i in range(len(c1)):
        if i==len(c1)-1:
            if time_comparison(c1[i][1],b1[1]):
                l2.append([str(c1[i][1]),str(b1[1])])
        elif time_comparison(c1[i][1],c1[i+1][0]):
            l2.append([str(c1[i][1]),str(c1[i+1][0])])
    
    #l2=[['10:30', '12:00'], ['13:00', '16:00'], ['18:00', '20:00']]        
    
    midl=list_sorting(l1,l2,0,0)
    
    #midl=[['10:30', '12:00'], ['11:30', '12:30'], ['13:00', '16:00'], ['15:00', '16:00'], ['17:00', '18:30'], ['18:00', '20:00']]
        
    for i in range(len(midl)-1):
        w = time_comparison(midl[i][0],midl[i+1][0])
        x = time_comparison(midl[i+1][0],midl[i][1])
        y = time_comparison(midl[i][1],midl[i+1][1])
        if w==1 and x==1 and y==1:
            output.append([str(midl[i+1][0]),str(midl[i][1])])
        elif w==1 and x==1 and y==-1:
            output.append([str(midl[i+1][0]),str(midl[i+1][1])])
        elif w==-1 and x==1 and y==-1:
            output.append([str(midl[i][0]),str(midl[i+1][1])])
        elif w==1 and x==1 and y==0:
            output.append([str(midl[i+1][0]),str(midl[i+1][1])])
    
    return output

# Main Function    
def main():
    
    # Static Input
    
    # Candidate 1's Schedule and Bounds for that day
    calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
    bound1 = ["9:00", "20:00"]
    
    # Candidate 2's Schedule and Bounds for that day
    calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
    bound2 = ["10:00", "18:30"]
    
    # Meeting duration in minutes
    time_of_meeting=30
    
    # Calling Time Scheduler Function
    output=time_scheduler(calendar1,calendar2,bound1,bound2)
    
    # Fetching common free time duration which is more or equal to required time for meeting 
    final_output=finalize_output(output,time_of_meeting)
    
    # Print Output
    print(final_output)

# Start Code, Calling Main Function    
main()

#Output

# [["11:30","12:00"],["15:00","16:00"],["18:00","18:30"]]