with open("objektlista_exc.txt") as f:
    objlist = [row for row in f.read().splitlines() if row[0] != "#"]
    exceptions = {}
    new_objlist = []
    for row_nr, row in enumerate(objlist):
        if row[0] == '|':
            found = False
            i = 1
            while not found:
                lockup_id = row_nr - i
                objname = objlist[lockup_id].split(";")
                if objname[0] != '|':
                    found = True
                exceptions[objname] = []
                exceptions[objname].append(row[1:])
                i -= 1
        else:
            new_objlist.append(row)


print(new_objlist)
print(exceptions)

# tagdatabase = []
# for obj in objlist:
#     obj_tag_base, obj_type_tmpl = obj.split(';')
#     for tag_tmpl in obj_type_tmpls[obj_type_tmpl]:
#         tagdatabase_row = ""
#         for tagdatabase_col_nr, tag_attribute in enumerate(tag_tmpl.split(';')):
#             if tagdatabase_col_nr == 0:
#                 tagdatabase_row += f"{obj_tag_base}_{tag_attribute}"
#             else:
#                 tagdatabase_row += f";{tag_attribute}"
#         tagdatabase.append(tagdatabase_row)
# for a in tagdatabase:
#     print(a)
#
#
# with open('tagdatabase.txt', 'w') as f:
#     f.writelines("%s\n" % row for row in tagdatabase)
