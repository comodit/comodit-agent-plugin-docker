from synapse.register_plugin import register
from docks import DocksController

os_mapping = """
[default]
default=None
"""

register(os_mapping, DocksController)
