print(">>>>>>>>>>>>>>>>WELCOMET ABC PARKING SYSTEM<<<<<<<<<<<<<<<<")
first_flr=[]
second_flr=[]
third_flr=[]
fourth_flr=[]

while True:
    a=input('Choose your Option (Park / Exit):').lower()
    if a=='park':
        veh_typ = int(input("enter your vehicle type (2 wheeler/4 wheeler/3 wheeler/6 wheeler):"))
        veh_no = input("enter your vehicle no:")
        ti = int(input("how many hours to park(*please mention in hours):"))
        flr = int(input("choose a floor to park your vechile(1/2/3/4):"))
        d={'id':veh_no,'veh_type':veh_typ,'hours':ti}
        def flr_add(x):
            if len(x)>=3:
                print("this floor is full")
                newflr= int(input("choose a newfloor (1/2/3/4):"))
                if newflr == 1:
                    flr_add(first_flr)
                elif newflr == 2:
                    flr_add(second_flr)
                elif newflr == 3:
                    flr_add(third_flr)
                elif newflr == 4:
                    flr_add(fourth_flr)
            else:
                x.append(d)
                print(x)
        if flr==1:
            flr_add(first_flr)
        elif flr==2:
            flr_add(second_flr)
        elif flr==3:
            flr_add(third_flr)
        elif flr==4:
            flr_add(fourth_flr)
        print("********************************************")
    elif a=='exit':
        print("Thank you for using ABC parking")
        break
