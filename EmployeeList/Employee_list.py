class Employee:
    """This is a class that holds data for employees"""

    def __init__(self, name='', eid=''):
        """Initializes employee class with a name and an employee id"""
        self.__name = name
        self.__eid = eid


    @property
    def name(self):
        return self.__name.capitalize()

    @name.setter
    def name(self, new_name):
        # checks to see if the name entered is alpha, otherwise it
        # defaults to 'Unknown'
        if new_name.isalpha():
            self.__name = new_name
        else:
            self.__name = 'Unknown'

    @property
    def eid(self):
        # fills the employee number with zeroes before returning
        return self.__eid.zfill(4)

    @eid.setter
    def eid(self, new_eid):
        # checks if entry is blank and defualts eid to '9999'
        if len(new_eid) == 0:
            self.__eid = '9999'
        else:
            self.__eid = new_eid

    def __str__(self):
        return f'{self.eid}: {self.name}'


class Manager(Employee):
    """A subclass of employee which stores data for managers"""

    def __init__(self, name='', eid=''):
        """Initializes a new instance of the manager subclass and borrows fields from the employee class"""
        super().__init__(name, eid)
        self.__subordinates = []
        self.__count = 0

    def add_subordinate(self):
        """creates an employee class and adds it to the list of subordinates for an instance of the manager subclass"""
        name = input('Enter subordinate name: ')
        eid = input('Enter subordinate id: ')
        subordinate = Employee()
        # adding these fields outside of the initializer allows the setter fields to change improper inputs
        subordinate.name = name
        subordinate.eid = eid
        self.__subordinates.append(subordinate)

    def print_subordinates(self):
        """Prints list of subordinates for an instance of a manager class"""
        print(f"\t{self.name}'s Employees")
        for s in self.__subordinates:
            print(f'\t{s}')


def main():
    """Main program logic"""
    employees = []
    entry = ''
    print(f'{"Employee Management System": ^50}')
    print('\nAdding Employees...')

    # While loop will run at least once and allow the user to stop entering data after
    while entry != 'N':
        print()
        new_employee = add_employee()
        employees.append(new_employee)
        entry = input('Do you want to enter more (Y/N)? ').upper()

    print('\nPrinting Employee List')
    # after all data is entered, prints a list of all employees/managers added
    for e in employees:
        print(e)
        # checks if the class is a manager, and then prints subordinate list for that manager if true
        if isinstance(e, Manager):
            e.print_subordinates()


def add_employee():
    """Adds a new instance of the employee or manager class"""
    name = input('Enter name: ')
    eid = input('Enter id: ')
    is_manager = input('Is the employee a manager (Y/N) ').upper()

    if is_manager == 'Y':
        new_employee = Manager()
        # adding these fields outside of the initializer allows the setter fields to change improper inputs
        new_employee.name = name
        new_employee.eid = eid
        sub_count = int(input('How many subordinates? '))
        while sub_count > 0:
            new_employee.add_subordinate()
            sub_count -= 1
    else:
        new_employee = Employee()
        # adding these fields outside of the initializer allows the setter fields to change improper inputs
        new_employee.name = name
        new_employee.eid = eid
    return new_employee


if __name__ == "__main__":
    # call and execute the main function
    main()
