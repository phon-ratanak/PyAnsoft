import os
import pathlib
import win32com.client as win32


def create_default_dir():
    """
    Create the default directory for storing examples.

    Returns:
        str: The path to the default directory.
    """
    home = pathlib.Path.home()
    path = home / 'Documents' / 'Ansoft' / 'Examples'

    os.makedirs(path, exist_ok=True)
    return str(path)


class Desktop:
    """
    Class for interacting with Ansoft Electronics Desktop.
    """

    def __init__(self, project_name: str = None, version: str = "2016.2",):
        self.oAnsoftApp = win32.Dispatch(f"Ansoft.ElectronicsDesktop.{version}")
        self.oDesktop = self.oAnsoftApp.GetAppDesktop()
        project_list = self.oDesktop.GetProjectList()

        if project_name in project_list:
            self.oDesktop.SetActiveProject(project_name)
        else:
            self.oDesktop.NewProject(project_name)





