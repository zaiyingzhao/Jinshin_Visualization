import glob 
dir_path = "../data/**/*.geojson"
geojson = glob.glob(dir_path,recursive=True)
print("[" , end= " ")
for file in geojson:
    print(f'"{file}"', ",", end=" ")
print("]", end = " ")