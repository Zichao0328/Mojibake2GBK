import os

class Renamer(object):

    def __init__(self, root_path):
        self.root_path = root_path

    def rename_files(self, path):
        file_abs_path = []
        '''
        自底向上遍历，防止更改父文件夹名后找不到子文件夹/子文件
        '''
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files + dirs:
                old_path = os.path.join(root, name)
                file_abs_path.append(old_path)
        '''
        修改文件名
        '''
        for abs_path in file_abs_path:
            old_path, old_name = os.path.split(abs_path)
            new_name = old_name.encode('gbk').decode('shift_jis')
            os.rename(abs_path, os.path.join(old_path, new_name))
        return file_abs_path
