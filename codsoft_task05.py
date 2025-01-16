def Choice():
    
    print("Contact book menu:")
    print("1.Add Contact\n2.View contact\n3.Search Contact\n4.Update Contact\n5.Delete Contact\n6.QUIT")

def Add_Contact():
    name=input("enter name:").lower()
    while True:
        Ph_no=input("Enter phone number: ").lower()
        if len(Ph_no)!=10:
            print("invalid phone number")
        else:
            break
    term='@gmail.c'
    while True:
        Email=input("Enter Email:").lower()
        if term in Email:
            break
        else:
            print("invalid entry")
    Addr=input("enter address:").lower()
    lst=[name,Ph_no,Email,Addr]
    
    LIST.append(lst)
    
    print("Contact added successfully!")

def View_Contact():
    print("Contact List is as below:")
    ln=len(LIST)
    for i in range(ln):
        ct=LIST[i][0] + '-' + LIST[i][1]
        print((i+1),".",ct)
        
def Search_Contact():
    NorPH=input("enter name or phone number whose details are to be searched for:").lower()
    ln=len(LIST)
    if any(NorPH in list for list in LIST) :
        for i in range(ln):
            if NorPH==LIST[i][0] or NorPH==LIST[i][1]:
                print(LIST[i])
            else:
                pass    
    else:
        print("invalid Entry!")

def Update_Contact():
    key=input("enter the name of the contact to be updated:").lower()
    ln=len(LIST)
    if any(key in list for list in LIST) :
        for i in range(ln):
            if LIST[i][0].lower()==key.lower():
                LIST[i][1]=input("enter new Phone number:")
                LIST[i][2]=input("enter new Email :")
                LIST[i][3]=input("enter new Address:")
            else:
                pass
    else:
        print("invalid entry!")   
    
    print("Contact updated Successfully!")    
def Delete_Contact():
    
    item=input("enter the name of the contact to be deleted:").lower()
    global LIST
    LIST= [sublist for sublist in LIST if item not in sublist]
    print("Contact", item, "deleted.")
    print(LIST)
    

         
        
             
Choice()
lst=[]
LIST=[]
New=[]
while True:
    ch=int(input("enter your choice:"))
    if ch==1:
        Add_Contact()
        print (LIST)
        
        
    elif ch==2:
        View_Contact()
        
    elif ch==3:
        Search_Contact()  
          
    elif ch==4:
        Update_Contact()
    
    elif ch==5:
        Delete_Contact()
    
    elif ch==6:
        print("exiting contact book!")
        break
    
    else:
        print("invalid choice!")
