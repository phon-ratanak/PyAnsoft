from pyansoft.desktop import Desktop
from pyansoft.hfsslib.modeler import Modeler
from pyansoft.hfsslib.operator import Operator, Analysis
from pyansoft.hfsslib.boundary import Boundary
from pyansoft.hfsslib.excitation import Excitation
from pyansoft.hfsslib.definition import Definition


class HFSS:
    def __init__(
        self,
        project_name: str = None,
        design_name: str = None,
        solution_type: str = "DrivenModal",
        specified_version: str = "2016.2",
        # new_desktop_session: bool = True,
    ):
        self.oDesktop = Desktop(
            project_name=project_name, version=specified_version
        ).oDesktop

        self.oProject = self.oDesktop.GetActiveProject()
        self.oProject.InsertDesign("HFSS", design_name, "", "")
        self.oDesign = self.oProject.GetActiveDesign()
        self.oDesign.SetSolutionType(solution_type)

        """ Import Class """
        self.definition = Definition(self.oDesktop)

        self.modeler = Modeler(self.oDesign)
        self.operator = Operator(self.oDesign)
        self.analysis = Analysis(self.oDesign)
        self.boundary = Boundary(self.oDesign)
        self.excitation = Excitation(self.oDesign)

    def __setitem__(self, key, value):

        if "$" in key:
            properties = [
                "NAME:AllTabs",
                [
                    "NAME:ProjectVariableTab",
                    ["NAME:PropServers", "ProjectVariables"],
                    [
                        "NAME:NewProps",
                        [
                            f"NAME:{key}",
                            "PropType:=",
                            "VariableProp",
                            "UserDef:=",
                            True,
                            "Value:=",
                            f"{value}",
                        ],
                    ],
                ],
            ]
            self.oProject = self.oDesktop.GetActiveProject()
            self.oProject.ChangeProperty(properties)
        else:
            properties = [
                "NAME:AllTabs",
                [
                    "NAME:LocalVariableTab",
                    ["NAME:PropServers", "LocalVariables"],
                    [
                        "NAME:NewProps",
                        [
                            f"NAME:{key}",
                            "PropType:=",
                            "VariableProp",
                            "UserDef:=",
                            True,
                            "Value:=",
                            f"{value}",
                        ],
                    ],
                ],
            ]
            self.oDesign = self.oProject.GetActiveDesign()
            self.oDesign.ChangeProperty(properties)
