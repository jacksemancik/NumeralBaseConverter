import argparse
from views import convert

#This programme runs using the following shell command: `python conv.py N --base BASE` Works up to base-61.
#Letters represent numbers incrementally. For example, a = 10, b = 11, c = 12, etc. A = 36

parser = argparse.ArgumentParser()
parser.add_argument("number_to_convert", metavar="N", type=str, nargs=1, help="the base-n number to be converted to base-10")
parser.add_argument("--base","-b",type=str,nargs=1,default=(10,),help="the base of the number to be converted; the default base is ten")
args = vars(parser.parse_args())
other_num = ''
for each in args['number_to_convert']:
	other_num += str(each)
system = 0
for each in args['base']:
	system += int(each)
if(10 > system):
	other_num = int(other_num)
else:
	pass

convert(system,other_num)

