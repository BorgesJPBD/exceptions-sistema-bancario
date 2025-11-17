class Running:
    def __init__(self):
        self.is_running = True
        
    def system_run(self):
        while self.is_running == True:
            print("please select a option: 1, 2 ,3(3 stops the system)")
            choice = input("Choooose: ")
            if choice == "1":
                print("1 worked")
            if choice == "2":
                print("2 worked")
            if choice == "3":
                print("3 worked")
                print("by-bye")
                self.is_running = False
                
                
system = Running()
system.system_run()