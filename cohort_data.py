"""Functions to parse a file containing student data."""

def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    houses = []
    for i in open(filename):
      i = i.rstrip().split('|')
      _,_,house,_,_ = i
      if house:
        houses.append(i[2])
      
  
    houses = set(houses)

    # TODO: replace this with your code

    return houses


def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """
    students = []
    for i in open(filename):
      i = i.rstrip().split('|')
      fn, ln, _, _, cohorts = i
      name = fn+ ' '+ln
      if cohort == cohorts:
        students.append(name)
      elif cohort == 'All' and cohorts != 'I' and cohorts != 'G':
        students.append(name)
      
 
      
    

    # TODO: replace this with your code

    return sorted(students)


def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """
    
    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []
    studentlist = []
    cohort_tuple = ("Dumbledore's Army","Gryffindor","Hufflepuff","Ravenclaw","Slytherin","Ghosts","Instructors")
    
    cohort_dict = {}

    for i in open(filename):
      i = i.rstrip()
      i = i.split('|')
      fn, ln, house, insturctor, cohorts = i
      name = fn+' '+ln
    #   cohort_dict[house] = [name]
    #   cohort_dict[house] = cohort_dict[house] + [name]
    #   # if house != '':
    #   #   cohort_dict[house] = []
    #   #   cohort_dict[house] = cohort_dict[house] + [name]
    #   # elif cohort == 'I':
    #   #   cohort_dict['insturctor'] = 
    #   # print(cohort_dict[house]+[name])
    # print(cohort_dict)
      
      
    # print(cohort_dict)

      if house == cohort_tuple[0]:
        dumbledores_army.append(name)
      elif house == cohort_tuple[1]:
        gryffindor.append(name)
      elif house == cohort_tuple[2]:
        hufflepuff.append(name)
      elif house == cohort_tuple[3]:
        ravenclaw.append(name)
      elif house == cohort_tuple[4]:
        slytherin.append(name)
      elif cohorts == "G":
        ghosts.append(name)
      elif cohorts == "I":
        instructors.append(name)

    dumbledores_army.sort()
    gryffindor.sort()
    hufflepuff.sort()
    ravenclaw.sort()
    slytherin.sort()
    ghosts.sort()
    instructors.sort()

    studentlist.append(dumbledores_army)
    studentlist.append(gryffindor)
    studentlist.append(hufflepuff)
    studentlist.append(ravenclaw)
    studentlist.append(slytherin)
    studentlist.append(ghosts)
    studentlist.append(instructors)

 
  # dumbledores_army = []
    # gryffindor = []
    # hufflepuff = []
    # ravenclaw = []
    # slytherin = []
    # ghosts = []
    # instructors = []



    # TODO: replace this with your code
    # print(studentlist)
    return studentlist


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """
    all_data=[]
    for i in open(filename):
      i = i.rstrip()
      i = i.split('|')
      fn, ln, house, insturctor, cohorts = i
      name = fn+' '+ln
      data = (name, house, insturctor, cohorts)
      all_data.append(data)

    # TODO: replace this with your code

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    # TODO: replace this with your code
    for i in all_data(filename):
      fn_ln, house, insturctor, cohorts = i
      if name == fn_ln:
        return cohorts
   


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    lastname = []
    for i in all_data(filename):
      fn_ln, _, _, _ = i
      full_name = fn_ln.split(' ')
      lastname.append(full_name[-1])
    dup = []
    for i in lastname:
      if lastname.count(i) != 1:
        # print(lastname)
        dup.append(i)    
    dup = set(dup)  

    return dup

    # TODO: replace this with your code


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """
    
    # TODO: replace this with your code
    housemates = set()
    h =None
    c= None
    for data in all_data(filename):
      fn_ln, house, insturctor, cohorts = data
      if name == fn_ln:
        h = house
        c = cohorts
    
    for fn_ln, house, insturctor, cohorts in all_data(filename):
        if house == h and cohorts == c and fn_ln != name:
          housemates.add(fn_ln)
    return housemates
    # housemates = set()

    # target_person = None
    # for person in all_data(filename):
    #     full_name, house, advisor, cohort_name = person

    #     if full_name == name:
    #         target_person = person
    #         break

    # if target_person:
    #     target_name, target_house, _, target_cohort = target_person

    #     for full_name, house, _, cohort_name in all_data(filename):
    #         if ((house, cohort_name) == (target_house, target_cohort) and
    #                 full_name != name):
    #             housemates.add(full_name)

    # return housemates


        



##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
