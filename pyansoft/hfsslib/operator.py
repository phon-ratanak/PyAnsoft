from typing import List


class Operator:
    """A class for creating 1D, 2D, and 3D models."""

    def __init__(self, oDesign):
        """Initialize the Operator with the design and 3D modeler editor."""
        self.oDesign = oDesign
        self.oEditor = oDesign.SetActiveEditor("3D Modeler")

    def get_face_id(self, name):
        """Get the face ID for the given name."""
        return self.oEditor.GetFaceIDs(name)

    def get_vertex_id_from_face(self, face_id):
        """Get the vertex IDs from the given face ID."""
        return self.oEditor.GetVertexIDsFromFace(face_id)

    def get_vertex_position(self, vertex_id):
        """Get the position of the vertex with the given ID."""
        return self.oEditor.GetVertexPosition(vertex_id)

    def subtract(
        self, blank_parts: List[str], tool_parts: List[str], keep_original: bool = False
    ):
        parameters = [
            "NAME:Selections",
            "Blank Parts:=",
            blank_parts,
            "Tool Parts:=",
            tool_parts,
        ]
        attributes = ["NAME:SubtractParameters", "KeepOriginals:=", keep_original]

        return self.oEditor.Subtract(parameters, attributes)

    def unite(self, object_name: List[str], keep_original: bool = False):
        parameters = ["NAME:Selections", "Selections:=", ",".join(object_name)]
        attributes = ["NAME:UniteParameters", "KeepOriginals:=", keep_original]

        self.oEditor.Unite(parameters, attributes)
        return object_name[0]

    def intersect(self, object_name: List[str], keep_original: bool = False):
        parameters = ["NAME:Selections", "Selections:=", object_name]
        attributes = ["NAME:IntersectParameters", "KeepOriginals:=", keep_original]

        self.oEditor.Intersect(parameters, attributes)
        return object_name[0]

    def imprint(self):
        # ToDo
        pass

    def move(self, object_name: List[str], position: List[str]):

        param_01 = [
            "NAME:Selections",
            "Selections:=",
            object_name,
            "NewPartsModelFlag:=",
            "Model",
        ]

        param_02 = [
            "NAME:TranslateParameters",
            "TranslateVectorX:=",
            position[0],
            "TranslateVectorY:=",
            position[1],
            "TranslateVectorZ:=",
            position[2],
        ]

        return self.oEditor.Move(param_01, param_02)

    def rotate(
        self,
        object_name: List[str],
        rotate_angle: str = "90 deg",
        rotate_axis: str = "Z",
    ):

        param_01 = [
            "NAME:Selections",
            "Selections:=",
            object_name,
            "NewPartsModelFlag:=",
            "Model",
        ]

        param_02 = [
            "NAME:RotateParameters",
            "RotateAxis:=",
            "Z",
            "RotateAngle:=",
            rotate_angle,
        ]

        return self.oEditor.Rotate(param_01, param_02)

    def duplicate_along_line(
        self,
        object_name: List[str],
        position: List[str],
        number_clone: int = 2,
        unit="",
    ):

        param_01 = [
            "NAME:Selections",
            "Selections:=",
            object_name,
            "NewPartsModelFlag:=",
            "Model",
        ]
        param_02 = [
            "NAME:DuplicateToAlongLineParameters",
            "CreateNewObjects:=",
            True,
            "XComponent:=",
            f"{position[0]}{unit}",
            "YComponent:=",
            f"{position[1]}{unit}",
            "ZComponent:=",
            f"{position[2]}{unit}",
            "NumClones:=",
            f"{number_clone}",
        ]
        param_03 = ["NAME:Options", "DuplicateAssignments:=", False]
        return self.oEditor.DuplicateAlongLine(param_01, param_02, param_03)

    def duplicate_around_axis(
        self,
        object_name: List[str],
        rotation_angle: str = "30deg",
        which_axis: str = "Z",
        number_clone: int = 2,
    ):

        param_01 = [
            "NAME:Selections",
            "Selections:=",
            object_name,
            "NewPartsModelFlag:=",
            "Model",
        ]
        param_02 = [
            "NAME:DuplicateAroundAxisParameters",
            "CreateNewObjects:=",
            True,
            "WhichAxis:=",
            which_axis,
            "AngleStr:=",
            rotation_angle,
            "NumClones:=",
            f"{number_clone}",
        ]
        param_03 = ["NAME:Options", "DuplicateAssignments:=", False]
        tuple_name = self.oEditor.DuplicateAroundAxis(param_01, param_02, param_03)
        return tuple_name[0]

    def cover_line(self, object_name: str):
        self.oEditor.CoverLines(
            [
                "NAME:Selections",
                "Selections:=",
                object_name,
                "NewPartsModelFlag:=",
                "Model",
            ]
        )
        return object_name

    @staticmethod
    def get_center_point(A, B):
        import decimal

        """
        Calculate the center point of a 3D coordinate system given two points A and B.

        Parameters:
        A (tuple): A tuple of the form (x, y, z) representing the coordinates of point A.
        B (tuple): A tuple of the form (x, y, z) representing the coordinates of point B.

        Returns:
        tuple: A tuple of the form (x, y, z) representing the coordinates of the center point.
        """
        # Use the decimal module to ensure precise results
        x = (decimal.Decimal(A[0]) + decimal.Decimal(B[0])) / 2
        y = (decimal.Decimal(A[1]) + decimal.Decimal(B[1])) / 2
        z = (decimal.Decimal(A[2]) + decimal.Decimal(B[2])) / 2

        # Convert the coordinates to strings for return
        return str(x), str(y), str(z)

    """ Implement function """

    def create_surface_from_line(self):
        pass


class Analysis:
    def __init__(self, oDesign):
        """Initialize the Operator with the design and 3D modeler editor."""
        self.oDesign = oDesign
        self.oModule = oDesign.GetModule("AnalysisSetup")

    def solution_setup(
        self,
        solution_name: str = "Setup1",
        frequency: float = "1GHz",
        max_delta_S: float = 0.02,
        max_passes: int = 6,
        save_fields: bool = True,
        save_rad_fields_only: bool = False,
        solution_tyoe: str = "HfssDriven",
    ):
        setup_parameter = [
            f"NAME:{solution_name}",
            "Frequency:=",
            f"{frequency}",
            "PortsOnly:=",
            False,
            "MaxDeltaS:=",
            max_delta_S,
            "UseMatrixConv:=",
            False,
            "MaximumPasses:=",
            max_passes,
            "MinimumPasses:=",
            1,
            "MinimumConvergedPasses:=",
            1,
            "PercentRefinement:=",
            30,
            "IsEnabled:=",
            True,
            "BasisOrder:=",
            1,
            "DoLambdaRefine:=",
            True,
            "DoMaterialLambda:=",
            True,
            "SetLambdaTarget:=",
            False,
            "Target:=",
            0.3333,
            "UseMaxTetIncrease:=",
            False,
            "PortAccuracy:=",
            2,
            "UseABCOnPort:=",
            False,
            "SetPortMinMaxTri:=",
            False,
            "UseDomains:=",
            False,
            "UseIterativeSolver:=",
            False,
            "SaveRadFieldsOnly:=",
            save_rad_fields_only,
            "SaveAnyFields:=",
            save_fields,
            "IESolverType:=",
            "Auto",
            "LambdaTargetForIESolver:=",
            0.15,
            "UseDefaultLambdaTgtForIESolver:=",
            True,
        ]
        self.oModule.InsertSetup(solution_tyoe, setup_parameter)
        return solution_name

    def frequency_sweep(
        self,
        sweep_name: str = "sweep",
        freq_range: List[str] = ("1GHz", "10GHz", "0.1GHz"),
        range_type: str = "LinearStep",
        types: str = "Interpolating",
        setup_name: str = "Setup1",
    ):
        if freq_range is None:
            freq_range = [str, str, str]
        freq_parameters = [
            f"NAME:{sweep_name}",
            "IsEnabled:=",
            True,
            "RangeType:=",
            range_type,
            "RangeStart:=",
            freq_range[0],
            "RangeEnd:=",
            freq_range[1],
            "RangeStep:=",
            freq_range[2],
            "Type:=",
            types,
            "SaveFields:=",
            False,
            "SaveRadFields:=",
            False,
            "InterpTolerance:=",
            0.5,
            "InterpMaxSolns:=",
            250,
            "InterpMinSolns:=",
            0,
            "InterpMinSubranges:=",
            1,
            "ExtrapToDC:=",
            False,
            "InterpUseS:=",
            True,
            "InterpUsePortImped:=",
            False,
            "InterpUsePropConst:=",
            True,
            "UseDerivativeConvergence:=",
            False,
            "InterpDerivTolerance:=",
            0.2,
            "UseFullBasis:=",
            True,
            "EnforcePassivity:=",
            True,
            "PassivityErrorTolerance:=",
            0.0001,
        ]
        self.oModule.InsertFrequencySweep(setup_name, freq_parameters)
        return sweep_name
