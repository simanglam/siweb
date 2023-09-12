#!/usr/bin/python3
import re
import os, sys
root_chunk = []
chunks = {}
current_chunk = None
file_name = None
output_chunk = None
def expand(chunk_name, indent):
	result = []
	try:
		output_chunk = chunks[chunk_name]
	except KeyError:
		print(f"KeyError {chunk_name} undefined")
		return []
	for i in output_chunk:
		match = re.match(r"(\s*)<<([^>]+)>>\s*$", i)
		if match:
			result.extend(expand(match.group(2), indent + match.group(1)))
		else:
			result.append(indent + i)
	return result

for i in sys.argv[1:]:
	if i.startswith("--"):
		i = i.strip("--")
		if i == "help":
			print("This is a Literate Programming tool made by Si Manglam to satisfy his own requirement.\nUsage: sitangle output_chunk_name file")
			exit(0)
		else:
			print("Unknown Option")
			exit(1)
	else:
		if output_chunk and file_name:
			print("Error, More than two argument")
			exit(1)
		elif output_chunk:
			file_name = i
		else:
			output_chunk = i
with open(file_name, "r") as f:
	for line in f:
		match = re.match(r"<<([^>]+)>>=", line)
		if match:
			current_chunk = match.group(1)
			if not current_chunk in chunks:
				chunks[current_chunk] = []
			if re.match(r"\S*\.\S+", current_chunk):
				if not current_chunk in root_chunk:
					root_chunk.append(current_chunk)
		else:
			if current_chunk:
				match = re.match(r"@[^\S]", line)
				if match:
					current_chunk = None
				else:
					chunks[current_chunk].append(line)
if output_chunk == "all":
	for name in root_chunk:
		os.system(f"touch {name}")
		with open(name, "w+") as f:
			for line in expand(name, ""):
				f.write(line)
else:
	with open(output_chunk, "w+") as f:
		for line in expand(output_chunk, ""):
			f.write(line)
