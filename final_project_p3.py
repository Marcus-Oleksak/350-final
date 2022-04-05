#!/bin/python3
#Copy and paste the module you developed in Exercise 3 below.

class PopulationGroup:
  
  def __init__(self, category, male_count, female_count, total_count):
    self.category = str(category)
    self.male_count = int(male_count)
    self.female_count = int(female_count)
    self.total_count = int(total_count)
    
  def calculate_category_percent(self):
    grand_total = 951982
    category_percent = (self.total_count / grand_total) * 100
    return category_percent
    

def main():
  print('Unit testing output follows...')
  print('\nTesting the constructor:')
  expected_age_group = '40-44'
  expected_male_count = 28176
  expected_female_count = 29271
  expected_total_count = 57447
  test_case = PopulationGroup(expected_age_group, expected_male_count,
  expected_female_count, expected_total_count)
  print(test_case.category)
  print(test_case.male_count)
  print(test_case.female_count)
  print(test_case.total_count)
  print('\nTesting the calculate_category_percentage method:')
  print(test_case.calculate_category_percent())
  

if __name__=='__main__':
  main()