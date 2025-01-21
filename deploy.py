from io import StringIO
from pyinfra import host, logger
from pyinfra.operations import files

version = host.data.get("version")

logger.info(f"Deploying version {version} to {host.name}")

files.put(
    name="Upload a StringIO object",
    src=StringIO(f"file contents for version {version}\n"),
    dest="/etc/motd",
)

files.get(
    name="Download a file",
    src="/etc/motd",
    dest="motd",
)