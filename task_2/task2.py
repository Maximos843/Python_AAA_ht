from typing import Union, Dict, Any


def menu():
    """Calling the menu to perform operations from the user."""
    print('Please, enter file name:')
    data = []
    while data == []:
        try:
            name = input()
            with open(name, 'r') as file:
                data = [line.rstrip().split(';') for line in file]
        except IOError:
            print('Please, enter correct file name:')
    print(
        '\nPlease, enter menu option:\n'
        '1 - Print hierarchy of teams in departments.\n'
        '2 - Print summary report by departments.\n'
        '3 - Save summary report by departments.'
    )
    option = int(input())
    while option not in [1, 2, 3]:
        print('Please, enter correct menu option.')
        option = int(input())
    if option == 1:
        print_hierarchy(data)
    elif option == 2:
        summary_report(data)
    else:
        print('Please, input a file name to write departments statistics.')
        name = input()
        write_report(data, name)


def print_hierarchy(data: list[list[str]]):
    """
    Print the hierarchy of teams in departments.

    Args:
        data (list[list[str]]): file content.
    """
    departments_teams: Dict[str, list[str]]
    departments_teams = {data[i][1]: [] for i in range(1, len(data))}
    unique = []
    for i in data[1:]:
        if i[2] not in unique:
            unique.append(i[2])
            departments_teams[i[1]].append(i[2])
    print('\nPrinting hierarchy:\n')
    for key, value in departments_teams.items():
        value = sorted(value)
        print(key)
        print('-\t' + '\n-\t'.join(value))


def summary_report(data: list[list[str]],
                   save: bool = False) -> Union[list[tuple[str]], list]:
    """
    Create summary report for each department.

    Args:
        data (list[list[str]]): file content.
        save (bool): the need to save to a file.

    Returns:
        list[list[int]]: summary report for each department.
        None: if there is no need to write to a file.
    """
    departments: Dict[str, list[Any]]
    departments = {data[i][1]: [10e8, 0, 0, []] for i in range(1, len(data))}
    departments_statistics = []
    for i in data[1:]:
        departments[i[1]][0] = min(departments[i[1]][0], int(i[-1]))
        departments[i[1]][1] = max(departments[i[1]][1], int(i[-1]))
        departments[i[1]][3].append(int(i[-1]))
        departments[i[1]][2] += 1
    for key, value in departments.items():
        n = value[2]
        median = ''
        value[3] = sorted(value[3])
        if n % 2 == 0:
            median = str(int((value[3][n // 2] + value[3][n // 2 - 1]) / 2))
        else:
            median = str(value[3][n // 2])
        if save is False:
            print('Department:', key)
            print('\tCount employers:', n)
            print('\tSalary fork:', value[0], '-', value[1])
            print('\tMean salary:', int(sum(value[3]) / n))
            print('\tMeadian salary:', median)
        else:
            departments_statistics.append([key, str(n), str(value[0]) + ' - ' + str(value[1]),
                                           str(int(sum(value[3]) / n)), median])
    if save:
        return departments_statistics
    return []


def write_report(data: list[list[str]], name: str):
    """
    Write in file summary report for each department

    Arguments:
        data (list[list[int]]): file content.
        name (str): name of the file to record the report.
    """
    departments_statistics = summary_report(data, save=True)
    with open(name, 'w') as file:
        file.write(';'.join(['Deratment', 'Count', 'Salary fork',
                             'Mean salary', 'Median salary']) + '\n')
        for i in departments_statistics:
            file.write(';'.join([j for j in i]) + '\n')


if __name__ == '__main__':
    menu()
