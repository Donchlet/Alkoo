import wget

imageur = 'https://www.instagram.com/p/CGNMx50na3O/'


def download(url=''):
    wget.download(url=url)

def main():
    download(url=imageur)

if __name__ == '__main__':
    main()















