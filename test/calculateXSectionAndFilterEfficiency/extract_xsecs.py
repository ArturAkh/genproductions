import sys
import glob
import os
import json
import argparse


parser = argparse.ArgumentParser(description='Script to extract cross-section values from logs of GenXSecAnalyzer.')
parser.add_argument('--folder',type=str,default=None,
                    help='Folder path to the GenXSecAnalyzer logs')

args = parser.parse_args()

if args.folder is None:
	print "please privide the folder with logs"
	exit(1)

logs = glob.glob(os.path.join(args.folder,"*.log"))

output_file = open(os.path.join(args.folder,"generator_xsecs.json"), "w")
xsec_dict = {}

for log in logs:
	dataset_name = os.path.basename(log).replace(".log","").replace("xsec_","")
	for l in open(log,"r").readlines():
		if "After filter: final cross section" in l:
			print dataset_name, float(l.strip().split()[6])
			xsec_dict[dataset_name] = float(l.strip().split()[6])
output_file.write(json.dumps(xsec_dict, sort_keys=True, indent=2))
