from PIL import Image
from PIL.ExifTags import TAGS
import exifread as ef

# Now this will only work on JPEG image files

# path to the image or video
imagename = "image.jpg"

# read the image data using PIL
image = Image.open(imagename)

# extract other basic metadata
info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1),
}

for label, value in info_dict.items():
    print(f"{label:25}: {value}")

# extract EXIF data
exifdata = image.getexif()

# iterating over all EXIF data fields
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")


def _convert_to_degress(value):
    """
    Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
    :param value:
    :type value: exifread.utils.Ratio
    :rtype: float
    """
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)


def getGPS(imagename):
    """
    returns gps data if present other wise returns empty dictionary
    """
    with open(imagename, "rb") as f:
        tags = ef.process_file(f)
        latitude = tags.get("GPS GPSLatitude")
        latitude_ref = tags.get("GPS GPSLatitudeRef")
        longitude = tags.get("GPS GPSLongitude")
        longitude_ref = tags.get("GPS GPSLongitudeRef")
        if latitude:
            lat_value = _convert_to_degress(latitude)
            if latitude_ref.values != "N":
                lat_value = -lat_value
        else:
            return {}
        if longitude:
            lon_value = _convert_to_degress(longitude)
            if longitude_ref.values != "E":
                lon_value = -lon_value
        else:
            return {}
        return {"latitude": lat_value, "longitude": lon_value}
    return {}


gps = getGPS(imagename)
print(gps)
