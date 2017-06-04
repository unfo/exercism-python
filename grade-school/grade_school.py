from collections import defaultdict

class School(object):
    def __init__(self, name):
        self.name = name
        self.grades = defaultdict(lambda: set())

    def add(self, student, _grade):
        self.grades[_grade].add(student)

    def grade(self, _grade):
        return self.grades[_grade]

    def sort(self):
        # Pretty sure hash keys are sorted by default
        # But I'd rather be 100% explicit here.
        for _grade in sorted(self.grades.keys()):
            if len(self.grades[_grade]) > 0:
                yield tuple([_grade, tuple(sorted(self.grades[_grade]))])
            
