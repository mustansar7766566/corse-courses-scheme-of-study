#F22BSEEN1E02076(Mustansar Hussain Tariq)


class Course:
    def __init__(self, code, name, credit_hours):
        self.code = code
        self.name = name
        self.credit_hours = credit_hours

    def __str__(self):
        return f"{self.code}: {self.name} ({self.credit_hours} credits)"


class SchemeOfStudy:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course_code):
        for course in self.courses:
            if course.code == course_code:
                self.courses.remove(course)

    def calculate_total_credit_hours(self):
        total_credits = 0
        for course in self.courses:
            total_credits += course.credit_hours
        return total_credits

    def __str__(self):
        scheme_str = f"{self.name}:\n"
        for course in self.courses:
            scheme_str += f"\t{str(course)}\n"
        scheme_str += f"Total credit hours: {self.calculate_total_credit_hours()}"
        return scheme_str
