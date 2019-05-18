from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt
import glob
import time

maxTime = 10

inputDir = '/home/psg/data/set_a/'
outputDir = 'graph/'

def plot(data, fname):
	x = data[0]
	y = data[1]
	plt.figure(figsize=(16, 9))
	plt.axis('off')
	plt.plot(x, y, 'b')
	plt.savefig(outputDir + fname + '.jpeg')
	plt.close()

def w2g(filename, mmap=False):
	sampleRate, data = read(filename, mmap = mmap)
	deltaT = 1/sampleRate
	t = 0
	plots = 0
	x = []
	y = []
	for yTemp in data:
		y.append(yTemp)
		x.append(t)
		t = t + deltaT
		if(t >= 0.1):
			t = 0
			plot([x,y], filename.split('/')[-1].split('.')[0] + '.' + str(plots))
			plots = plots + 1
			x = []
			y = []

	x = []
	y = []
	while(plots < 10*maxTime):
		plot([x,y], filename.split('/')[-1].split('.')[0] + '.' + str(plots))
		plots = plots + 1

def main():
	os.popen('rm ' + outputDir + '*')
	filename = glob.glob(inputDir + "*")
	i = 0
	for fname in filename:
		w2g(fname)
		print(i)
		i = i + 1

if __name__ == '__main__':
	main()
