from platform import python_version


def write_text(filename,filetext:str):
    filename.write(filetext)
    filename.write(python_version())
    filename.close()



with open("test.txt","w") as f:
    write_text(f,"more intelegent")