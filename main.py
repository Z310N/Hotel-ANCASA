import random
import datetime
  
# Global List Declaration
name = []
phno = []
add = []
checkin = []
checkout = []
room = []
rc = []
p = []
roomno = []
custid = []
day = []
  
# Global Variable Declaration
  
i = 0
  
# Home Function
def Home():
     
    print("\t\t\t\t\t\t WELCOME TO HOTEL ANCASA\n")
    print("\t\t\t 1 Booking\n")
    print("\t\t\t 0 Exit\n")
  
    ch=int(input("->"))
     
    if ch == 1:
        print(" ")
        Booking()
     
    else:
        exit()
 
# Function used in booking
  
def date(c):
     
    if c[2] >= 2020 and c[2] <= 2022:
         
        if c[1] != 0 and c[1] <= 12:
             
            if c[1] == 2 and c[0] != 0 and c[0] <= 31:
                 
                if c[2]%4 == 0 and c[0] <= 29:
                    pass
                 
                elif c[0]<29:
                    pass
                 
                else:
                    print("Invalid date\n")
                    name.pop(i)
                    phno.pop(i)
                    add.pop(i)
                    checkin.pop(i)
                    checkout.pop(i)
                    Booking()
             
             
            # if month is odd & less than equal
            # to 7th  month
            elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31:
                pass
             
            # if month is even & less than equal to 7th
            # month and not 2nd month
            elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2:
                pass
             
            # if month is even & greater than equal
            # to 8th  month
            elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31:
                pass
             
            # if month is odd & greater than equal
            # to 8th  month
            elif c[1]>=8 and c[1]%2!=0 and c[0]<=30: 
                pass
             
            else:
                print("Invalid date\n")
                name.pop(i)
                phno.pop(i)
                add.pop(i)
                checkin.pop(i)
                checkout.pop(i)
                Booking()
                 
        else:
            print("Invalid date\n")
            name.pop(i)
            phno.pop(i)
            add.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            Booking()
             
    else:
        print("Invalid date\n")
        name.pop(i)
        phno.pop(i)
        add.pop(i)
        checkin.pop(i)
        checkout.pop(i)
        Booking()
  
  
# Booking function
def Booking():
     
        # used global keyword to
        # use global variable 'i'
        global i
        print(" BOOKING ROOMS")
        print(" ")
         
        while 1:
            n = str(input("Name: "))
            p1 = str(input("Phone No.: "))
            a = str(input("Address: "))
             
            # checks if any field is not empty
            if n!="" and p1!="" and a!="":
                name.append(n)
                add.append(a)
                break
                 
            else:
                 print("\tName, Phone no. & Address cannot be empty..!!")
              
        cii=str(input("Check-In(dd/mm/yyy/): "))
        checkin.append(cii)
        cii=cii.split('/')
        ci=cii
        ci[0]=int(ci[0])
        ci[1]=int(ci[1])
        ci[2]=int(ci[2])
        date(ci)
          
        coo=str(input("Check-Out: "))
        checkout.append(coo)
        coo=coo.split('/')
        co=coo
        co[0]=int(co[0])
        co[1]=int(co[1])
        co[2]=int(co[2])
         
        # checks if check-out date falls after
        # check-in date
        if co[1]<ci[1] and co[2]<ci[2]:
             
            print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
            name.pop(i)
            add.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            Booking()
        elif co[1]==ci[1] and co[2]>=ci[2] and co[0]<=ci[0]:
             
            print("\n\tErr..!!\n\tCheck-Out date must fall after Check-In\n")
            name.pop(i)
            add.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            Booking()
        else:
            pass
         
        date(co)
        d1 = datetime.datetime(ci[2],ci[1],ci[0])
        d2 = datetime.datetime(co[2],co[1],co[0])
        d = (d2-d1).days
        day.append(d)
          
        # randomly generating room no. and customer
        # id for customer
        rn = random.randrange(40)+300
        cid = random.randrange(40)+10
         
         
        # checks if alloted room no. & customer
        # id already not alloted
        while rn in roomno or cid in custid:
            rn = random.randrange(60)+300
            cid = random.randrange(60)+10
             
        rc.append(0)
        p.append(0)
               
        if p1 not in phno:
            phno.append(p1)
        elif p1 in phno:
            for n in range(0,i):
                if p1== phno[n]:
                    if p[n]==1:
                        phno.append(p1)
        elif p1 in phno:
            for n in range(0,i):
                if p1== phno[n]:
                    if p[n]==0:
                        print("\tPhone no. already exists and payment yet not done..!!")
                        name.pop(i)
                        add.pop(i)
                        checkin.pop(i)
                        checkout.pop(i)
                        Booking()
        print("")
        print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")
        print("Room No. - ",rn)
        print("Customer Id - ",cid)
        roomno.append(rn)
        custid.append(cid)
        i=i+1
        n=int(input("0-BACK\n ->"))
        if n==0:
            Home()
        else:
            exit()
 
# RECORD FUNCTION
def Record():
     
    # checks if any record exists or not
    if phno!=[]:
        print("        *** HOTEL RECORD ***\n")
        print("| Name        | Phone No.    | Address       | Check-In  | Check-Out     | Room Type     | Price      |")
        print("----------------------------------------------------------------------------------------------------------------------")
         
        for n in range(0,i):
            print("|",name[n],"\t |",phno[n],"\t|",add[n],"\t|",checkin[n],"\t|",checkout[n],"\t|",room[n],"\t|",price[n])
         
        print("----------------------------------------------------------------------------------------------------------------------")
     
    else:
        print("No Records Found")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
         
    else:
        exit()
 
# Driver Code
Home()