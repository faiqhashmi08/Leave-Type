import datetime

class Employee:
    def __init__(self, name, leave_balance):
        self.name = name
        self.leave_balance = leave_balance
        self.leave_history = []

    def apply_for_leave(self, start_date, end_date, leave_type):
        days_requested = (end_date - start_date).days + 1
        if days_requested > self.leave_balance:
            return "Insufficient leave balance"
        else:
            self.leave_balance -= days_requested
            leave_record = {"start_date": start_date, "end_date": end_date, "leave_type": leave_type}
            self.leave_history.append(leave_record)
            return "Leave application successful"

class LeaveManager:
    def __init__(self, employees):
        self.employees = employees

    def get_employee(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee
        return None

    def apply_for_leave(self, employee_name, start_date, end_date, leave_type):
        employee = self.get_employee(employee_name)
        if employee is None:
            return "Employee not found"
        else:
            return employee.apply_for_leave(start_date, end_date, leave_type)
