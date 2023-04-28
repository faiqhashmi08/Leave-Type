class LeaveType:
    def __init__(self, name, max_days):
        self.name = name
        self.max_days = max_days
        self.available_days = max_days
        
    def request_leave(self, days):
        if days > self.available_days:
            print("Sorry, you do not have enough available days for this leave type.")
        else:
            self.available_days -= days
            print(f"{days} days of {self.name} leave requested and approved.")
    
    def add_days(self, days):
        self.available_days += days
        if self.available_days > self.max_days:
            self.available_days = self.max_days
        print(f"{days} days of {self.name} leave added. Available days: {self.available_days}")
        
    def __str__(self):
        return f"{self.name} leave: {self.available_days} available days out of {self.max_days} max days."
