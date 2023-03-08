# Point to pyansoft library
import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(dirname(abspath(__file__)))))

from pyansoft import HFSS


# import library

hfss = HFSS(
    project_name="Active_Metasurface",
    design_name="Unit_Cell",
)

""" Design Variables ============================= """
""" ============================================== """

hfss["p"] = "7.5 mm"
hfss["pz"] = "30 mm"
hfss["t"] = "1 mm"
hfss["rv"] = "0.15 mm"
hfss["rp"] = "0.3 mm"
hfss["a"] = "6 mm"
hfss["d"] = "2 mm"


""" Object Color ================================= """
""" ============================================== """
sub_color = "(128 128 128)"
via_color = "(192 192 192)"
cond_color = "(192 192 192)"

# Diode color RLC lumped component
R_color = "(192 192 192)"
L_color = "(192 192 192)"
C_color = "(192 192 192)"

""" Create 3D Object ============================= """
""" ============================================== """

# Create airbox


def create_air_box(Nx, Ny, dx, dy):
    return hfss.modeler.create_box(
        position=["-p/2", "-p/2", "-pz/2-t/2"],
        size=["p", "p", "pz + t"],
        name="AirBox",
        transparency=1
    )


# Create substrate
substrate = hfss.modeler.create_box(
    position=["-p/2", "-p/2", "0"],
    size=["p", "p", "t"],
    color=sub_color,
    name="Substrate",
    material="FR4_epoxy"
)

# Create via
via = hfss.modeler.create_cylinder(
    center=["0", "d", "0"],
    radius="rv",
    height="t",
    color=sub_color,
    name="mid_via",
    material="pec",
    solve_inside=False
)

# Create Via
via_list = []
N_via = 10
# via wall
for iy in range(2):
    for iv in range((N_via - 1) + 1):
        wall = hfss.modeler.create_cylinder(
            center=[f"-p/2+{iv}*p/({N_via-1})", f"{-1+2*iy}*p/2", "0"],
            radius="rv", height="t",
            name=f"via_{iy}_{iv}",
            material="pec",
            solve_inside=False
        )
        via_list.append(wall)

via_wall = hfss.operator.unite(via_list)
hfss.operator.intersect(
    object_name=[via_wall, air_box],
    keep_original=True
)

hfss.operator.subtract(
    blank_parts=substrate,
    tool_parts=via_wall,
    keep_original=True
)

""" Create 3D Object ============================= """
""" ============================================== """
