import requests, argparse, zipfile, os

class ChromeExtensionDownloader():

    def __init__(self):
        
        self.base_url = "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=${version}&acceptformat=crx2,crx3&x=id%3D${result[1]}%26uc&nacl_arch=${nacl_arch}"
        self.chrome_version = "103.0.5060.134"
        self.nacl_arch = "x86_64"

        self.extension_id = ''
        self.extension_name = ''

        parser = argparse.ArgumentParser(description='Chrome Extension Downloader')
        parser.add_argument('-u', '--url', help='URL of the extension page')
        parser.add_argument('-i', '--id', help='Extension ID')
        parser.add_argument('-v', '--version', help='Chrome Version : Specify chrome version', default="103.0.5060.134")
        parser.add_argument('-a', '--arch', help='NACL arch, x86_64 or arm', default="x86_64")
        parser.add_argument('-o', '--output_path', help='Output Path', default="")
        parser.add_argument('-x', '--extract', help='Extract the extension or not : 0 - No : Rest : Yes', default='0')

        args = parser.parse_args()
        
        if args.url:
            url_parts = args.url.split('/')
            self.extension_name, self.extension_id = url_parts[url_parts.index('detail') + 1] , url_parts[url_parts.index('detail') + 2]
            self.download_extension(self.extension_id)
        elif args.id:
            self.download_extension(args.id)
        else:
            print('No URL or ID specified')
            return None
        
        if args.extract != '0':
            self.extract_extension(self.extension_name, args.output_path)


    def download_extension(self, extension_id):
        self.extension_id = extension_id

        if self.extension_name == '':
            self.extension_name = self.extension_id
        
        extension_download_url = self.base_url.replace("${version}", self.chrome_version).replace("${nacl_arch}", self.nacl_arch).replace("${result[1]}", self.extension_id)
        print('Downloading extension from: ' + extension_download_url)
        try:
            response = requests.get(extension_download_url, timeout=10)
        except Exception as e:
            print(f'Error downloading extension: {e}')
            return None
        if response.status_code == 200:
            # save to file
            with open(f'{self.extension_name}.crx', 'wb') as f:
                f.write(response.content)
            print(f'Extension {self.extension_name} downloaded successfully')
            return True
        else:
            print('Extension download failed')
            return None

    def download_from_url(self, extension_page_url):
        url_parts = extension_page_url.split('/')
        self.extension_name, self.extension_id = url_parts[url_parts.index('detail') + 1] , url_parts[url_parts.index('detail') + 2]
        print(f'Downloading extension {self.extension_name} with id {self.extension_id}')
        self.download_extension(self.extension_id)

    def extract_extension(self, extension_file_path, output_path):
        print(f'Extracting extension {extension_file_path.split("/")[-1]} to {output_path}')
        extension_name = extension_file_path.split("/")[-1].split(".")[0]
        full_extraction_path = os.path.join(output_path, extension_name)
        with zipfile.ZipFile(extension_file_path, 'r') as zip_ref:
            zip_ref.extractall(full_extraction_path)
        return full_extraction_path

if __name__ == '__main__':
    ChromeExtensionDownloader()