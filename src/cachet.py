import cachetclient.cachet as cachet
import json
import os


API_TOKEN = os.getenv('API_TOKEN')
API_ENDPOINT = os.getenv('API_ENDPOINT')


def get_components():
    res = {}
    json_data = cachet.Components(endpoint=API_ENDPOINT, api_token=API_TOKEN, verify=False).get()
    items = json.loads(json_data)
    for item in items['data']:
        res[item['id']] = item
    return res


components = get_components()


def get_incidents():
    res = []
    json_data = cachet.Incidents(endpoint=API_ENDPOINT, api_token=API_TOKEN, verify=False).get()
    incidents = json.loads(json_data)
    for item in incidents['data']:
        component_id = item['component_id']
        item['component'] = components.get(component_id, None)
        res.append(item)

    return res
