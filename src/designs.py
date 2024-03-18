import os
import os.path as path
from PIL import Image, ImageDraw
import shutil

BLANK_TSHIRT = "static/blank_tshirt.png"
DESIGN_POINTS = [(190, 100), (410, 400)]


blank_tshirt = Image.open(BLANK_TSHIRT).convert("RGBA")

def create_tshirt(design: str, output_file: str) -> None:
	tshirt = blank_tshirt.copy()
	draw = ImageDraw.Draw(tshirt)
	draw.rectangle(DESIGN_POINTS, fill="black")

	tshirt.save(output_file, "PNG")

for static_item in os.listdir("static/"):
	if path.isdir(f"static/{static_item}") and static_item.startswith("festes"):

		os.makedirs(f"static/{static_item}/samarretes", exist_ok=True)

		for design in os.listdir(f"static/{static_item}/dissenys"):
			create_tshirt(
				f"static/{static_item}/dissenys/{design}",
				f"static/{static_item}/samarretes/{design}"
			)
