__author__ = 'Vlad'
f = 'file.txt'

def open_f(f):
    obj = open(f,'r')
    return(obj.read(), "Name of the file:",obj.name,"Opening mode:", obj.mode)

def write_f(f):
    obj_w = open(f, "w")
    obj_w.write("hello world in the new file\n")
    obj_w.write("and another line\n")
    obj_w.close()
    return(obj_w)


print open_f(f)
# print write_f(f)