from io import StringIO
from pyinfra.operations import files

# files.put(
#     name="Update the message of the day file",
#     src="files/motd",
#     dest="/etc/motd",
#     mode="644",
# )

files.put(
    name="Upload a StringIO object",
    src=StringIO("file contents"),
    dest="/etc/motd",
)
