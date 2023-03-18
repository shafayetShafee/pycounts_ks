# read version from installed package
from importlib.metadata import version
__version__ = version("pycounts_ks")

# populate package namespace
from pycounts_ks.pycounts_ks import count_words
from pycounts_ks.plotting import plot_words