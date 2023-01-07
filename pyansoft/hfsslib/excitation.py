from typing import List


class Excitation:
    """A class for creating excitation."""

    def __init__(self, oDesign) -> None:
        self.oDesign = oDesign
        self.oModule = oDesign.GetModule("BoundarySetup")

    def floquet_port(
        self,
        A_vector: List[str],
        B_vector: List[str],
        name: str = "FloquetPort",
        number_modes: int = 2,
        deembed: str = "0mm",
        face_id: int = None,
    ):
        do_deembed = True if deembed != "0mm" else False

        floquet_parameters = [
            f"NAME:{name}",
            "Faces:=",
            [int(face_id)],
            "NumModes:=",
            number_modes,
            "RenormalizeAllTerminals:=",
            True,
            "DoDeembed:=",
            do_deembed,
            "DeembedDist:=",
            deembed,
            [
                "NAME:Modes",
                [
                    "NAME:Mode1",
                    "ModeNum:=",
                    1,
                    "UseIntLine:=",
                    False,
                    "CharImp:=",
                    "Zpi",
                ],
                [
                    "NAME:Mode2",
                    "ModeNum:=",
                    2,
                    "UseIntLine:=",
                    False,
                    "CharImp:=",
                    "Zpi",
                ],
            ],
            "ShowReporterFilter:=",
            False,
            "ReporterFilter:=",
            [False, False],
            "UseScanAngles:=",
            True,
            "Phi:=",
            "0deg",
            "Theta:=",
            "0deg",
            ["NAME:LatticeAVector", "Start:=", A_vector[0], "End:=", A_vector[1]],
            ["NAME:LatticeBVector", "Start:=", B_vector[0], "End:=", B_vector[1]],
            [
                "NAME:ModesList",
                [
                    "NAME:Mode",
                    "ModeNumber:=",
                    1,
                    "IndexM:=",
                    0,
                    "IndexN:=",
                    0,
                    "KC2:=",
                    0,
                    "PropagationState:=",
                    "Propagating",
                    "Attenuation:=",
                    0,
                    "PolarizationState:=",
                    "TE",
                    "AffectsRefinement:=",
                    True,
                ],
                [
                    "NAME:Mode",
                    "ModeNumber:=",
                    2,
                    "IndexM:=",
                    0,
                    "IndexN:=",
                    0,
                    "KC2:=",
                    0,
                    "PropagationState:=",
                    "Propagating",
                    "Attenuation:=",
                    0,
                    "PolarizationState:=",
                    "TM",
                    "AffectsRefinement:=",
                    True,
                ],
            ],
        ]

        return self.oModule.AssignFloquetPort(floquet_parameters)
