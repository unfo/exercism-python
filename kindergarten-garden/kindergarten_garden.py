class Garden(object):
    PLANTS = {
        'C': 'Clover',
        'G': 'Grass',
        'R': 'Radishes',
        'V': 'Violets'
    }

    STUDENTS = [
        'Alice', 'Bob', 'Charlie', 'David',
        'Eve', 'Fred', 'Ginny', 'Harriet',
        'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]

    def __init__(self, plant_rows, students=STUDENTS):
        self.plant_rows = plant_rows.split('\n')
        self.students = sorted(students)
        self.students_plants = {}

        for idx, name in enumerate(self.students):
            self.students_plants[name] = []
            for row in self.plant_rows:
                # Dis here is reaaal ugly.
                # I'll return to it in a few days of thought
                # But since it passes, I'll submit it
                if len(row) >= (idx+1)*2:
                    self.students_plants[name].append(row[idx*2])
                    self.students_plants[name].append(row[idx*2+1])

    def plants(self, name):
        if name not in self.students_plants:
            return []
        return [Garden.PLANTS[p] for p in self.students_plants[name]]
