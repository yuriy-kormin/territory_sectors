from conf import drive,folder_id

file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
