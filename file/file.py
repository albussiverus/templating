#
# file_id = open("/Users/build/Documents/GitHub/templating/file/test.txt",
#                mode='r')
#
# # txt = file_id.read()
#
# for line in file_id:
#     print(line)
#
# # txt = file_id.readline()
# # print(txt)
# file_id.close()
#
# fid = open("file_to_write.txt", mode='w')
# fid.write("This is a text we are going to write")
# fid.close()
#
# fid = open("file_to_write.txt", mode='a')
# seq = ("this is one\n", "o\nr", "two\n")
# fid.writelines(seq)
# fid.close()
#
try:
    fid = open("file_to_write.txt", mode='a')
    seq = ("this is one\n", "o\nr", "two\n")
    fid.writelines(seq)
except:
    pass
finally:
    fid.close()


with open("file_to_write_2.txt", mode='w') as file_id:
    seq = ("this is one", "or", "two")
    file_id.writelines(seq)
