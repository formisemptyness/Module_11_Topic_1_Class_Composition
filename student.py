class Student:
    '''Student class using '''
    def __init__(self, maj, s_date, _gpa):
        self.major = maj
        self.start_date = s_date
        self.gpa = _gpa

    def change_major(self, maj):
        self.major = maj

    def update_gpa(self, _gpa):
        self.gpa = _gpa

    def display(self):
        return 'Major: ' + self.major + '\n' + 'Start Date: ' + self.start_date + '\n' + 'Grade Point Average: ' + str(self.gpa)
