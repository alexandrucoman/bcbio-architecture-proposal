import collections

Flavor = collections.namedtuple(
    "Flavor",
    ["cpus", "memory"]
)

Instance = collections.namedtuple(
    "Instance",
    ["name", "state", "type", "ip_address", "placement"])