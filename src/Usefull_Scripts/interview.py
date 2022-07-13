import json

dict1 = {}

def create_dict1(file_content):
    dict1["remote_addr"] = file_content[0]
    time = f"{file_content[3]}, {file_content[4]}"
    dict1["time"] = time
    dict1["method"] = file_content[5]
    dict1["path"] = file_content[6]
    dict1["version"] = file_content[7]
    dict1["response"] = file_content[8]
    dict1["bytesSent"] = file_content[9]
    user_agent =  f"{file_content[11]} ' '  {file_content[12]} ' '  {file_content[13]} "
    dict1["user_agent"] = user_agent.replace("\'", "").replace("\n"," ")
    return dict1





def get_from_file():
    with open("ind.log", "r") as f:
        content = f.read()
        file_content = content.split(" ")
        print(file_content)
        dict1 = create_dict1(file_content)
        return dict1
file_content = get_from_file()
print(str(file_content).replace(",",",\n").strip())

# print(type(str(file_content)))
