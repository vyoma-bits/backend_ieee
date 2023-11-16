import csv

class Course:
    def __init__(self, name, department, instructor, examination_date):
        self.name = name
        self.department = department
        self.instructor = instructor
        self.examination_date = examination_date
        self.sections = []

    def get_all_sections(self):
        return self.sections

    def __str__(self):
        print("Course:", self.name)
        print("Department:", self.department)
        print("Instructor:", self.instructor)
        print("Examination Date:", self.examination_date)

    def populate_new_sections(self, sections):
        if not self.sections:
            self.sections = sections

class Section:
    def __init__(self, course, day, slot, type):
        self.course = course
        self.day = day
        self.slot = slot
        self.type = type
        self.occupied_slots = {day: [slot]}

    def get_occupied_slots(self):
        return self.occupied_slots

    def is_clash(self, other_section):
        return self.day == other_section.day and self.slot == other_section.slot

class Timetable:
    def __init__(self):
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)

    def check_for_clashes(self):
        examination_clashes = []
        lecture_section_clashes = []

        for course1 in self.courses:
            for course2 in self.courses:
                if course1 != course2 and course1.examination_date == course2.examination_date:
                    examination_clashes.append((course1.name, course2.name))

        for course in self.courses:
            for section1 in course.get_all_sections():
                for section2 in course.get_all_sections():
                    if section1 != section2 and section1.is_clash(section2):
                        lecture_section_clashes.append((section1.course.name, section1.type, section2.course.name, section2.type))

        return examination_clashes, lecture_section_clashes

    def export_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow(['Course', 'Department', 'Instructor', 'Examination Date', 'Day', 'Slot', 'Type'])

            for course in self.courses:
                for section in course.get_all_sections():
                    writer.writerow([course.name, course.department, course.instructor, course.examination_date, section.day, section.slot, section.type])
# Import the necessary classes


# Create a new course
course1 = Course("MEOW", "Computer Science", "Vyoma", "20240512")

# Create a section for the course
section1 = Section(course1, "Monday", 10, "Lecture")

# Add the section to the course
course1.populate_new_sections([section1])

# Create another course
course2 = Course("GENERAL CHEMISTRY", "Computer Science", "DAVID", "20240512")

# Create a section for the second course
section2 = Section(course2, "Tuesday", 11, "Lecture")

# Add the section to the course
course2.populate_new_sections([section2])

# Create a timetable
timetable = Timetable()

# Enroll the courses in the timetable
timetable.enroll_course(course1)
timetable.enroll_course(course2)

# Check for clashes
examination_clashes, lecture_section_clashes = timetable.check_for_clashes()

# Print clash information
if examination_clashes:
    print("Examination clashes:")
    for clash in examination_clashes:
        print("- " + clash[0] + " and " + clash[1])

if lecture_section_clashes:
    print("Lecture/section clashes:")
    for clash in lecture_section_clashes:
        print("- " + clash[0] + " (" + clash[1] + ") and " + clash[2] + " (" + clash[3] + ")")

# Export the timetable to a CSV file
timetable.export_to_csv("timetable.csv")
print("done")

    

