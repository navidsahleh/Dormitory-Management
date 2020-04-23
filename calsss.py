import pickle

class Student(object):
    def __init__(self,name,code):
        self.name = name
        self.code = code
        
    '''def edit_student(self,record):
        with open('navid.txt','r+') as f:
            lines=f.readlines()
            for i in range(0,len(lines)):
                if record in lines[i]:
                    k=input("give the new name: ")
                    p=lines[i].split(" ")
                    lines[i]=k+" "+p[1]
                    break
            f.seek(0)
            f.writelines(lines)'''
      
            
            
    def edit_student(self,p,record):
        for i in p:
            if i.code==record:
                k=input("give the new name: ")
                i.name=k
                break
        with open('name.txt','wb') as f:
            for i in p:
                pickle.dump(i,f, protocol=pickle.HIGHEST_PROTOCOL)
        
        
    
    def delete_student(self,p,record):
        for i in range(0,len(p)):
            if p[i].code==record:
                del p[i]
                break
        with open('name.txt','wb') as f:
            for i in p:
                pickle.dump(i,f, protocol=pickle.HIGHEST_PROTOCOL)
        
    
                
    def get_name(self):
        print(self.name)
    
    
class Manager(object):
    
    def __init__(self,name=None):
        self.name=name
        self.stu = []
        self.k= None
    
    def set_name_man(self,name):
        self.name=name
       
    def save_room(self,room):
        with open('room.txt','ab') as f:
            pickle.dump(room,f, protocol=pickle.HIGHEST_PROTOCOL)
        
    def get_k(self):
        return self.k
            
    def edit_student(self,p,record):
        Student.edit_student(self,p,record)
        
    def delete_student(self,p,record):
        Student.delete_student(self,p,record)
        
    def show_member(self,room):
        room.show_member()
        
    '''def add(self,person):
        name=person.name
        record=person.code
        with open('navid.txt','a+') as f:
            f.write(name)
            f.write(' '+str(record))
            f.write('\n')'''
            
     #jagozin commente        
    def add(self,person):
        with open('name.txt','ab') as f:
            pickle.dump(person,f, protocol=pickle.HIGHEST_PROTOCOL)
#            f.write('\n')
        

    def load_name_file(self):
        with open('name.txt', "rb") as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break
        
    def load_room_file(self):
        with open('room.txt', "rb") as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break
       
    def sign_up(self,user,pas,name):
        with open('userpass.txt','a+') as f:
            f.write(user)
            f.write(' '+pas)
            f.write(' '+name+'\n')
            print("signing up was succesfull...")
            
    def log_in(self,user,pas):
        with open('userpass.txt','r+') as f:
            lines=f.readlines()
            for i in range(0,len(lines)):
                z=lines[i].split(' ')
                if z[0]==user and z[1]==pas:
                    print("welcome",z[2])
                    self.name=z[2]
                    self.k=False
                    break
                else:
                    print("something is wrong!!!")
                    self.k=True
                    break

    def find_student(self,record,p):
        for i in p:
            if i.code==record:
                return i
        
    
    def add_to_room(self,p_room,student,rnum):
        for i in p_room:
            if i.roomnum==rnum:
                if len(i.member)<int(i.capacity):
                    i.member.append(student)
                    print(i.member)
                else:
                    print("the room is full")
                break
        with open('room.txt','wb') as f:
            for i in p_room:
                pickle.dump(i,f, protocol=pickle.HIGHEST_PROTOCOL)
                    
            
            
    '''def edit_student(self,record):
        with open('navid.txt','r+') as f:
            lines=f.readlines()
            for i in range(0,len(lines)):
                if record in lines[i]:
                    k=input("give the new name: ")
                    p=lines[i].split(" ")
                    lines[i]=k+" "+p[1]
                    break
            f.seek(0)
            f.writelines(lines)'''


        
    
#    def delete_student(self,record):
#        with open("navid.txt", "r") as f:
#            lines = f.readlines()
#            with open("navid.txt", "w") as f:
#                for line in lines:
#                    if record not in line: 
#                        f.write(line)

            
    
    def __str__(self):
        return self.name
    
#    def add_stu(self,student):
#        self.stu.append(student)
#        print(self.stu)
        
        
#    def find_stu(self,record):
#        for Student in self.stu:
#            if record==Student.code:
#                return Student

    
class Room(object):
    def __init__(self,roomnum,capacity,price,floornum):
        self.roomnum = roomnum
        self.capacity = capacity
        self.price = price
        self.floornum = floornum
        self.member = []
        
        
    def add_member(self,student):
        if len(self.member)<int(self.capacity):
            self.member.append(student)
            print(self.member)
        else:
            print("the room is full!")
        
    def show_member(self):
        for Student in self.member:
            Student.get_name()
            
    def delete_member(self,name):
        for Student in self.member:
            if name== Student.get_name():
                self.member.remove(Student)
                
        
            

#he = Student('vahid','12467')
#she = Student('navid','23252')
#manager = Manager('kasra')
#room = Room('1','4','12','1')
#room.add_member(he)
#room.add_member(she)
#manager.show_member(room)



#he = Student('vahid','12467')
#she = Student('navid','23252')
#manager = Manager('kasra')
#record = "23252"
#manager.add(he)
#manager.add(she)

###### edit kardane daneshjo ###############
#he = Student('mahsa','1533')
#she = Student('sanaz','234349')
#manager = Manager('kasra')
#record = "234349"
#manager.add(he)
#manager.add(she)
#p=list(manager.load())
#manager.edit_student(p,record)
#############################################




############ delete an student###############
#manager = Manager('kasra')
#p=list(manager.load())
#record= "12467"
#manager.delete_student(p,record)
#############################################


########### username and password ############

#manager = Manager()                
#l=input("1-sign up\n2-log in")
#if l=="1":
#    name=input("Name: ")
#    manager.set_name_man(name)
#    user=input("Username: ")
#    pas=input("Password: ")
#    manager.sign_up(user,pas,name)
#elif l=="2":
#    user=input("Username: ")
#    pas=input("Password: ")
#    manager.log_in(user,pas)


#################################################
                
                
############### find student and then add to a room ####
#manager = Manager('kamran')
#room1 = Room("1","4","5000","1")
#room2 = Room("2","4","5000","1")
#p=list(manager.load())
#record=input("give me the number of Student you want to add: ")
#he=manager.find_student(record,p)
#room1.add_member(he)
#manager.save_room(room1)
#p=list(manager.load())
#for i in p:
#    z=i.member[0]
#    print(z.name)
#    print(z.code)

                
                
#################################################                            
                
                
                
    

mk=True
k=True
while k==True:
    manager = Manager()                
    l=input("1-sign up\n2-log in\n")
    if l=="1":
        name=input("Name: ")
        manager.set_name_man(name)
        user=input("Username: ")
        pas=input("Password: ")
        manager.sign_up(user,pas,name)
    elif l=="2":
        user=input("Username: ")
        pas=input("Password: ")
        manager.log_in(user,pas)
        if manager.get_k()==False:
            k=False
    


while mk==True:
    
            
    print("\nwhat do you want to do?\n"+"\n1"+")"+"New student"+"\n2"+")"+"Register new block"+
        "\n3"+")"+"Register new room"+"\n4"+")"+"edit Student"+"\n5"+")"+
        ")"+"Add member to room"+"\n6"+")"+"Delete All member from a room"+"\n7"+")"+"exit")
    ask=int(input())

#add new Student
    if ask==1:
    
        name=input("give me the name of student:\n")
        record=input("give me the record of student\n")
        he = Student(name,record)
    
        manager.add(he)
        del name

#Register new room 
    elif ask==3:
        num=input("Please enter a Number for room:\n")
        cap=input("Please enter the Capicity of room:\n")
        price=input("Please enter the rent price for room\n")
        floor=input("Please enter the floor number:\n")
        room = Room(num,cap,price,floor)
        manager.save_room(room)
            
            
#        elif soal=="2":
            

    elif ask==4:
    
        record=input("Please enter Student Number:\n")
        print("\n1"+")"+"Delete Student"+"\n2"+")"+"Edit Student name"+"\n3"+")"+"Chosse room"+"\n4"+")"+"Show room ")
        give=int(input())
    
    
        #delete Student
        if give==1:
        
            p=list(manager.load_name_file())
            manager.delete_student(p,record)
            del record
        
        #edit Student name
        elif give==2:
            p=list(manager.load_name_file())
            manager.edit_student(p,record)
            del record 

#add member to room
    elif ask==5:
        rnum=input("give me the number for the room: ")
        record=input("give me the record of Student you want to add: ")
        p_name=list(manager.load_name_file())
        he=manager.find_student(record,p_name)
        p_room=list(manager.load_room_file())
        manager.add_to_room(p_room,he,rnum)
        

#exit
    elif ask==7:
        mk=False

