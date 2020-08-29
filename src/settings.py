"""
TODO: 
for every option create class with possible options etc, die wird adnn aufgerufen wenn man nach den Options fragt

"""


class zipSettings():
    true_in = False 
    """
    Settings for python deep search
    """
    def __init__(self, depth=3):
        self.depth = depth #defines depth of searching for ZIPfolders in Folder 
        self.settingslist = ["depth"]  #append here when adding new settings 
    def __enter__(self):
        #get data from settings storage 
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        #save actual settings to settings storage
        pass 

    def get_depth(self):
        return self.depth
    
    def set_depth(self,d:int):
        try:
            self.depth = d
        except Exception as e:
            print(e)
            return e 
    
    def run(self):
        #possibility to set settings 
        print("> Hello there you can alter these settings:")
        c = 0 
        for i in self.settingslist:
            c+=1 
            print(">"+str(c)+": "+str(i))
        
        def get_in():
            inp = input("Option number: ")
            try:
                if int(inp) <= len(self.settingslist):
                    print("do sth")
                else:
                    get_in()
            except Exception as e:
                print(e)
                print("\n\n")
                get_in()
        get_in()
        

if (__name__ == "__main__"):
    zset = zipSettings()
    zset.run()
    
    