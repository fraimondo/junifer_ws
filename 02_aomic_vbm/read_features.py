# %%
from junifer.storage import HDF5FeatureStorage


uri = "/data/group/riseml/fraimondo/junifer_ws/features/ds003097_GMD/ds003097_GMD.hdf5"
storage = HDF5FeatureStorage(uri=uri)

# %%
feature_list = storage.list_features()

for k, v in feature_list.items():
    print(f"{k}: {v["name"]}")

# %%  Get features in a dataframe format
features_df = storage.read_df("VBM_GM_Schaefer1000x7_Mean_aggregation")

# %%  Get features in a dictionary format
features_raw = storage.read("VBM_GM_Schaefer1000x7_Mean_aggregation")

# %%


