class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        MAJORS = ("Math", "Science", "English", "Art", "History")
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        if major not in MAJORS:
            raise ValueError
        else:
            self.major = major
        x = isinstance(gpa, float)
        if x == False:
            raise ValueError
        elif gpa < 0 or gpa > 4.0:
            raise ValueError
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major in " + self.major + " with gpa: " + str(self.gpa)
