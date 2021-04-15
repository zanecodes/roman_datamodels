from asdf.extension import ManifestExtension
from .stnode import TaggedObjectNodeConverter


DATAMODEL_CONVERTERS = [
    TaggedObjectNodeConverter(),
]

DATAMODEL_EXTENSIONS = [
    ManifestExtension.from_uri(
        "http://stsci.edu/asdf/datamodels/roman/manifests/datamodels-1.0",
    	converters=DATAMODEL_CONVERTERS)
]