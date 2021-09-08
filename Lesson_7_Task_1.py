import os

root = os.path.dirname('GB_HT')
project_name = 'le_projecto'
paths = [os.path.join(project_name, 'settings'), os.path.join(project_name, 'mainapp'), os.path.join(project_name, 'adminapp'), os.path.join(project_name, 'authapp')]
for _path in paths:
    os.makedirs(os.path.join(root, _path), exist_ok=True)