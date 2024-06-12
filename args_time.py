import argparse
import time

parser = argparse.ArgumentParser(description='Data for this program.')
parser.add_argument('--tim', action='store', type=int, default=10,
                    help='time for program to run in seconds')
parser.add_argument('--delay', action='store', type=float, default=0.5,
                    help='time in between messages')
parser.add_argument('--debug', action='store_true', 
                    help='specifies if debug statements are printed')
args = parser.parse_args()

if args.debug:
   print (f'arguments: {vars(args)}')

start_time = time.time()
cur_time   = start_time
mesg_time  = start_time

while (start_time + args.tim > cur_time):
   time.sleep(0.0001)         # some short delay to avoid busy waits
   cur_time = time.time()
   if (mesg_time + args.delay < cur_time):
      mesg_time = cur_time
      print (f'time: {cur_time - start_time:0.2f}')

