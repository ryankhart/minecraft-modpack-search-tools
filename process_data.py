import json


def filter_by_game_version(data, game_version_list):
    return [d for d in data if any(item in d['game_versions'] for item in game_version_list)]


def sort_by(data):
    pass


def print_list(data):
    pass

if __name__ == "__main__":
    pass
    with open('data.json', "r") as data_file:
        data = json.load(data_file)['modpack_metadata']
    filtered_data = filter_by_game_version(data, ['1.12.2'])
    print(filtered_data)
    