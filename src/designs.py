import os
import os.path as path
from PIL import Image, ImageDraw
import argparse
import logging
import shutil

Point = tuple[int, int]
Size = tuple[int, int]

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action="store_true", help="Add debug messages")
parser.add_argument(
    "-b",
    "--print-box-bg",
    action="store_true",
    help="Print a yellow rectangle indicating the box size and position",
)
parser.add_argument(
    "-d",
    "--print-design-bg",
    action="store_true",
    help="Print an orange rectangle indicating the design size and position",
)
args = parser.parse_args()

logger = logging.getLogger("designs")
logger.setLevel(logging.DEBUG if args.verbose else logging.INFO)
logger_handler = logging.StreamHandler()
logger_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
logger.addHandler(logger_handler)

BLANK_TSHIRT_FRONT = "static/blank_tshirt_front.png"
BLANK_TSHIRT_BACK = "static/blank_tshirt_back.png"

BOX_POINTS_FRONT = [(232, 200), (647, 800)]
BOX_POINTS_BACK = [(232, 200), (647, 800)]
BOX_POINTS_HEART = [(500, 220), (647, 350)]

blank_tshirt_front = Image.open(BLANK_TSHIRT_FRONT).convert("RGBA")
blank_tshirt_back = Image.open(BLANK_TSHIRT_BACK).convert("RGBA")
logger.info("Successfully loaded blank t-shirt image")


def get_box_origin(box_points: tuple[Point, Point]) -> Point:
    return (box_points[0][0], box_points[0][1])


def get_box_size(box_points: tuple[Point, Point]) -> Size:
    return (box_points[1][0] - box_points[0][0], box_points[1][1] - box_points[0][1])


def get_design_in_box_size(design_size: Size, box_size: Size) -> Size:
    if design_size[1] / design_size[0] >= box_size[1] / box_size[0]:
        return (int(box_size[1] / design_size[1] * design_size[0]), box_size[1])
    return (box_size[0], int(box_size[0] / design_size[0] * design_size[1]))


def get_design_in_box_origin(
    design_in_box_size: Size, box_origin: Point, box_size: Size
) -> Point:
    if design_in_box_size[1] / design_in_box_size[0] >= box_size[1] / box_size[0]:
        return (
            box_origin[0] + (box_size[0] - design_in_box_size[0]) // 2,
            box_origin[1],
        )
    return box_origin


def add_design_to_tshirt(tshirt: Image, design: Image, box_points: tuple[Point, Point]):
    if args.print_box_bg:
        logger.info("Printing box yellow rectangle into tshirt")
        draw = ImageDraw.Draw(tshirt)
        draw.rectangle(box_points, fill="yellow")

    box_origin = get_box_origin(box_points)
    box_size = get_box_size(box_points)
    logger.debug(f"Box origin: { box_origin }")
    logger.debug(f"Box size: { box_size }")

    design_in_box_size = get_design_in_box_size(design.size, box_size)
    logger.debug(f"Design size: { design_in_box_size }")
    design_in_box_origin = get_design_in_box_origin(
        design_in_box_size, box_origin, box_size
    )
    logger.debug(f"Design origin: { design_in_box_origin }")

    if args.print_design_bg:
        logger.info("Printing design orange rectangle into tshirt")
        draw = ImageDraw.Draw(tshirt)
        design_in_box_rb = tuple(
            [x + y for x, y in zip(design_in_box_origin, design_in_box_size)]
        )
        draw.rectangle((design_in_box_origin, design_in_box_rb), fill="orange")

    logger.info("Printing design into tshirt")
    resized_design = design.resize(design_in_box_size)

    tshirt.paste(resized_design, design_in_box_origin, resized_design)


def _create_tshirt_generic(
    src_dir: str,
    design_file: str,
    output_file: str,
    template_tshirt: Image,
    box_points: tuple[Point, Point],
):
    tshirt = template_tshirt.copy()
    design = Image.open(f"{ src_dir }/{ design_file }").convert("RGBA")

    add_design_to_tshirt(tshirt, design, box_points)

    logger.info(f"Saving t-shirt with design to { output_file }")
    tshirt.save(output_file, "PNG")


def create_tshirt_front(src_dir: str, design_file: str, output_file: str) -> None:
    _create_tshirt_generic(
        src_dir, design_file, output_file, blank_tshirt_front, BOX_POINTS_FRONT
    )


def create_tshirt_back(src_dir: str, design_file: str, output_file: str) -> None:
    _create_tshirt_generic(
        src_dir, design_file, output_file, blank_tshirt_back, BOX_POINTS_BACK
    )


def create_tshirt_heart(src_dir: str, design_file: str, output_file: str) -> None:
    _create_tshirt_generic(
        src_dir, design_file, output_file, blank_tshirt_front, BOX_POINTS_HEART
    )


def create_tshirt(src_dir: str, design_file: str, output_file: str) -> None:
    design_basename = path.splitext(design_file)[0]
    splitted_basename = design_basename.rsplit("_", maxsplit=1)

    if len(splitted_basename) == 2:
        _, suffix = splitted_basename
        logger.debug(f"Found suffix {suffix} on design { design_file }")
        if suffix == "back":
            logger.debug(f"Design { design_file } is type BACK")
            create_tshirt_back(src_dir, design_file, output_file)
        elif suffix == "heart":
            logger.debug(f"Design { design_file } is type HEART")
            create_tshirt_heart(src_dir, design_file, output_file)
        else:
            logger.debug(f"Design { design_file } is type FRONT")
            create_tshirt_front(src_dir, design_file, output_file)
    else:
        logger.debug(f"No suffix found on design { design_file }")
        logger.debug(f"Design { design_file } is type FRONT")
        create_tshirt_front(src_dir, design_file, output_file)


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
                f"static/{generacio_dir}/samarretes/{design}",
            )
