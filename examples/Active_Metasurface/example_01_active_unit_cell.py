import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(dirname(abspath(__file__)))))

# import library
from pyansoft import HFSS

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


""" Create 3D Object ============================= """
""" ============================================== """
pla_color = "(0 128 255)"
sub_color = "(128 128 128)"
silver_color = "(192 192 192)"

# Create airbox for periodic structure
air_box = hfss.modeler.create_box(
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


""" Create 2D Object ============================= """
""" ============================================== """

patch = hfss.modeler.create_rectangle(
    position=["-a/2", "-a/2", "t"], 
    size=["a", "a"], name="patch",
)

gnd = hfss.modeler.create_rectangle(
    position=["-p/2", "-p/2", "0"], 
    size=["p", "p"], name="Ground"
)

port = hfss.modeler.create_circle(
    center=["0", "d", "0"],
    radius="rp",
    name="Port"
)

hfss.operator.subtract(
    blank_parts=gnd,
    tool_parts=port,
    keep_original=True
)

hfss.boundary.assign_perfect_E(
    object_name=[patch, gnd],
    bc_name="Perf_E",
)

""" Assign materials =================================================================== """
""" ==================================================================================== """

""" Periodic Boundary and Floquet Port ================================================= """
""" ==================================================================================== """

face_id = hfss.operator.get_face_id(air_box)

# Master1
vertex_m1 = hfss.operator.get_vertex_id_from_face(face_id[2])
origin_m1 = hfss.operator.get_vertex_position(vertex_m1[1])
u_pos_m1 = hfss.operator.get_vertex_position(vertex_m1[2])

hfss.boundary.master(
    origin=origin_m1,
    u_pos=u_pos_m1,
    name="Master1",
    reverse_v=True,
    face_id=face_id[2]
)

# Master2
vertex_m2 = hfss.operator.get_vertex_id_from_face(face_id[3])
origin_m2 = hfss.operator.get_vertex_position(vertex_m2[1])
u_pos_m2 = hfss.operator.get_vertex_position(vertex_m2[2])

hfss.boundary.master(
    origin=origin_m2,
    u_pos=u_pos_m2,
    name="Master2",
    reverse_v=True,
    face_id=face_id[3]
)

# Slave1
vertex_s1 = hfss.operator.get_vertex_id_from_face(face_id[4])
origin_s1 = hfss.operator.get_vertex_position(vertex_s1[2])
u_pos_s1 = hfss.operator.get_vertex_position(vertex_s1[1])

hfss.boundary.slave(
    origin=origin_s1,
    u_pos=u_pos_s1,
    name="Slave1",
    master="Master1",
    face_id=face_id[4]
)

# Slave2
vertex_s2 = hfss.operator.get_vertex_id_from_face(face_id[5])
origin_s2 = hfss.operator.get_vertex_position(vertex_s2[2])
u_pos_s2 = hfss.operator.get_vertex_position(vertex_s2[1])

hfss.boundary.slave(
    origin=origin_s2,
    u_pos=u_pos_s2,
    name="Slave2",
    master="Master2",
    face_id=face_id[5]
)

# Floquet Port1
vertex_p1 = hfss.operator.get_vertex_id_from_face(face_id[0])
A_vector = [
    hfss.operator.get_vertex_position(vertex_p1[3]),
    hfss.operator.get_vertex_position(vertex_p1[0])
]
B_vector = [
    hfss.operator.get_vertex_position(vertex_p1[3]),
    hfss.operator.get_vertex_position(vertex_p1[2])
]
hfss.excitation.floquet_port(
    A_vector=A_vector,
    B_vector=B_vector,
    name="FloquetPort1",
    deembed="pz/2",
    face_id=face_id[0]
)

# Floquet Port2
vertex_p1 = hfss.operator.get_vertex_id_from_face(face_id[1])
A_vector = [
    hfss.operator.get_vertex_position(vertex_p1[2]),
    hfss.operator.get_vertex_position(vertex_p1[1])
]
B_vector = [
    hfss.operator.get_vertex_position(vertex_p1[2]),
    hfss.operator.get_vertex_position(vertex_p1[3])
]
hfss.excitation.floquet_port(
    A_vector=A_vector,
    B_vector=B_vector,
    name="FloquetPort2",
    deembed="pz/2",
    face_id=face_id[1]
)

# Setup Analysis
hfss.analysis.solution_setup(
    solution_name="Setup1",
    frequency="10GHz",
    max_passes=10,
)

hfss.analysis.frequency_sweep(
    sweep_name="Sweep",
    freq_range=("5GHz", "15GHz", "0.01GHz"),
    setup_name="Setup1"
)
