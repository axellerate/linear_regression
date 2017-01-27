from matplotlib import pyplot as plt

# maps height in cm to weight in kg
dataset = [ [150,45],
			[155,52],
			[160,55],
			[165,61],
			[170,65],
			[175,71],
			[180,77],
			[185,83],
			[190,91],
			[195,103] ]

x_values = [i[0] for i in dataset]
y_values = [i[1] for i in dataset]

# if you want to graph the points
# plt.plot(x_values, y_values, 'bo')
# plt.show()

#initialize theta_0 and theta_1 to 0.0
theta_0 = 0.0
theta_1 = 0.0
# this is alpha
learn_rate = 0.001

# hypothesis function
h = lambda x : theta_0 + (theta_1 * x)

# core of the linear regression algorithm
def summation(h, dataset):

	total_1 = 0
	total_2 = 0
	m = len(dataset)

	# update the totals simultaneously
	for i in dataset:
		total_1 += h(i[0]) - i[1]
		total_2 += (h(i[0]) - i[1]) * i[1]
	# return the totals
	return total_1 * (1.0/m), total_2 * (1.0/m)

# update theta_0 and theta_1
for i in range(100):
	sum1,sum2 = summation(h, dataset)
	# updates happen
	theta_0 = theta_0 - learn_rate * sum2
	theta_1 = theta_1 - learn_rate * sum1

# print theta_0
# print theta_1
# print h(170)