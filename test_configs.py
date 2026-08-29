from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp
from gvm.transforms import EtreeCheckCommandTransform

connection = UnixSocketConnection(path='/run/gvmd/gvmd.sock')

with Gmp(connection=connection, transform=EtreeCheckCommandTransform()) as gmp:
    gmp.authenticate('admin', 'test1234')
    configs = gmp.get_scan_configs()
    for config in configs.findall("config"):
        name = config.find("name").text
        print(f"- {name}")
