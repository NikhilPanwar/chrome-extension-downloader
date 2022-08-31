# Chrome Extension Dowloader
A while ago, I needed to download few thousand chrome extensions for a personal project.
So i wrote this.

Not 100% sure if it works anymore, but it should.


### Usage
```
usage: chrome_extension_downloader.py [-h] [-u URL] [-i ID] [-v VERSION] [-a ARCH] [-o OUTPUT_PATH] [-x EXTRACT]

Chrome Extension Downloader

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL of the extension page
  -i ID, --id ID        Extension ID
  -v VERSION, --version VERSION
                        Chrome Version : Specify chrome version
  -a ARCH, --arch ARCH  NACL arch, x86_64 or arm
  -o OUTPUT_PATH, --output_path OUTPUT_PATH
                        Output Path
  -x EXTRACT, --extract EXTRACT
                        Extract the extension or not : 0 - No : Rest : Yes
```