import pandas as pd
import json

df = pd.read_csv('topic_configs.csv')

with open('topic_template.json', 'r') as template_file:
    template = json.load(template_file)

topics_list = []

for index, row in df.iterrows():
    topic_str = json.dumps(template)

    topic_str = topic_str.replace("{topic_name}", row['topic name'])
    topic_str = topic_str.replace('"{count}"', str(row['partition count']))
    topic_str = topic_str.replace('"{retention.ms}"', str(row['retention.ms']))
    topic_str = topic_str.replace('"{segment.bytes}"', str(row['segment.bytes']))
    
    topics_list.append(json.loads(topic_str))

json_output = json.dumps(topics_list, indent=4)

with open('topics.json', 'w') as json_file:
    json_file.write(json_output)
