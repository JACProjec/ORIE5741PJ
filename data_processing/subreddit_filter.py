import pandas as pd
import numpy as np
import json
import os
import random

# Specify the path to json files folder
file_path = os.path.dirname(__file__)

# Input comment for comment, post for post
x = input('Please input comment or post:')

# Create list of jsons for path. Set comment = True if wanting comments, otherwise False for post
if x == 'comment':
    jsons = ['output-comment-2016-01.jsonl', 'output-comment-2016-02.jsonl', 'output-comment-2016-03.jsonl', 'output-comment-2016-04.jsonl', 'output-comment-2016-05.jsonl', 'output-comment-2016-06.jsonl', 'output-comment-2016-07.jsonl', 'output-comment-2016-08.jsonl', 'output-comment-2016-09.jsonl', 'output-comment-2016-10.jsonl', 'output-comment-2016-11.jsonl', 'output-comment-2016-12.jsonl', 'output-comment-2017-01.jsonl', 'output-comment-2017-02.jsonl', 'output-comment-2017-03.jsonl', 'output-comment-2017-04.jsonl', 'output-comment-2017-05.jsonl']
elif x == 'post':
    jsons = [    'output-post-2016-01.jsonl','output-post-2016-02.jsonl','output-post-2016-03.jsonl','output-post-2016-04.jsonl','output-post-2016-05.jsonl','output-post-2016-06.jsonl','output-post-2016-07.jsonl','output-post-2016-08.jsonl','output-post-2016-09.jsonl','output-post-2016-10.jsonl', 'output-post-2016-11.jsonl','output-post-2016-12.jsonl','output-post-2017-01.jsonl','output-post-2017-02.jsonl','output-post-2017-03.jsonl','output-post-2017-04.jsonl','output-post-2017-05.jsonl']
else:
    print("Incorrect input")


# instantiate empty dict to store dataframes
dataframes ={}

# output csv file path
if x == 'comment':
    output_json_path = "/Downloads/filtered_comment_combined.jsonl"
elif x == 'post':
    output_json_path = "/Downloads/filtered_post_combined.jsonl"

# Instantiate blank json
with open(output_json_path, 'w', encoding='utf-8') as file:
    pass 

# List of subreddits 
subreddit_list = ['darksouls3', 'NoMansSkyTheGame', 'StardewValley']

with open(output_json_path, 'w', encoding='utf-8') as output_file:
    for json_file in jsons:
        full_path = os.path.join(file_path, json_file)
        with open(full_path, 'r', encoding='utf-8') as file:
            for line in file:
                data = json.loads(line)
                if data.get('subreddit') in subreddit_list:
                    output_file.write(json.dumps(data) + '\n')


