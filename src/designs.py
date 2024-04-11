import os
import os.path as path
from PIL import Image, ImageDraw
import argparse
import logging
import shutil

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action='store_false', help="Add debug messages")
args = parser.parse_args()

logger = logging.getLogger("designs")
logger.setLevel(logging.INFO if args.verbose else logging.DEBUG)
logger_handler = logging.StreamHandler()
logger_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logger.addHandler(logger_handler)

BLANK_TSHIRT = "static/blank_tshirt.png"
BOX_POINTS = [(190, 120), (410, 420)]


box_origin = (BOX_POINTS[0][0], BOX_POINTS[0][1])
box_size = (BOX_POINTS[1][0]-BOX_POINTS[0][0], BOX_POINTS[1][1]-BOX_POINTS[0][1])
logger.debug(f"Box origin: { box_origin }")
logger.debug(f"Box size: { box_size }")

blank_tshirt = Image.open(BLANK_TSHIRT).convert("RGBA")
logger.info("Successfully loaded blank t-shirt image")

def get_design_in_box_size(design_size: tuple[int, int], box_size: tuple[int, int]) -> tuple[int, int]:
	if design_size[1]/design_size[0] >= box_size[1]/box_size[0]:
		return (int(box_size[1]/design_size[1]*design_size[0]), box_size[1])
	return (box_size[0], int(box_size[0]/design_size[0]*design_size[1]))

def get_design_in_box_origin(design_in_box_size: tuple[int, int], box_size: tuple[int, int]) -> tuple[int, int]:
	if design_in_box_size[1]/design_in_box_size[0] >= box_size[1]/box_size[0]:
		return (box_origin[0] + (box_size[0]-design_in_box_size[0])//2, box_origin[1])
	return box_origin

def create_tshirt(src_dir: str, design_file: str, output_file: str) -> None:
	tshirt = blank_tshirt.copy()
	design = Image.open(f"{ src_dir }/{ design_file }").convert("RGBA")

	design_in_box_size = get_design_in_box_size(design.size, box_size)
	logger.debug(f"Design size for { design_file }: { design_in_box_size }")
	design_in_box_origin = get_design_in_box_origin(design_in_box_size, box_size)
	logger.debug(f"Design origin for { design_file }: { design_in_box_origin }")

	resized_design = design.resize(design_in_box_size)

	tshirt.paste(resized_design, design_in_box_origin, resized_design)

	logger.info(f"Saving t-shirt with design to { output_file }")
	tshirt.save(output_file, "PNG")

logger.info("Scanning generacions in 'dissenys/'")
for generacio_dir in os.listdir("dissenys/"):

	logger.info(f"Checking if { generacio_dir } is generació")
	if path.isdir(f"dissenys/{generacio_dir}") and generacio_dir.startswith("festes"):
		logger.info(f"Found generació in { generacio_dir }")

		logger.info(f"Creating camisetes directory for generacio { generacio_dir }")
		os.makedirs(f"static/{generacio_dir}/samarretes", exist_ok=True)

		logger.info(f"Scanning dissenys for generació { generacio_dir }")
		for design in os.listdir(f"dissenys/{generacio_dir}"):

			logger.info(f"Creating t-shirt out of design { design }")
			create_tshirt(
				f"dissenys/{generacio_dir}",
				f"{design}",
				f"static/{generacio_dir}/samarretes/{design}"
			)
