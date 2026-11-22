# news-image-20261121 entry (Python 3.13, standard library only).
# The image beside this file sums up Saturday 21 November 2026's
# world news: Iran's strikes on U.S. bases in Bahrain, the missile
# strike on Kryvyi Rih and Russian weapons landing in Poland,
# Bitcoin's flush to $55,100 and rebound, Mexico's capture of cartel
# boss "Chapo Isidro", and COP31 running into overtime. This program
# copies the image to /output/entry.png; the grader runs it twice and
# both runs must write the same bytes, so the copy is byte-for-byte
# with no timestamps.
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)
