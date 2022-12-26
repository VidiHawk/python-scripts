### Next steps
- in <code>web-image-processing.py</code>, replace <code>OS</code> in functions by <code>Path</code>


# Data Processing Tools

This is intended to grow into a library of useful data processing tools scripted in Python.

# Index

## Image processing

- [Resize image batches](web_image_processor.py)
  This collection of functions may come handy when preparing imagery for new website. You can process  backgrounds, thumbails, icons, etc. in a variety of formats such as jpg, png, svg, webp, ico.
- [Extract metadata from large image batches](image_metadata.py)

## General file processing

- [Batch renaming](rename.py)

## Map data processing

- [Convert json data to geojson](json_to_geojson.py)
- [Get addresses from coordinates](reverse_geocoding.py)

# Prerequisites

- [python 3](https://www.python.org/downloads/)
- [pip3](https://pip.pypa.io/en/stable/)

## Requirements

- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
  
You'll know you did it right if you can run `git --version` and you see a response like `git version x.x.x`

## Setup

Clone this repo

`git clone https://github.com/VidiHawk/python-scripts`

`cd <your project's file>`

Then install dependencies

`pip install -r requirements.txt`

# Adding your own tools

If you want to add packages to the requirement.txt file, I recommand using the pipreqs package. To install it:

`pip install pipreqs`

To build automatically your requirements.txt, just run the following command in the project directory:

`pipreqs . --force`

The --force flag will overwrite the existing requirements.txt file.

## Notes

These scripts have been created and tested on the Ubuntu 20.04.4 LTS operating system and Python 3.8.10

# Acknoledgements

- [youtube_dl](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#readme)
- [yt_dlt](https://github.com/yt-dlp/yt-dlp/blob/master/README.md)
- [ffmpeg](https://ffmpeg.org/)
