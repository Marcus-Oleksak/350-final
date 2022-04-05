#!/bin/python3
#Final Project - Part 4

#The following is pseudocode that you may use to help design your main function:
# do build_population_group_list
# do calculate_column_totals
# sort population groups by age group
# do print_report
# sort population groups by total_count descending
# do print_report
# sort population groups by male_count descending
# do print_report
# sort population groups by female_count descending
# do print_report

# The following is pseudocode that you may use to help design your build_population_group_list function:
# prompt for infile
# open infile
# initalize population_groups_list
# for line in infile:
#     split line into strings
#     convert male_count and female_count to ints
#     construct a new PopulationGroup instance
#     if this line is NOT the total line:
#           construct a new PopulationGroup instance
#           append instance to population_groups list
# close infile
# return population_groups_list

# The following is pseudocode that you may use to help design your calculate_column_totals function:
# Receive population_groups_list as parameter
# initialize male_total, female_total, overall_total, percent_total
# for group in population_groups_list:
#     accumulate male_total, female_total, overall_total, percent_total
# return male_total, female_total, overall_total, percent_total

# The following is pseudocode that you may use to help design your print_report function:
# receive population_groups_list, title as parameters
# print blank lines
# print title
# print column headings
# for group in population_groups_list:
#     print a report line using values from PopulationGroup instance
# print column total line using male_total, female_total, overall_total, percent_total


from final_project_p3 import PopulationGroup


def main():
  population_group_list = get_pop_list()
  
  population_group_list.sort(key = by_category)
  print_report(population_group_list, 'Counts by Age Group')
  
  population_group_list.sort(key = by_total_count, reverse = True)
  print_report(population_group_list, 'Counts by Descending Total Count')
  
  population_group_list.sort(key = by_male_count, reverse = True)
  print_report(population_group_list, 'Counts by Descending Male Count')
  
  population_group_list.sort(key = by_female_count, reverse = True)
  print_report(population_group_list, 'Counts by Descending Female Count')

  
def get_pop_list():
  filename = input('Please enter the input filename:')
  infile = open(filename, 'r')
  population_group_list = []
  for line in infile:
    category, male_count, female_count, total_count = line.split()
    if category != 'Total':
      group_object = PopulationGroup(category, male_count, female_count, total_count)
      population_group_list.append(group_object)
  infile.close()
  return population_group_list
  
  
def calculate_column_totals(population_group_list):
  male_total = 0
  female_total = 0
  overall_total = 0
  percent_total = 0
  for group in population_group_list:
    male_total += group.male_count
    female_total += group.female_count
    overall_total += group.total_count
    percent_total += group.calculate_category_percent()
  return male_total, female_total, overall_total, percent_total
    
    
def by_category(g):
  return g.category
  
  
def by_total_count(g):
  return g.total_count
  
  
def by_male_count(g):
  return g.male_count
  
  
def by_female_count(g):
  return g.female_count
  
  
def print_report(population_group_list, report_title):
  male_total, female_total, overall_total, percent_total = calculate_column_totals(population_group_list)
  print('\n\n')
  print('{0:^50}\n'.format(report_title))
  print('{0:<10}{1:>10}{2:>10}{3:>10}{4:>10}'.format('Age Group','Males',
  'Females','Total','Percent'))
  for group in population_group_list:
    print('{0:<10}{1:>10,}{2:>10,}{3:>10,}{4:>10.2f}'.format(
      group.category,
      group.male_count,
      group.female_count,
      group.total_count,
      group.calculate_category_percent()))
  print('{0:<10}{1:>10,}{2:>10,}{3:>10,}{4:>10.2f}'.format('Total', male_total,
  female_total, overall_total, percent_total))


main()
