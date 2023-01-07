from typing import List


class Modeler:
    """A class for creating 1D, 2D, and 3D models."""

    def __init__(self, oDesign) -> None:
        self.oDesign = oDesign
        self.oEditor = oDesign.SetActiveEditor("3D Modeler")

    """ 1D Objects ============================================="""

    def create_line(
            self,
            pl_point: List[float],
            name: str = "Polyline",
            unit: str = "",
            color: str = "(143 175 143)",
            transparency: float = 0,
            material: str = "vacuum",
            solve_inside: bool = True,

    ):

        pl_points = ["NAME:PolylinePoints"] + [
            ["NAME:PLPoint",
             "X:=", f"{p[0]}{unit}",
             "Y:=", f"{p[1]}{unit}",
             "Z:=", f"{p[2]}{unit}"] for p in pl_point
        ]

        pl_segments = ["NAME:PolylineSegments"] + [
            ["NAME:PLSegment",
            "SegmentType:=", "Line",
            "StartIndex:=", s_index,
            "NoOfPoints:=", 2] for s_index in range(len(pl_point)-1)
        ]

        pl_sections = [
			"NAME:PolylineXSection",
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]

        parameters = [
            "NAME:PolylineParameters",
            "IsPolylineCovered:="	, True,
            "IsPolylineClosed:="	, False, 
            pl_points, pl_segments, pl_sections
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
        
        return self.oEditor.CreatePolyline(parameters, attributes)


    def create_center_point_arc(
            self,
            pl_point: List[float],
            arc_center: List[str],
            arc_angle: str = "90deg",
            arc_plane: str = "XY",
            name: str = "Polyline",
            unit: str = "",
            color: str = "(143 175 143)",
            transparency: float = 0,
            material: str = "vacuum",
            solve_inside: bool = True,

    ):

        pl_points = ["NAME:PolylinePoints"] + [
            ["NAME:PLPoint",
             "X:=", f"{p[0]}{unit}",
             "Y:=", f"{p[1]}{unit}",
             "Z:=", f"{p[2]}{unit}"] for p in pl_point
        ]

        pl_segments = [
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "AngularArc",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2,
				"NoOfSegments:="	, "0",
				"ArcAngle:="		, arc_angle,
				"ArcCenterX:="		, f"{arc_center[0]}{unit}",
				"ArcCenterY:="		, f"{arc_center[1]}{unit}",
				"ArcCenterZ:="		, f"{arc_center[2]}{unit}",
				"ArcPlane:="		, arc_plane
			]
		]

        pl_sections = [
			"NAME:PolylineXSection",
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]

        parameters = [
            "NAME:PolylineParameters",
            "IsPolylineCovered:="	, True,
            "IsPolylineClosed:="	, False, 
            pl_points, pl_segments, pl_sections
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

        return self.oEditor.CreatePolyline(parameters, attributes)

    """ 2D Objects ================================================="""

    def create_rectangle(
            self,
            position: List[float],
            size: List[float],
            which_axis: str = "Z",
            unit: str = "",
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
            unit: str = "",
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

    """ 3D Objects ========================== """



    def create_box(
            self,
            position: List[float],
            size: List[float],
            unit: str = "",
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


