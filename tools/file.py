import os

def get_file_names(path, show_files = 0):
    print(f"Get all file names in {path}")
    files_names = os.listdir(path)
    if '.DS_Store' in files_names:
        files_names.remove('.DS_Store')
    
    if show_files:
        print(files_names)
    return files_names

# path = '/Users/junnnn/Desktop/NUS/Github/File_management'
# file_names = get_file_names(path)
