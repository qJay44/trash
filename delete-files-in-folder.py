import os

dirs = 'C:\\Users\\gerku\\Desktop\\firearms'
dirsPath = [os.path.join(dirs, name) for name in os.listdir(dirs)]

removeCount = 0
for folder in dirsPath:
    for file in os.listdir(folder):
        if not ('fire' in file and not 'dryfire' in file):
            os.remove(os.path.join(folder, file))
            removeCount += 1

print(f'removed {removeCount} files')

