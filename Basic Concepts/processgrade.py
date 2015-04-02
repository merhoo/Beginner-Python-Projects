'''
Created on Feb 10, 2012

@author: Ryan Stillings, Meredith Hoo, Kai Kuehner 
'''
import sys

def find_location_in_list(list,index):
    ''''''
    location = -1
    for i in range(len(list)):
        if list[i] == index:
            location = i
            break
    return location
def write_grades_to_file(x_students,x_file,X,student_list,student_averages):
    if len(x_students) > 0:
        x_file = open(X + ".csv", "w")
        for x_student in x_students:
            x_file.write(x_student + "," + str(student_averages[find_location_in_list(student_list,x_student)]))
        x_file.close()
def process_grades(src):
    '''Writes the grade to a file for csv
    Arguments:
    x_students -- list of students
    x_file -- file that contains grade
    x -- grade that student has
    Returns:
    files for each grade containing the students with that grade and their grade
    '''
    student_list = []
    student_averages = []
    try:
        input_file = open(src, "r")
    except IOError as error:
        print("Error: Cannot open '" + src + "' for processing.")
        sys.exit(1)
    a_students = []
    b_students = []
    c_students = []
    d_students = []
    f_students = []
    for line in input_file:
        line = line.split(",")
        student = line[0]
        sum = 0
        num_grades = 0
        for i in range(1, len(line)):
            try:
                sum += int(line[i])
                num_grades += 1
            except:
                pass
        avg = sum // num_grades
        if avg >= 90:
            a_students.append(student)
        elif avg >= 80:
            b_students.append(student)
        elif avg >= 70:
            c_students.append(student)
        elif avg >= 60:
            d_students.append(student)
        else:
            f_students.append(student)
        student_list.append(student)
        student_averages.append(student)
            
    write_grades_to_file(a_students,"a_file","A",student_list,student_averages)
    write_grades_to_file(b_students,"b_file","B",student_list,student_averages)
    write_grades_to_file(c_students,"c_file","C",student_list,student_averages)
    write_grades_to_file(d_students,"d_file","D",student_list,student_averages)
    write_grades_to_file(f_students,"f_file","F",student_list,student_averages)

def main():
    if len(sys.argv) != 2:
        print("Usage: python " + sys.argv[0] + " [input file]")
        sys.exit(1)
    process_grades(sys.argv[1])

if __name__ == "__main__":
    main()