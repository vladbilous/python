import os
import shutil

os.mkdir("folder_zip")

for filename in range(3):
    f = open("folder_zip/file_%s" % filename, "w")
    f.write('some data')
    f.close()

shutil.make_archive("my_zip", "zip", root_dir=".",
                    base_dir="./folder_zip")
shutil.copy("my_zip.zip", "../my_zip.zip")
shutil.rmtree("folder_zip")
input()
shutil.unpack_archive("../my_zip.zip")
os.remove("my_zip.zip")
os.remove("../my_zip.zip")
print(shutil.disk_usage("."))
