import os

from send2trash import send2trash
from subprocess import call


class FolderManager:
    def __init__(self, projects_rootdir: str):
        self.projects_rootdir = projects_rootdir

    def delete_contact_folder(self, name):
        contact_dir = os.path.join(self.projects_rootdir, name)
        try:
            send2trash(contact_dir)
        except OSError as e:
            print("Error sending to trash: %s : %s" %
                  (contact_dir, e.strerror))
            return

        print(f'Deleted directory for contact: {name}')

    def create_contact_folder(self, name):
        contact_dir = os.path.join(self.projects_rootdir, name)
        if not os.path.exists(contact_dir):
            os.makedirs(contact_dir)
            print(f'Created directory: {contact_dir}')
        return contact_dir

    def open_directory(self, target_directory):
        call(["open", target_directory])
