from importlib import resources

def get_flatland():
	"""Get path to example "Flatland" [1]_ text file.

	Returns
	-------
	pathlib.PosixPath or pathlib.WindowsPath depending on the OS
		path to file.

	References
	----------

	.. [1] E. A. Abbott, "Flatland", Seeley & Co., 1884.
	"""
	with resources.path("pycounts_ks.data", "flatland.txt") as f:
		data_file_path = f
	return data_file_path