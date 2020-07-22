#!/usr/bin/env python3

import json
import time


def filter_by_game_version(data, game_version_list):
    return [d for d in data if any(item in d['game_versions'] for item in game_version_list)]


def sort_by_key(data, key, should_reverse=False):
    return sorted(data, key=lambda i: i[key], reverse=should_reverse)


def print_list(data, exclude_keys=[]):
    for d in data:
        print('Project Name: ' + d['project_name'])
        print('Total Downloads: ' + str(d['total_downloads']))
        print('Last Updated: ' + time.strftime('%Y-%m-%d', time.localtime(int(d['date_updated']))))
        print()


if __name__ == "__main__":
    pass
    with open('data.json', "r") as data_file:
        data = json.load(data_file)['modpack_metadata']
    filtered_data = filter_by_game_version(data, ['1.12.2'])
    sorted_data = sort_by_key(filtered_data, 'total_downloads', True)
    print_list(sorted_data)
