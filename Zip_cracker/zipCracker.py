
import zipfile

zipFilePath = rf"{input('Zip folder: ')}"
passFilePath = r"passList.txt"

with zipfile.ZipFile(zipFilePath, "r") as zFile:
    with open(passFilePath, "r") as pFile:

        for line in pFile.readlines():
            try:
                password = bytes(line, encoding='utf-8')
                zFile.extractall(pwd=password)
            
            except:
                pass
