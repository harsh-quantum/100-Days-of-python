class job:
    name = None
    salary = None
    work_hours = None

    def __init__(self, name, salary, work_hours):
        self.name = name
        self.salary = salary
        self.work_hours = work_hours

    def details(self):
        print(f"Job type: {self.name}\nSalary: {self.salary}\nHours worked: {self.work_hours}")


class doctor(job):
    speciality = None
    years = None

    def __init__(self, speciality, years):
        self.name = "Doctor"
        self.salary = "£50,000"
        self.work_hours = "50"
        self.speciality = speciality
        self.years = years

    def details(self):
        print(
            f"Job type: {self.name}\nSalary: {self.salary}\nHours worked: {self.work_hours}\nSpecialtiy : {self.speciality}\nYears: {self.years}")


class teacher(job):
    subject = None
    position = None

    def __init__(self, subject, position):
        self.name = "Teacher"
        self.salary = "£30,000"
        self.work_hours = "40"
        self.subject = subject
        self.position = position

    def details(self):
        print(
            f"Job type: {self.name}\nSalary: {self.salary}\nHours worked: {self.work_hours}\nSubject : {self.subject}\nPosition: {self.position}")


Lawyer = job("Lawyer", "£50,000", "80")
Lawyer.details()
print()
computer_s_t = teacher("Computer Science", "Classroom Teacher")
computer_s_t.details()

print()
pediatric_doctor = doctor("Pediatric Consultant", "7")
pediatric_doctor.details()
