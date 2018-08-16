backgrounds = open("data/backgrounds.txt","r")

unique_process_dict = {}


for b in backgrounds.readlines():
    process = b.split("/")[1]
    if unique_process_dict.get(process):
        if "ext" in b:
            print "Replacing",unique_process_dict.get(process),"with",b
            unique_process_dict[process] = b
        else:
            print "Neglecting",b
    else: unique_process_dict[process] = b

backgrounds.close()

files = "".join([b for b in unique_process_dict.values()])

with open("datasets.txt","w") as f:
    f.write(files)
    f.close()
