#Function to remove negative current from BCM plates to neighboring positive plates

def negativePlates( x1, x2, x3, x4, err1, err2, err3, err4):
    for i  in range(len(x1)):
        if ((len(x1) != len(x2)) or (len(x1) != len(x3)) or (len(x1) != len(x4)) ):
            print("Column lengths don't match. Check import.")
            
        elif ((x1[i]>=0) and (x2[i]>=0) and (x3[i]>=0) and (x4[i]>=0)): # + + + +  
            continue
            
        elif (x1[i]>=0 and x2[i]<0 and x3[i]>=0 and x4[i]>=0): # + - + + 
            x1[i]=x1[i]+abs(x2[i]/2)
            x4[i]=x4[i]+abs(x2[i]/2)
            x2[i]=1E-20 
            
            err1[i]= err1[i]+err2[i]/2
            err4[i]= err4[i]+ err2[i]/2
            
        elif (x1[i]>=0 and x2[i]>=0 and x3[i]<0 and x4[i]>=0): # + + - + 
            x1[i]=x1[i]+abs(x3[i]/2)
            x4[i]=x4[i]+abs(x3[i]/2)
            x3[i]=1E-20    

            err1[i]= err1[i]+err3[i]/2
            err4[i]= err4[i]+ err3[i]/2
            
        elif (x1[i]>=0 and x2[i]>=0 and x3[i]>=0 and x4[i]<0): # + + + - 
            x2[i]=x2[i]+abs(x4[i]/2)
            x3[i]=x3[i]+abs(x4[i]/2)
            x4[i]=1E-20
            
            err2[i]= err2[i]+err4[i]/2
            err3[i]= err3[i]+ err4[i]/2
            
        elif (x1[i]>=0 and x2[i]<0 and x3[i]<0 and x4[i]>=0): # + - - + 
            x1[i]=x1[i]+abs(x2[i]/2)+abs(x3[i]/2)
            x4[i]=x4[i]+abs(x2[i]/2)+abs(x3[i]/2)
            x2[i]=1E-20 
            x3[i]=1E-20 
            
            err1[i]= err1[i]+err2[i]/2 + err3/2
            err4[i]= err4[i]+ err2[i]/2 + err3/2
            
        elif (x1[i]>=0 and x2[i]>=0 and x3[i]<0 and x4[i]<0): # + + - - 
            x1[i]=x1[i]+abs(x3[i])
            x2[i]=x2[i]+abs(x4[i])
            x4[i]=1E-20 
            x3[i]=1E-20 
    
            err1[i]= err1[i]+err3[i]
            err2[i]= err2[i]+ err4[i]
            
        elif (x1[i]>=0 and x2[i]<0 and x3[i]>=0 and x4[i]<0): # + - + - 
            x1[i]=x1[i]+abs(x2[i])
            x3[i]=x3[i]+abs(x4[i])
            x2[i]=1E-20 
            x4[i]=1E-20 
            
            err1[i]= err1[i]+err2[i]
            err3[i]= err3[i]+ err4[i]
            
        elif (x1[i]>=0 and x2[i]<0 and x3[i]<0 and x4[i]<0): # + - - - 
            x1[i]=x1[i]+abs(x2[i])+abs(x3[i])+abs(x4[i])
            x2[i]=1E-20 
            x3[i]=1E-20 
            x4[i]=1E-20 
            
            err1[i]= err1[i] + err2[i] + err3[i] + err4[i]
            
        elif (x1[i]<0 and x2[i]>=0 and x3[i]>=0 and x4[i]>=0): # - + + + 
            x2[i]=x2[i]+abs(x1[i]/2)
            x3[i]=x3[i]+abs(x1[i]/2)
            x1[i]=1E-20 
            
            err2[i]= err2[i]+err1[i]/2
            err3[i]= err3[i]+ err1[i]/2
            
        elif (x1[i]<0 and x2[i]<0 and x3[i]<0 and x4[i]>=0):  # - - - + 
            x4[i]=x4[i]+abs(x2[i])+abs(x3[i])+ abs(x1[i])
            x1[i]=1E-20 
            x2[i]=1E-20 
            x3[i]=1E-20 
            
            err4[i]= err1[i] + err2[i] + err3[i] + err4[i]

            
        elif (x1[i]<0 and x2[i]>=0 and x3[i]<0 and x4[i]<0):  # - + - - 
            x2[i]=x2[i]+abs(x1[i])+abs(x3[i])+ abs(x4[i])
            x1[i]=1E-20 
            x3[i]=1E-20 
            x4[i]=1E-20 
            
            err2[i]= err1[i] + err2[i] + err3[i] + err4[i]

        elif (x1[i]<0 and x2[i]<0 and x3[i]>=0 and x4[i]<0):  # - - + - 
            x3[i]=x3[i]+abs(x1[i])+abs(x2[i])+ abs(x4[i])
            x1[i]=1E-20 
            x2[i]=1E-20 
            x4[i]=1E-20 
            
            err3[i]= err1[i] + err2[i] + err3[i] + err4[i]

        elif (x1[i]<0 and x2[i]<0 and x3[i]<0 and x4[i]<0): # - - - - 
            x1[i]=1E-20 
            x2[i]=1E-20 
            x3[i]=1E-20 
            x4[i]=1E-20
            
        elif (x1[i]<0 and x2[i]>=0 and x3[i]<0 and x4[i]>=0):  # - + - + 
            x2[i]=x2[i]+abs(x1[i])
            x4[i]=x4[i]+abs(x3[i])
            x1[i]=1E-20 
            x3[i]=1E-20 
            
            err2[i]= err2[i]+err1[i]/2
            err4[i]= err4[i]+ err3[i]/2
            
        elif (x1[i]<0 and x2[i]<0 and x3[i]>=0 and x4[i]>=0): # - - + + 
            x3[i]=x3[i]+abs(x1[i])
            x4[i]=x4[i]+abs(x2[i])
            x1[i]=1E-20 
            x2[i]=1E-20 
            
            err3[i]= err3[i]+err1[i]/2
            err4[i]= err4[i]+ err2[i]/2
            
        elif (x1[i]<0 and x2[i]>=0 and x3[i]>=0 and x4[i]<0): # - + + - 
            x2[i]=x2[i]+abs(x1[i]/2)+abs(x4[i]/2)
            x3[i]=x3[i]+abs(x1[i]/2)+abs(x4[i]/2)
            x4[i]=1E-20 
            x1[i]=1E-20 
            
            err2[i]= err2[i]+err1[i]/2 +err4[i]/2
            err3[i]= err3[i]+ err1[i]/2 +err4[i]/2
            
        else:
            print("Resolve row ",i,", Values: ",x1[i],x2[i],x3[i],x4[i] ) 
    return(x1,x2,x3,x4, err1, err2, err3, err4)



