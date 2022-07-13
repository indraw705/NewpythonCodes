import json
import requests
import urllib3
from requests.auth import HTTPBasicAuth


def write_to_file(date, group_by, resp):
    resp = str(resp).replace(",", ",\n").replace("{", "{\n")
    with open("QoQ.json", "a") as file_object:
        file_object.write(date + " >> " + group_by + "\n\n")
        file_object.write(str(resp))
        file_object.write("\n\n")


def write_size_to_file(date, index, size):
    with open("QoQ.json", "a") as file_object:
        file_object.write(date + " >> " + index.upper() + "\n\n")
        file_object.write(str(size[:-2]))
        file_object.write("\n\n")


def get_critical_asset_data(date, agentId, group_by):
    url = "https://kubeingress." + pod + ".eng.sjc01.qualys.com/ioc-ws/events/count"
    params = {"filter": f'(dateTime:["{date}T00:00:00.000Z".."{date}T23:59:59.999Z"]) AND asset.agentid:{agentId}',
              "groupBy": group_by,
              "state": "false", "pagesize": 5000}
    headers = {"customerId": customer_id,
               "S2S-Authorization": S2S_auth_token}
    response = requests.get(url, headers=headers, params = params, verify=False)
    resp = json.loads(response.text)
    write_to_file(date, group_by, resp)


def get_agent_wise_count(resp, uuid):
    count = resp.get(uuid)
    if count:
        return count
    else:
        return 0


def getQoQStats_EventsCount_by_type(date, group_by):

    url = "https://kubeingress." + pod + ".eng.sjc01.qualys.com/ioc-ws/events/count"
    params = {"filter": f'(dateTime:["{date}T00:00:00.000Z".."{date}T23:59:59.999Z"])', "groupBy": group_by,
              "state": "false", "pagesize": 5000}
    headers = {"customerId": customer_id,
               "S2S-Authorization": S2S_auth_token}
    response = requests.get(url, headers=headers, verify=False, params=params)
    resp = json.loads(response.text)
    write_to_file(date, group_by, resp)


def get_auth_key():
    url = "https://kubeingress." + pod + ".eng.sjc01.qualys.com/ioc-ws/auth"
    headers = {"Content-Type": "application/json",
               "accept": "*/*"}
    data = {"username": "ioc", "password": "ioc" + pod + ""}
    data = json.dumps(data)
    response = (requests.post(url=url, headers=headers, data=data, verify=False))
    resp = json.loads(response.text)
    return str(resp["jwt"])


def getQoQStats_EventsCount_by_agent(date, group_by):
    url = "https://kubeingress." + pod + ".eng.sjc01.qualys.com/ioc-ws/events/count"
    params = {"filter": f'(dateTime:["{date}T00:00:00.000Z".."{date}T23:59:59.999Z"])', "groupBy": group_by,
              "state": "false", "pagesize": 5000, "limit": 25}
    headers = {"customerId": customer_id,
               "S2S-Authorization": S2S_auth_token}
    response = requests.get(url, headers=headers,params = params, verify=False)
    resp = json.loads(response.text)
    with open("QoQ.json", "a") as file_object:
        file_object.write(date + " >> " + group_by + "\n\n")
        file_object.write((str(get_agent_wise_count(resp, "990fad5c-a3b9-482a-b5d7-e79c7e94bc76"))) + ":\n")
        file_object.write((str(get_agent_wise_count(resp, "320a6b00-5961-4f2e-a4c1-6f4f8e61b8b4"))) + ":\n")
        file_object.write((str(get_agent_wise_count(resp, "75d72401-32ec-41ee-9488-cef0767e588c"))) + ":\n")
        file_object.write((str(get_agent_wise_count(resp, "3c2e9c9a-3859-4aac-b28c-725de497c2b2"))) + ":\n")
        file_object.write((str(get_agent_wise_count(resp, "e3e8cf0d-9b08-4e40-9fa6-a84854276707"))) + ":\n")
        file_object.write((str(get_agent_wise_count(resp, "83f2560e-2d80-4aa0-899f-eeeebe291282"))) + ":\n")
        file_object.write((str(get_agent_wise_count(resp, "16625b0b-768d-49f8-9782-c1d1bfeda43f"))) + ":\n")
        file_object.write((str(get_agent_wise_count(resp, "0dc0b321-e8ec-4cb7-ba3a-dfc7b44b348d"))) + ":\n")
        file_object.write((str(get_agent_wise_count(resp, "c8d370d1-7810-4736-9e37-3cad272f73b4"))) + ":\n")
        file_object.write((str(get_agent_wise_count(resp, "5b8944d1-497e-4984-a649-edacfedf0123"))) + ":\n")
        file_object.write((str(get_agent_wise_count(resp, "3edefba3-b0cd-4700-834b-0f87ccb9693f"))) + ":\n")
        file_object.write((str(get_agent_wise_count(resp, "83df61dc-c6d5-4c3b-85d0-e9c01f608143"))) + ":\n")
        file_object.write((str(get_agent_wise_count(resp, "073f949b-61cc-450d-a516-6c7940b7adc7"))) + ":\n")
        file_object.write((str(get_agent_wise_count(resp, "33fcf9e1-c53f-453c-bff9-d352610ca581"))) + ":\n")
        file_object.write((str(get_agent_wise_count(resp, "5fedba72-2598-41d1-a1d2-133e34b08edb"))) + ":\n")
        file_object.write((str(get_agent_wise_count(resp, "c6bff1e0-4d7b-494d-a017-68170ee2075b"))) + ":\n")
        file_object.write((str(get_agent_wise_count(resp, "13566268-a928-4121-9040-887e6df274f3"))) + ":\n")


def get_size_of_index(date):
    url = f"http://qelsdataioc01.{pod}.eng.sjc01.qualys.com:50140/_cat/indices/ioc_ts_rt_{customer_id}_{date}"
    print(url)
    resp = requests.get(url=url, auth=HTTPBasicAuth('admin', 'admin123'), verify=False)
    response = resp.text.split(" ")
    index, store_size, pre_store_size = response[2], response[8], response[9]
    print(f'{index} - {store_size} - {pre_store_size}')
    write_size_to_file(date, index, store_size)


if __name__ == '__main__':
    pod = "p13"
    customer_id = "2dd48beb-d268-5821-83bf-8cfa50611ea1"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    S2S_auth_token = get_auth_key()
    agentId = "0dc0b321-e8ec-4cb7-ba3a-dfc7b44b348d"
    with open("QoQ.json", "w") as file_object:
        file_object.truncate(0)
    for i in range(12, 13):
        getQoQStats_EventsCount_by_type("2022-07-" + str(i), "process.name")
        getQoQStats_EventsCount_by_type("2022-07-" + str(i), "file.name")
        getQoQStats_EventsCount_by_type("2022-07-" + str(i), "network.remote.address.ip")
        getQoQStats_EventsCount_by_agent("2022-07-" + str(i), "asset.agentid")
        getQoQStats_EventsCount_by_type("2022-07-" + str(i), "type")
        get_size_of_index("2022-07-" + str(i).rjust(2, '0'))

        # get_critical_asset_data("2022-07-" + str(i), agentId, "process.name")
        # get_critical_asset_data("2022-07-" + str(i), agentId, "file.name")
        # get_critical_asset_data("2022-07-" + str(i), agentId, "network.remote.address.ip")
