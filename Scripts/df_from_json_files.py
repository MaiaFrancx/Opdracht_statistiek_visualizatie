# # Functie die DataFrame "df" creëert vanuit .json files die zich in een folder "directory" bevinden

# def df_from_json_files (directory) :
    
#     data_list = []

#     for file in os.listdir(directory) :
#         with open(file) as file:
#             data = json.loads(file.read())
#         data_list.append(data)

#     df = pd.DataFrame(data_list)
#     return df  