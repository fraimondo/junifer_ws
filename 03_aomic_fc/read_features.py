# %%
from junifer.storage import HDF5FeatureStorage


uri = "/data/group/riseml/fraimondo/junifer_ws/features/ds003097_FC/ds003097_FC.hdf5"
storage = HDF5FeatureStorage(uri=uri)

# %%
feature_list = storage.list_features()

for k, v in feature_list.items():
    print(f"{k}: {v["name"]}")

# %%  Get features in a dataframe format
features_df = storage.read_df("BOLD_FC-DMNBuckner-5mm_functional_connectivity")

# %%  Get features in a dictionary format
features_raw = storage.read("BOLD_FC-DMNBuckner-5mm_functional_connectivity")

# %%


