class Learn_from_Home:    

    details = {}
        
    def addStacks(self,name):
        '''
        Takes the name as parameter and assigns the stack interested by the participant(case sensitive)
        '''
        stack=input("\nThe Stacks are:\nPython\nGO\nWeb\nUI/UX\nFlutter\n\nEnter the stack for which the participant is interested in: ")
        if name in self.details:
            self.details[name]["stack"]=stack
        else:
            self.details[name]={"stack":stack,"role":None,"available_time":None}
        return    
           


    def setMentorOrLearner(self,name):
        '''
        Sets the participant as a Mentor or a Learner
        '''
        role=int(input("\nDo you wish to be\n1.Mentor\n2.Learner\n\nEnter your choice(1 or 2): "))        
        if name in self.details:
            self.details[name]["role"]=role
        else:
            self.details[name]={"stack":None,"role":role,"available_time":None}
        return
        


    def setAvailableTime(self,name):
        '''
        Gets the available time of a mentor
        '''
        if self.details[name]["role"]==1 :
            avail_time=int(input("\nEnter available time by mentor in hours: ")) 
            if name in self.details:
                self.details[name]["available_time"]=avail_time
            else:
                self.details[name]={"stack":None,"role":None,"available_time":avail_time}
        return
        


    def getMentor(self,stack,time):
        '''
        Finds the available mentors for the required stack and time
        '''
        check=0
        print("\nThe available mentors are: ")
        for x in self.details:
            if self.details[x]["stack"]==stack and self.details[x]["available_time"]>=time:
                print("{} ".format(x))
                check=1
        if check==0:
            print("Sorry, no mentors are available for the given stack and ")
        return

        
        

A=Learn_from_Home()
ans='y'
while ans=='y':
    print("\n\n_____________Participant Details____________\n")
    name=input("\nEnter the name of the participant: ")
    A.addStacks(name)
    A.setMentorOrLearner(name)
    A.setAvailableTime(name)
    ans=input("\nDo you want to enter the details of another participnt?(y/n): ")
ans='y'
while ans=='y':
    print("\n\n_____________Get Mentor____________\n")
    stack=input("\nThe Stacks are:\nPython\nGO\nWeb\nUI/UX\nFlutter\n\nEnter a stack: ")
    time=int(input("Enter the time in hours: "))
    A.getMentor(stack,time)
    ans=input("\nDo you want to check the mentor availability of another stack and time?(y/n): ")
        
    
