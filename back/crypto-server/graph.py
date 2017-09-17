import matplotlib.pyplot as plt

plt.ion()
fig = plt.figure()
axes = fig.add_subplot(111)
# axes.set_autoscale_on(True)
graph = axes.plot(0, 0)[0]

def updateGraph(X, Y):
	# print(X)
	# print(Y)
	# print(len(X))
	# print(len(Y))
	axes.relim()
	axes.autoscale_view(True,True,True)

	graph.set_xdata(X)
	graph.set_ydata(Y)
	# plt.tight_layout
	# plt.autoscale(enable=True, axis='y')

	plt.draw()

	plt.pause(0.01)