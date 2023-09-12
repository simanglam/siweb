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

