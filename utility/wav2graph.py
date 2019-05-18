from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt

color = ['r', 'b']

inputDir = 'data/set_a/'

def plot(data):
	x = data[0]
	y = data[1]
	plt.plot(x, y, 'r')
	plt.show()

def main(filename=inputDir + 'normal__201102081321.wav', mmap=False):
	sampleRate, data = read(filename)
	deltaT = 1/sampleRate
	t = 0
	x = []
	y = []
	for yTemp in data:
		y.append(yTemp)
		x.append(t)
		t = t + deltaT
	plot([x,y])

if __name__ == '__main__':
	main()