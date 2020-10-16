

import pandas as pd
import requests



def list_function_handler(card_custom_field, custom_field):
    list_of_options = {x['id']: x for x in custom_field['options']}
    option = list_of_options[card_custom_field['idValue']]
    return option['value']['text']


CUSTOM_FIELD_GET_VALUE = {
    # How we retrieve the value given a custom field type
    'number': lambda card_custom_field, _: float(card_custom_field['value']['number']),
    'text': lambda card_custom_field, _: card_custom_field['value']['text'],
    'date': lambda card_custom_field, _: (card_custom_field['value']['date']),
    'checkbox': lambda card_custom_field, _: card_custom_field['value']['checked'] == 'true',
    'list': list_function_handler,
}

API_URL = 'https://api.trello.com/1/boards'


class TrelloAPIError(Exception):
    pass


class TrelloConnector():
    
    def __init__(self, key_id,token, board_id):
        self.board_id  = board_id
        self.token = token
        self.key_id = key_id

    def get_board(self, path, **custom_params):
        url = '{API_URL}/{path}'.format(API_URL=API_URL,path=path)
        try:
            result = requests.get(
                url, params={'key': self.key_id, 'token': self.token, **custom_params}
            )
            return result.json()
        except:
            raise TrelloAPIError
    @staticmethod
    def replace_id_by_value(
        card_with_id,
        lists_ids_mapping=None,
        labels_id_mapping=None,
        members_id_mapping=None,
        custom_fields_id_mapping=None,
    ):
       

        # id, name and url fields do not need to translate from id to value
        card_with_value = {'id': card_with_id['id']}

        if 'name' in card_with_id:
            card_with_value['name'] = card_with_id['name']
        if 'url' in card_with_id:
            card_with_value['url'] = card_with_id['url']

        # lists, members and labels need to translate from a id to a value
        if lists_ids_mapping:
            card_with_value['lists'] = lists_ids_mapping[card_with_id['idList']]
        if members_id_mapping:
            card_with_value['members'] = [
                members_id_mapping[member] for member in card_with_id['idMembers']
            ]
        if labels_id_mapping:
            card_with_value['labels'] = [
                labels_id_mapping[label['id']] for label in card_with_id['labels']
            ]

        # custom fields
        if custom_fields_id_mapping:
            for card_custom_field in card_with_id['customFieldItems']:
                custom_field = custom_fields_id_mapping[card_custom_field['idCustomField']]
                get_value = CUSTOM_FIELD_GET_VALUE[custom_field['type']]
                card_with_value[custom_field['name']] = get_value(card_custom_field, custom_field)

        return card_with_value

    def retrieve_data(self, data_source):
       
        fields_for_request = []
        lists_ids_mapping = labels_id_mapping = members_id_mapping = custom_fields_id_mapping = None

        if 'name' in data_source:
            fields_for_request += ['name']
        if 'url' in data_source:
            fields_for_request += ['url']
        if 'lists' in data_source:
            fields_for_request += ['idList']
            lists_ids_mapping = {
                x['id']: x['name']
                for x in self.get_board("{board_id}/lists".format(board_id=self.board_id), fields='name')
            }
        if 'labels' in data_source:
            fields_for_request += ['labels']
            labels_id_mapping = {
                x['id']: x['name']
                for x in self.get_board("{board_id}/labels".format(board_id=self.board_id), fields='name')
            }
        if 'members' in data_source:
            fields_for_request += ['idMembers']
            members_id_mapping = {
                x['id']: x['fullName']
                for x in self.get_board("{board_id}/members".format(board_id=self.board_id), fields='fullName')
            }

        if "custom_fields" in data_source:
            custom_fields_id_mapping = {
                x['id']: x
                for x in self.get_board("{board_id}/customFields".format(board_id=self.board_id), fields='name')
            }   

        # get cards
        cards_with_id = self.get_board(
            "{board_id}/cards".format(board_id=self.board_id),
            fields=fields_for_request,
            customFieldItems='true' if "custom_fields" in data_source else 'false',
        )

        # replace all id in `cards_with_id` by the corresponding readable value
        cards_with_value = [
            self.replace_id_by_value(
                card_with_id,
                lists_ids_mapping,
                labels_id_mapping,
                members_id_mapping,
                custom_fields_id_mapping,
            )
            for card_with_id in cards_with_id
        ]

        return pd.DataFrame(cards_with_value)



def main(key, token,board_id,  export=False):
    data = ["name","url","list","labels","members","custom_fields"]
    obj = TrelloConnector(key, token,board_id)
    try:
        df = obj.retrieve_data(data)
    except TrelloAPIError:
        print("failed to connect to trello. please check token, key and board id")
        return False
    name = ""
    if export == "csv":
        name = "trello-export.csv"
        df.to_csv(name)
    elif export == "xls":
        name = "trello-export.xlsx"
        df.to_excel(name) 
    if name:
        print("Exported to : "+ name) 
    return df

if __name__ == '__main__':
    token = ""
    key = ""
    board_id = "VCmIpC16"
    main(key,token,board_id)
    