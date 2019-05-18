import sys
from network import classifier_1d
from utils import pred

def main(args):
	fName = args[1]
	label, prob = pred(fName)
	print(prob)
	print(lower(label))

if __name__ == '__main__':
	main(sys.argv)