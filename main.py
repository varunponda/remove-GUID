import re
import os
# Path of directory_name assumed as, D:\Notion-backup\Export-0a317d39-5bf7-4eeb-b160-57e88d9d743d-Part-1\Export-0a317d39-5bf7-4eeb-b160-57e88d9d743d
directory_name = input('input the directory path:')
def remove_guid(path):
    guid_pattern = r' [a-fA-F0-9]{32}$'
    directory, filename = os.path.split(path)
    
    if filename:
        name, ext = os.path.splitext(filename)
        match = re.search(guid_pattern, name)
        if match:
            cleaned_name = name[:match.start()]
            cleaned_filename = cleaned_name + ext
        else:
            cleaned_filename = filename
        return os.path.join(directory, cleaned_filename)
    else:
        match = re.search(guid_pattern, directory)
        if match:
            cleaned_directory = directory[:match.start()]
            return cleaned_directory
        else:
            return directory

 
def guid_removal(directory):
    for item in os.listdir(directory):
      old_path = os.path.join(directory,item)
      path_name = remove_guid(item)
      new_path_name = os.path.join(directory, path_name)
      os.rename(old_path,new_path_name)
      if os.path.isdir(new_path_name) == True:
          guid_removal(new_path_name)
print("process complete")

guid_removal(directory_name)