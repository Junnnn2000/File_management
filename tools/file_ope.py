import os

def get_file_names(path, show_files = 0):
    files_names = os.listdir(path)
    if '.DS_Store' in files_names:
        files_names.remove('.DS_Store')
    if show_files:
        print(f"Get all file names in {path}")
        print(files_names)

    return files_names


def get_file_paths(root, show_paths = 0):
    file_names = get_file_names(root)
    file_paths = []
    for file_name in file_names:
        file_paths.append(os.path.join(root, file_name))
    if show_paths:
        print(f"Get all paths names in {root}")
        print(file_paths)
        
    return file_paths


# path = '/Users/junnnn/Desktop/NUS/Github/File_management'
# # file_names = get_file_names(path)
# file_paths = get_file_paths(path, show_paths=1)
