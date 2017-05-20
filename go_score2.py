from __future__ import division
import sys
import math

def go_score1(filename1):

    file1 = open(filename1) #native
    x1=[]
    y1=[]
    z1=[]
    for line in file1:
        if 'ATOM' in line and 'CA' in line:
            splitted_line = [line[:6], line[6:11], line[12:16], line[17:20], line[21], line[22:26], line[30:38], line[38:46], line[46:54]]
            a = "%-6s %5s %4s %3s %s %4s    %8s %8s %8s\n"%tuple(splitted_line)
            a = a.split()
            x1.append(float(a[-3]))
            y1.append(float(a[-2]))
            z1.append(float(a[-1]))
    distance_native = []
    for i in range(len(x1)-1):
        for j in range(i+1,len(x1)):
            val = math.sqrt((x1[i]-x1[j])**2+(y1[i]-y1[j])**2+(z1[i]-z1[j])**2)
            distance_native.append(val)
            
    file1.close()

    return distance_native

def go_score2(filename2):

    file2 = open(filename2) #models
    x2=[]
    y2=[]
    z2=[]
    for line in file2:
        if 'ATOM' in line and 'CA' in line:
            splitted_line = [line[:6], line[6:11], line[12:16], line[17:20], line[21], line[22:26], line[30:38], line[38:46], line[46:54]]
            a = "%-6s %5s %4s %3s %s %4s    %8s %8s %8s\n"%tuple(splitted_line)
            a = a.split()
            x2.append(float(a[-3]))
            y2.append(float(a[-2]))
            z2.append(float(a[-1]))
    distance_model = []
    for i in range(len(x2)-1):
        for j in range(i+1,len(x2)):
            val = math.sqrt((x2[i]-x2[j])**2+(y2[i]-y2[j])**2+(z2[i]-z2[j])**2)
            distance_model.append(val)
            
    file2.close()

    return distance_model



if __name__ == "__main__":
    dist_nat = go_score1(sys.argv[1])

    for name in range(10):
        name = '%s.B%i.pdb'%(sys.argv[2],int(99990001)+int(name))

        dist_mod = go_score2(name)
    
        val = 0
        sigma = 1
        for i in range(len(dist_nat)):
            calc = math.exp((-(dist_nat[i]-dist_mod[i])**2)/2*sigma**2)
            val = val + calc
        result = val / len(dist_nat)

        print name,' ',result
        
        
