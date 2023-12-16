import os, sys, shutil, re, datetime
import constants

class FileSorter:
    def __init__(self, path):
        self.path = path

    def sanitizePath(self):
        if (os.path.isabs(self.path)):
            return self.path
        else:
            return os.path.join(os.getcwd(), self.path)

    def getFolderPath(self, file, path):
        fileExtension = os.path.splitext(file)[1]
        folderPath = os.path.join(path, 'Others')

        for key in constants.DEFAULT_FILE_TYPES:
            if fileExtension in constants.DEFAULT_FILE_TYPES[key]:
                folderPath = os.path.join(path, key)
                break

        if not os.path.exists(folderPath):
            os.makedirs(folderPath)
        
        return folderPath

    def getNameForDuplicate(self, file, folderPath):
        fileName, extension = os.path.splitext(file)
        i = 1

        while os.path.exists(os.path.join(folderPath, fileName + '_' + str(i) + extension)):
            i += 1
        
        return os.path.join(folderPath, fileName + '_' + str(i) + extension)                
        

    def sortDirectory(self):
        sanitizedPath = self.sanitizePath()

        if(os.path.exists(sanitizedPath)):
            for entry in os.listdir(sanitizedPath):
                entryPath = os.path.join(sanitizedPath, entry)

                if os.path.isfile(entryPath):
                    folderPath = self.getFolderPath(entry, sanitizedPath)

                    if (os.path.exists(os.path.join(folderPath, entry))):
                        fileName = self.getNameForDuplicate(entry, folderPath)
                    else:
                        fileName = entry
                    
                    shutil.move(entryPath, os.path.join(folderPath, fileName))
        else:
            print('Path does not exists')
