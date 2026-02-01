import sys
import PIL
import PIL.ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    valid_exts = ["jpeg", "jpg", "png"]
    before_file_name = sys.argv[1]
    before_file_ext = get_extension(sys.argv[1])
    after_file_name = sys.argv[2]
    after_file_ext = get_extension(sys.argv[2])

    if before_file_ext not in valid_exts:
        sys.exit("Invalid input")

    if after_file_ext not in valid_exts:
        sys.exit("Invalid output")

    if before_file_ext != after_file_ext:
        sys.exit("Input and output have different extensions")

    try:
        with PIL.Image.open(before_file_name) as im, PIL.Image.open("shirt.png") as shirt:
            #width, height =
            im = PIL.ImageOps.fit(im, size=shirt.size)
            im.paste(shirt, shirt)
            im.save(fp=after_file_name)
    except FileNotFoundError:
        sys.exit("Input does not exist")

def get_extension(file_name: str):
    point_ind = file_name.rfind(".")
    if point_ind == 1:
        return None
    return file_name[point_ind + 1:].lower()


if __name__ == "__main__":
    main()
