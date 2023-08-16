import numpy as np
import matplotlib.pyplot as plt


# creating the dataset
data = {'C':['20','24'], 'C++':['15','23'], 'Java':['30','29'],
		'Python':['35','23']}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(courses, values, color ='maroon',
		width = 0.4)

plt.xlabel("Courses offered")
plt.ylabel("No. of students enrolled")
plt.title("Students enrolled in different courses")
plt.show()
