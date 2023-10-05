#!/usr/bin/python3
"""
This module provides a function to create a .tgz archive from web_static folder
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    now = datetime.now().strftime("%Y%m%d%H%M%S")

    archive_path = "versions/web_static_{}.tgz".format(now)

    local("mkdir -p versions")

    archived = local("tar -cvzf {} web_static".format(archive_path))

    if archived.return_code != 0:
        return None
    else:
        return archive_path
