from io import StringIO
from facts.swap_enabled import SwapEnabled
from pyinfra import host, logger
from pyinfra.operations import files

version = host.data.get("version")

is_swap_enabled = host.get_fact(SwapEnabled)

logger.info(f"Deploying version {version} to {host.name} with swap enabled: {is_swap_enabled}")

files.put(
    name=f"Upload a StringIO object for {version}",
    src=StringIO(f"file contents for version {version}\n"),
    dest="/etc/motd",
)

files.get(
    name="Download a file",
    src="/etc/motd",
    dest="motd",
)