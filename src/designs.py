import os
import os.path as path
import shutil

for static_item in os.listdir("static/"):
	if path.isdir(f"static/{static_item}") and static_item.startswith("festes"):

		os.makedirs(f"static/{static_item}/samarretes", exist_ok=True)

		for design in os.listdir(f"static/{static_item}/dissenys"):
			shutil.copyfile(
				f"static/{static_item}/dissenys/{design}",
				f"static/{static_item}/samarretes/{design}"
			)
