import os
max_subjects = 4
week_days = ["Monday", "Tuesday", "Wedenesday", "Thursday", "Friday", "Saturday"]
lecturer_list = ("M. Saoungoumi", "Pr.Yenke", "Dr.Abboubakar", "Dr. Ndam", "M.Dangbe", "M.Kani")
hall_list = ("Salle 9", "Salle 10", "Labo Info")
subject_list = ["Linear Algebra(MAT 221)", "Introduction to CS(INF 113)"]
class_list = [["GBIO1", "ABB2", "IAB2", "GEN"], \
["GIN1", "GIN2", ["GLO", "RIN"]], \
["GIM1", ["GMP2", "GEL2", "GTE2", "MIP2"], ["GMP3", "GEL3", "GTE3", "MIP3"]]]
print("  Welcome to the timetable generator...")
'''week_name = input("Please enter the week : ")
week_list.append(week_name)'''
print("Let us start with Monday : \n")
monday_subjects = []
for i in range(max_subjects):
	subject = input("Please enter the subjects for monday :")
	if subject_list.__contains__(subject):
		monday_subjects.append(subject)
	else:
		print("The subject is not in the list of subjects.")
print("Let us now work on the subjects : ")
for i in range(monday_subjects.__len__()):
	monday_lecturers = []
	lecturer = input("Please enter the lecturer assigned for subject {}".format(monday_subjects.__getitem__(i)))
	if lecturer_list.__contains__(lecturer):
		monday_lecturers.append(lecturer)
	else:
		print("Sorry, the lecturer {} is not recognized.".format(lecturer))

print("{}".format(hall_list.__getitem__(0)))