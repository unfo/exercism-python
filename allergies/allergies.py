class Allergies(object):
	_allergies = {
		'eggs': 		1,
		'peanuts': 		2,
		'shellfish': 	4,
		'strawberries': 8,
		'tomatoes': 	16,
		'chocolate': 	32,
		'pollen': 		64,
		'cats': 		128
	}

	def __init__(self, allergy_value):
		self.value = allergy_value
		self.lst = [allergy for allergy, value in self._allergies.items() if self.value & value == value]

	def is_allergic_to(self, name):
		return (name in self.lst)
	
