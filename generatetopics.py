import pandas as pd
import json

df = pd.read_csv('topic_configs.csv')

topics_list = []

# Add document link to the future topic configs

for index, row in df.iterrows():
    topic_dict = {
        "topic_name": row['topic name'],
        "partitions_count": str(row['partition count']),
        "replication_factor": 3,
        "configs": [
            {
                "name": "cleanup.policy",
                "value": str(row['cleanup.policy'])
            },
            {
                "name": "compression.type",
                "value": str(row['compression.type'])
            },
            {
                "name": "retention.ms",
                "value": str(row['retention.ms'])
            },
            {
                "name": "segment.bytes",
                "value": str(row['segment.bytes'])
            }
        ]
    }
    topics_list.append(topic_dict)

json_output = json.dumps(topics_list, indent=4)

print(json_output)

with open('application1/topics/topics.json', 'w') as json_file:
    json_file.write(json_output)
