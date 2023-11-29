import ast

# Sample DeepDiff output
deep_diff_output = [{'topic_f': {'values_changed': {"root['configs'][0]['value']": {'new_value': 'compact', 'old_value': 'delete'},
                                                    "root['configs'][1]['value']": {'new_value': 'gzip', 'old_value': 'lz4'},
                                                    "root['configs'][2]['value']": {'new_value': 504800010, 'old_value': 604800000}}},
                     'type': 'update'}]

def replace_generic_path(diff_output):
    """
    Replace generic paths in DeepDiff output with actual keys from the JSON object.

    Parameters:
    - diff_output (list): DeepDiff output with generic paths.
    - json_object (dict): Original JSON object.

    Returns:
    - list: DeepDiff output with replaced paths.
    """
    replaced_output = []
    for item in diff_output:
        for key, value in item.items():
            if value in ('update', 'new', 'removed'):
                return replaced_output
            replaced_values = {}
            for index, changes in enumerate(value.values()):
                print("Value.values() " + value.values())
                print("Changes.values() " + changes.values())
                if changes[f"root['configs'][{index}]['value']"]["new_value"] in {"compact", "delete"}:
                    cleanup_policy_str = str(changes).replace(f"root['configs'][{index}]['value']", "cleanup.policy")
                    cleanup_policy = ast.literal_eval(cleanup_policy_str)
                    updated_cleanup_policy = {f"\'{list(cleanup_policy.keys())[index]}\' : \'{cleanup_policy['cleanup.policy']['new_value']}\'"}
                    final_updated_cleanup_policy = str(updated_cleanup_policy).replace('"', "")
                    print(final_updated_cleanup_policy)
                    upc = ast.literal_eval(final_updated_cleanup_policy)
                    replaced_values.update(upc)
                elif changes[f"root['configs'][{index}]['value']"]["new_value"] in {'lz4', 'gzip', 'zstd', 'none', 'snappy'}:
                    compression_type_str = str(changes).replace(f"root['configs'][{index}]['value']", "compression.type")
                    compression_type = ast.literal_eval(compression_type_str)
                    updated_compression_type = {f"\'{list(compression_type.keys())[index]}\' : \'{compression_type['compression.type']['new_value']}\'"}
                    final_updated_compression_type = str(updated_compression_type).replace('"', "")
                    print(final_updated_compression_type)
                    uct = ast.literal_eval(final_updated_compression_type)
                    replaced_values.update(uct)
                elif changes[f"root['configs'][{index}]['value']"]["new_value"] is int:
                    retention_ms_str = str(changes).replace(f"root['configs'][{index}]['value']", "retention.ms")
                    retention_ms = ast.literal_eval(retention_ms_str)
                    updated_retention_ms = {f"\'{list(retention_ms.keys())[index]}\' : \'{retention_ms['retention.ms']['new_value']}\'"}
                    final_updated_retention_ms = str(updated_retention_ms).replace('"', "")
                    print(final_updated_retention_ms)
                    urm = ast.literal_eval(final_updated_retention_ms)
                    replaced_values.update(urm)
                replaced_output.append(replaced_values)
        print(replaced_output)
    return replaced_output



# Replace generic paths with original keys
replaced_diff_output = replace_generic_path(deep_diff_output)
