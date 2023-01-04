from typing import List


class Modeler:
    """A class for creating 1D, 2D, and 3D models."""

    def __init__(self, oDesign) -> None:
        self.oDesign = oDesign
        self.oEditor = oDesign.SetActiveEditor("3D Modeler")

    """ 2D Objects =========================================="""

    def create_rectangle(
            self,
            position: List[float],
            size: List[float],
            which_axis: str = "Z",
            unit: str = "mm",
            name: str = "Rectangular",
            color: str = "(143 175 143)",
            transparency: float = 0,
            material: str = "vacuum",
            solve_inside: bool = True,

    ):
        rectangle_parameters = [
            "NAME:RectangleParameters",
            "IsCovered:=", True,
            "XStart:=", f"{position[0]}{unit}",
            "YStart:=", f"{position[1]}{unit}",
            "ZStart:=", f"{position[2]}{unit}",
            "Width:=", f"{size[0]}{unit}",
            "Height:=", f"{size[1]}{unit}",
            "WhichAxis:=", which_axis
        ]
        attributes = [
            "NAME:Attributes",
            "Name:=", name,
            "Flags:=", "",
            "Color:=", color,
            "Transparency:=", transparency,
            "PartCoordinateSystem:=", "Global",
            "UDMId:=", "",
            "MaterialValue:=", f"\"{material}\"",
            "SolveInside:=", solve_inside
        ]
        return self.oEditor.CreateRectangle(rectangle_parameters, attributes)

    def create_circle(
            self,
            position: List[float],
            radius: float,
            which_axis: str = "Z",
            unit: str = "mm",
            name: str = "Circle",
            color: str = "(143 175 143)",
            transparency: float = 0,
            material: str = "vacuum",
            solve_inside: bool = True,
    ):
        circle_parameters = [
            "NAME:CircleParameters",
            "IsCovered:=", True,
            "XCenter:=", f"{position[0]}" + unit,
            "YCenter:=", f"{position[1]}" + unit,
            "ZCenter:=", f"{position[2]}" + unit,
            "Radius:=", f"{radius}" + unit,
            "WhichAxis:=", which_axis,
            "NumSegments:=", "0"
        ]
        attributes = [
            "NAME:Attributes",
            "Name:=", name,
            "Flags:=", "",
            "Color:=", color,
            "Transparency:=", transparency,
            "PartCoordinateSystem:=", "Global",
            "UDMId:=", "",
            "MaterialValue:=", f"\"{material}\"",
            "SolveInside:=", solve_inside
        ]
        return self.oEditor.CreateCircle(circle_parameters, attributes)

    def create_regular_polygon(
            self,
            center: List[float],
            start: List[float],
            number_sides: int = 12,
            which_axis: str = "Z",
            unit: str = "mm",
            name: str = "RegularPolygon",
            color: str = "(143 175 143)",
            transparency: float = 0,
            material: str = "vacuum",
            solve_inside: bool = True,
    ):
        regular_polygon_parameters = [
            "NAME:RegularPolygonParameters",
            "IsCovered:=", True,
            "XCenter:=", f"{center[0]}" + unit,
            "YCenter:=", f"{center[1]}" + unit,
            "ZCenter:=", f"{center[2]}" + unit,
            "XStart:=", f"{start[0]}" + unit,
            "YStart:=", f"{start[1]}" + unit,
            "ZStart:=", f"{start[2]}" + unit,
            "NumSides:=", f"{number_sides}",
            "WhichAxis:=", which_axis
        ]
        attributes = [
            "NAME:Attributes",
            "Name:=", name,
            "Flags:=", "",
            "Color:=", color,
            "Transparency:=", transparency,
            "PartCoordinateSystem:=", "Global",
            "UDMId:=", "",
            "MaterialValue:=", f"\"{material}\"",
            "SolveInside:=", solve_inside
        ]
        return self.oEditor.CreateRegularPolygon(regular_polygon_parameters, attributes)

    def create_ellipse(
            self,
            center: List[float],
            major_radius: int = 1,
            ratio: int = 2,
            which_axis: str = "Z",
            unit: str = "mm",
            name: str = "Ellipse",
            color: str = "(143 175 143)",
            transparency: float = 0,
            material: str = "vacuum",
            solve_inside: bool = True,
    ):
        regular_ellipse = [
            "NAME:EllipseParameters",
            "IsCovered:=", True,
            "XCenter:=", f"{center[0]}" + unit,
            "YCenter:=", f"{center[1]}" + unit,
            "ZCenter:=", f"{center[2]}" + unit,
            "MajRadius:=", f"{major_radius}" + unit,
            "Ratio:=", f"{ratio}",
            "WhichAxis:=", which_axis,
            "NumSegments:=", "0"
        ]
        attributes = [
            "NAME:Attributes",
            "Name:=", name,
            "Flags:=", "",
            "Color:=", color,
            "Transparency:=", transparency,
            "PartCoordinateSystem:=", "Global",
            "UDMId:=", "",
            "MaterialValue:=", f"\"{material}\"",
            "SolveInside:=", solve_inside
        ]
        return self.oEditor.CreateEllipse(regular_ellipse, attributes)

    """ 3D Objects ========================================== """

    def create_box(
            self,
            position: List[float],
            size: List[float],
            unit: str = "mm",
            name: str = "Ellipse",
            color: str = "(143 175 143)",
            transparency: float = 0,
            material: str = "vacuum",
            solve_inside: bool = True,
    ):
        box_parameters = [
            "NAME:BoxParameters",
            "XPosition:=", f"{position[0]}" + unit,
            "YPosition:=", f"{position[1]}" + unit,
            "ZPosition:=", f"{position[2]}" + unit,
            "XSize:=", f"{size[0]}" + unit,
            "YSize:=", f"{size[1]}" + unit,
            "ZSize:=", f"{size[2]}" + unit
        ]
        attributes = [
            "NAME:Attributes",
            "Name:=", name,
            "Flags:=", "",
            "Color:=", color,
            "Transparency:=", transparency,
            "PartCoordinateSystem:=", "Global",
            "UDMId:=", "",
            "MaterialValue:=", f"\"{material}\"",
            "SolveInside:=", solve_inside
        ]
        return self.oEditor.CreateBox(box_parameters, attributes)

    def create_cylinder(
            self,
            center: List[float],
            radius: float,
            height: float,
            which_axis: str = "Z",
            unit: str = "mm",
            name: str = "Ellipse",
            color: str = "(143 175 143)",
            transparency: float = 0,
            material: str = "vacuum",
            solve_inside: bool = True,
    ):
        cylinder_parameters = [
            "NAME:CylinderParameters",
            "XCenter:=", f"{center[0]}" + unit,
            "YCenter:=", f"{center[1]}" + unit,
            "ZCenter:=", f"{center[2]}" + unit,
            "Radius:=", f"{radius}" + unit,
            "Height:=", f"{height}" + unit,
            "WhichAxis:=", which_axis,
            "NumSides:=", "0"
        ]
        attributes = [
            "NAME:Attributes",
            "Name:=", name,
            "Flags:=", "",
            "Color:=", color,
            "Transparency:=", transparency,
            "PartCoordinateSystem:=", "Global",
            "UDMId:=", "",
            "MaterialValue:=", f"\"{material}\"",
            "SolveInside:=", solve_inside
        ]
        return self.oEditor.CreateCylinder(cylinder_parameters, attributes)


