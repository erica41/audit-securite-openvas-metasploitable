from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp
from gvm.transforms import EtreeCheckCommandTransform

connection = UnixSocketConnection(path='/run/gvmd/gvmd.sock')

with Gmp(connection=connection, transform=EtreeCheckCommandTransform()) as gmp:
    gmp.authenticate('admin', 'test1234')
    targets = gmp.get_targets()
    for target in targets.findall("target"):
        name = target.find("name").text
        target_id = target.get("id")
        print(f"- {name} (ID: {target_id})")
