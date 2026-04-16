import os
import shutil

# 1、 os.mkdir(path)：创建目录，如果目录存在抛出异常
try:
    os.mkdir('./test')
except FileExistsError:
    pass

# 2、os.makedirs(path)：创建多级目录（如果路径中的所有目录都存在，会抛出异常）
try:
    os.makedirs('./test/aa')
except FileExistsError:
    pass

# 3、os.rmdir(path)：删除空目录
# os.rmdir('./test/aa')

# 4、os.removedirs(path)：递归删除空目录，在成功删除末尾一级目录后，会继续尝试删除上一层目录，直到非空目录
# os.removedirs('./test/aa')

# 5、os.path.exists(path)：判断路径是否存在（文件和目录都算）
result = os.path.exists('./test/aa/c')
print(result)

# 6、os.path.isdir(path)：判断路径是否存在（不存在或者是文件返回False，存在返回True）

# 7、os.path.isfile(path)：判断是否是文件

# 8、os.scandir(path)：扫描指定目录， 返回迭代器

# 9、os.walk(path)：安层级，递归遍历指定目录下，所有子目录和文件，返回生成器
# 返回生成器是按层级目录存储('path', [目录文件夹], [文件])

# 10、shutil.rmtree(path)：删除有内容的目录