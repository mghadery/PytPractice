filename = input("File name:").strip().lower()
pointIndex = filename.rfind(".")
ext = filename[pointIndex + 1:] if pointIndex != -1 else ""

match ext:
    case "gif":
        mtype="image/gif"
    case "jpg":
        mtype = "image/jpeg"
    case "jpeg":
        mtype = "image/jpeg"
    case "png":
        mtype = "image/png"
    case "pdf":
        mtype = "application/pdf"
    case "txt":
        mtype="text/plain"
    case "zip":
        mtype="application/zip"
    case _:
        mtype="application/octet-stream"

print(mtype)

