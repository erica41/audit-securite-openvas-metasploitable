from gvm.connections import UnixSocketConnection
from gvm.protocols.gmp import Gmp
from gvm.transforms import EtreeCheckCommandTransform

TARGET_ID = "aceb6c17-fad0-4563-a201-a17f131c682e"

connection = UnixSocketConnection(path='/run/gvmd/gvmd.sock')

with Gmp(connection=connection, transform=EtreeCheckCommandTransform()) as gmp:
    gmp.authenticate('admin', 'test1234')

    # Récupérer l'ID du scan config "Full and fast"
    configs = gmp.get_scan_configs()
    config_id = None
    for config in configs.findall("config"):
        if config.find("name").text == "Full and fast":
            config_id = config.get("id")
            break

    print(f"Scan Config ID trouvé : {config_id}")

    # Récupérer l'ID du scanner OpenVAS
    scanners = gmp.get_scanners()
    scanner_id = None
    for scanner in scanners.findall("scanner"):
        if scanner.find("name").text == "OpenVAS Default":
            scanner_id = scanner.get("id")
            break

    print(f"Scanner ID trouvé : {scanner_id}")

    # Créer la tâche
    response = gmp.create_task(
        name="Scan-Metasploitable-Auto",
        config_id=config_id,
        target_id=TARGET_ID,
        scanner_id=scanner_id
    )
    task_id = response.get("id")
    print(f"Tâche créée avec succès ! ID : {task_id}")

    # Lancer le scan
    start_response = gmp.start_task(task_id)
    print("Scan lancé !")
    print(start_response)
