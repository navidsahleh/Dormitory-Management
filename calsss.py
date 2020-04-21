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
        with open('navid.txt','wb') as f:
            for i in p:
                pickle.dump(i,f, protocol=pickle.HIGHEST_PROTOCOL)
        
        
    
    def delete_student(self,p,record):
        for i in range(0,len(p)):
            if p[i].code==record:
                del p[i]
                break
        with open('navid.txt','wb') as f:
            for i in p:
                pickle.dump(i,f, protocol=pickle.HIGHEST_PROTOCOL)
        
    
                
    def get_name(self):
        print(self.name)
    
    
class Manager(object):
    
    def __init__(self,name):
        self.name=name
        self.stu = []
            
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
        with open('navid.txt','ab') as f:
            pickle.dump(person,f, protocol=pickle.HIGHEST_PROTOCOL)
#            f.write('\n')
        

    def load(self):
        with open('navid.txt', "rb") as f:
            while True:
                try:
                    yield pickle.load(f)
                except EOFError:
                    break
       
    def sign_up(self,user,pas):
        with open('userpass.txt','a+') as f:
            f.write(user)
            f.write(' '+pas)
            
    def log_in(self,user,pas):
        with open('userpass.txt','r+') as f:
            lines=f.readlines()
            for i in range(0,len(lines)):
                z=lines[i].split(' ')
                if z[0]==user and z[1]==pas:
                    print("welcome",user)
                    break
                else:
                    print("something is wrong!!!")


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
    
    def add_stu(self,student):
        self.stu.append(student)
        print(self.stu)
        
        
    def find_stu(self,record):
        for Student in self.stu:
            if record==Student.code:
                return Student

    
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
manager = Manager('kasra')                
l=input("1-sign up\n2-log in")
if l=="1":
    user=input("Username: ")
    pas=input("Password: ")
    manager.sign_up(user,pas)
elif l=="2":
    user=input("Username: ")
    pas=input("Password: ")
    manager.log_in(user,pas)


#################################################


'''
manager = Manager("MR rahmani")
print("Welcome",manager)            
print("what do you want to do?"+"\n1"+")"+"New student"+"\n2"+")"+"Register new block"+
    "\n3"+")"+"Register new room"+"\n4"+")"+"edit Student")
ask=int(input())

#add new Student
if ask==1:
    
    name=input("give me the name of student:\n")
    record=input("give me the record of student\n")
    he = Student(name,record)
    
    manager.add(he)
    del name

elif ask==3:
    num=input("Please enter a Number for room:\n")
    cap=input("Please enter the Capicity of room:\n")
    price=input("Please enter the rent price for room\n")
    floor=input("Please enter the floor number:\n")
    room = Room(num,cap,price,floor)
    
    print("what do you want to do?"+"\n1"+")"+"Add member"+"\n2"+")"+"Delete member")
    soal=input()
    
    if soal=="1":
        name=input("give me the name of student:\n")
        record=input("give me the record of student\n")
        he = Student(name,record)
        room.add_member(he)
        
#    elif soal=="2":
        


elif ask==4:
    
    record=input("Please enter Student Number:\n")
    print("\n1"+")"+"Delete"+"\n2"+")"+"Edit"+"\n3"+")"+"Chosse room"+"\n4"+")"+"Show room ")
    give=int(input())
    
    
    #delete Student
    if give==1:
        
        manager.delete_student(record)
        del record
        
    #edit Student name
    elif give==2:
        manager.edit_student(record)
        del record 

'''




