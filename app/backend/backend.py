import sys
from network import classifier_1d
from utils import pred

def main(args):
	fName = args[1]
	label, prob = pred(fName)
	# print(fName)
	print(prob)
	print(label.lower())

if __name__ == '__main__':
	main(sys.argv)
