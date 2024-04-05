import os
import os.path as path
from PIL import Image, ImageDraw
import shutil

BLANK_TSHIRT = "static/blank_tshirt.png"
BOX_POINTS = [(190, 100), (410, 400)]

box_origin = (BOX_POINTS[0][0], BOX_POINTS[0][1])
box_size = (BOX_POINTS[1][0]-BOX_POINTS[0][0], BOX_POINTS[1][1]-BOX_POINTS[0][1])
blank_tshirt = Image.open(BLANK_TSHIRT).convert("RGBA")

def get_design_size(design_size: tuple[int, int], box_size: tuple[int, int]) -> tuple[int, int]:
	if design_size[1]/design_size[0] >= box_size[1]/box_size[0]:
		return (int(box_size[1]/design_size[1]*design_size[0]), box_size[1])
	return (box_size[0], int(box_size[0]/design_size[0]*design_size[1]))

def create_tshirt(design: str, output_file: str) -> None:
	tshirt = blank_tshirt.copy()
	design = Image.open(design).convert("RGBA")
	resized_design = design.resize(get_design_size(design.size, box_size))

	tshirt.paste(resized_design, box_origin, resized_design)

	tshirt.save(output_file, "PNG")

for static_item in os.listdir("static/"):
	if path.isdir(f"static/{static_item}") and static_item.startswith("festes"):

		os.makedirs(f"static/{static_item}/samarretes", exist_ok=True)

		for design in os.listdir(f"static/{static_item}/dissenys"):
			create_tshirt(
				f"static/{static_item}/dissenys/{design}",
				f"static/{static_item}/samarretes/{design}"
			)
