# objlist.txt
# obj_tag_base;obj_type_tmpl
#
# obj_type_tmpl.txt
# every row = tag_tamplate -> tag_attribute;tag_attribute


def load_obj_type_tmpls(obj_type_tmpl_files):
    obj_type_tmpls = {}
    for file in obj_type_tmpl_files:
        obj_type_tmpl = file[:-4]
        with open(file) as f:
            tag_tmpls = [row for row in f.read().splitlines() if row[0] != "#"]
        obj_type_tmpls[obj_type_tmpl] = tag_tmpls
    return obj_type_tmpls

obj_type_tmpls = load_obj_type_tmpls(["objekt1.txt", "objekt2.txt"])

with open("objektlista.txt") as f:
    objlist = f.read().splitlines()
tagdatabase = []
for obj in objlist:
    obj_tag_base, obj_type_tmpl = obj.split(';')
    for tag_tmpl in obj_type_tmpls[obj_type_tmpl]:
        tagdatabase_row = ""
        for tagdatabase_col_nr, tag_attribute in enumerate(tag_tmpl.split(';')):
            if tagdatabase_col_nr == 0:
                tagdatabase_row += f"{obj_tag_base}_{tag_attribute}"
            else:
                tagdatabase_row += f";{tag_attribute}"
        tagdatabase.append(tagdatabase_row)
for a in tagdatabase:
    print(a)


with open('tagdatabase.txt', 'w') as f:
    f.writelines("%s\n" % row for row in tagdatabase)
