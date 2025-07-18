import h5py
import json

h5_path = "keras_model.h5"

# Step 1: Load and parse the model config string
with h5py.File(h5_path, "r") as f:
    if 'model_config' not in f.attrs:
        raise ValueError("No 'model_config' attribute found in the HDF5 file.")
    
    raw_config = f.attrs['model_config']
    
    # Only decode if it's bytes
    if isinstance(raw_config, bytes):
        model_config_str = raw_config.decode('utf-8')
    else:
        model_config_str = raw_config
    
    model_config = json.loads(model_config_str)

# Step 2: Recursively remove all 'groups' keys from DepthwiseConv2D layers
def remove_groups_key(config):
    if isinstance(config, dict):
        if config.get("class_name") == "DepthwiseConv2D":
            if "groups" in config.get("config", {}):
                print("Removing 'groups' from:", config["config"].get("name", "unknown"))
                config["config"].pop("groups", None)
        for key, value in config.items():
            remove_groups_key(value)
    elif isinstance(config, list):
        for item in config:
            remove_groups_key(item)

remove_groups_key(model_config)

# Step 3: Save the cleaned config back to the H5 file
with h5py.File(h5_path, "a") as f:
    cleaned_config_str = json.dumps(model_config)
    f.attrs.modify('model_config', cleaned_config_str.encode('utf-8'))

print("✅ Successfully removed all 'groups' keys. Try loading the model again now.")
