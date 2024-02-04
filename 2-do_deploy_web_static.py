# Import Fabric API
from fabric.api import *
import os

# Define the remote hosts
env.hosts = ['<54.236.12.178>', '<54.226.35.202>']

def do_deploy(archive_path):
    """
    Distribute an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False

    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, '/tmp/')

    # Extract the archive to the folder /data/web_static/releases/<archive filename without extension>
    archive_filename = os.path.basename(archive_path)
    release_folder = '/data/web_static/releases/{}'.format(
        archive_filename.replace('.tgz', '')
    )
    run('mkdir -p {}'.format(release_folder))
    run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

    # Delete the archive from the web server
    run('rm /tmp/{}'.format(archive_filename))

    # Move the contents of the web_static folder to the release folder
    run('mv {}/web_static/* {}'.format(release_folder, release_folder))

    # Remove the web_static folder
    run('rm -rf {}/web_static'.format(release_folder))

    # Delete the symbolic link /data/web_static/current
    run('rm -rf /data/web_static/current')

    # Create a new symbolic link to the new version
    run('ln -s {} /data/web_static/current'.format(release_folder))

    print("New version deployed!")
    return True
