class Animal:
    def __init__(self):
        self.eyes = 2
        
    def breathe(self):
        print("Inhale , Exhale.")
        
class Tiger(Animal):
    def __init__(self):
        super().__init__()
        
    def breathe(self):
        super().breathe()
        print("doing on the surface")
        
    def run(self):
        print("moving very fast.")
        
bagha = Tiger()
bagha.run()
bagha.breathe()
print(f"tiger have {bagha.eyes} eyes")