from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp
from gvm.transforms import EtreeCheckCommandTransform

connection = UnixSocketConnection(path='/run/gvmd/gvmd.sock')

with Gmp(connection=connection, transform=EtreeCheckCommandTransform()) as gmp:
    gmp.authenticate('admin', 'test1234')
    version = gmp.get_version()
    print("Connexion réussie ! Version GMP :")
    print(version.find("version").text)
