from typing import List


class Boundary:
    """A class for creating boundary."""

    def __init__(self, oDesign) -> None:
        self.oDesign = oDesign
        self.oModule = oDesign.GetModule("BoundarySetup")

    def master(
        self,
        origin: List[str],
        u_pos: List[str],
        name: str = "Master",
        reverse_v: bool = False,
        face_id: int = None,
    ):
        master_parameters = [
            f"NAME:{name}",
            "Faces:=",
            [int(face_id)],
            ["NAME:CoordSysVector", "Origin:=", origin, "UPos:=", u_pos],
            "ReverseV:=",
            reverse_v,
        ]

        return self.oModule.AssignMaster(master_parameters)

    def slave(
        self,
        origin: List[str],
        u_pos: List[str],
        name: str = "Slave",
        master: str = None,
        reverse_v: bool = False,
        saning_angles: bool = True,
        phi: str = "0deg",
        theta: str = "0deg",
        face_id: int = None,
    ):
        slave_parameters = [
            f"NAME:{name}",
            "Faces:=", [int(face_id)],
            ["NAME:CoordSysVector", "Origin:=", origin, "UPos:=", u_pos],
            "ReverseV:=", reverse_v,
            "Master:=", master,
            "UseScanAngles:=", saning_angles,
            "Phi:=", phi,
            "Theta:=", theta,
        ]
        return self.oModule.AssignSlave(slave_parameters)

    def assign_finite_conductor(
        self,
        object_name: List[str],
        cond_name: str = "FiniteCond",
        material: str = None,
        roughness: str = "0um",
        infinite_ground_plane: bool = False,
    ):

        finite_cond_parameter = [
            f"NAME:{cond_name}",
            "Objects:=", object_name,
            "UseMaterial:=", True if material is not None else False,
            "Material:=", material,
            "UseThickness:=", False,
            "Roughness:=", roughness,
            "InfGroundPlane:=", infinite_ground_plane,
            "IsTwoSided:=", False,
            "IsInternal:=", True,
        ]
        return self.oModule.AssignFiniteCond(finite_cond_parameter)

    def assign_perfect_E(
        self,
        object_name: List[str],
        bc_name: str = "PerfE",
        infinite_ground: bool = False,
    ):
        perfect_E_parameters = [
            f"NAME:{bc_name}",
            "Objects:=", object_name,
            "InfGroundPlane:=", infinite_ground,
        ]
        return self.oModule.AssignPerfectE(perfect_E_parameters)

    def assign_perfect_H(
        self,
        object_name: List[str],
        bc_name: str = "PerfH",
    ):
        perfect_H_parameters = [
            f"NAME:{bc_name}",
            "Objects:=", object_name,
        ]
        return self.oModule.AssignPerfectH(perfect_H_parameters)

    def assign_lumped_RLC(
        self,
        object_name: List[str],
        start_point: List[str],
        stop_point: List[str],
        rlc_name: str = "LumpRLC",
        R_value: str = None,
        L_value: str = None,
        C_value: str = None,
    ):
        R = [False, "0ohm"] if R_value is None else [True, R_value]
        L = [False, "0nH"] if L_value is None else [True, L_value]
        C = [False, "0pF"] if C_value is None else [True, C_value]

        RLC_parameters = [
            f"NAME:{rlc_name}",
            "Objects:=",            object_name,
            ["NAME:CurrentLine", "Start:=", start_point, "End:=", stop_point],
            "UseResist:=", R[0],
            "Resistance:=", R[1],
            "UseInduct:=", L[0],
            "Inductance:=", L[1],
            "UseCap:=", C[0],
            "Capacitance:=", C[1],
        ]
        return self.oModule.AssignLumpedRLC(RLC_parameters)
