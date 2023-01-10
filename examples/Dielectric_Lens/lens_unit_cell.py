# Point to pyansoft library
import sys
from os.path import dirname, abspath
sys.path.append(dirname(dirname(dirname(abspath(__file__)))))

# import library
from pyansoft import HFSS

hfss = HFSS(
    project_name="MetasurfaceLens", 
    design_name="Unit_Cell",
)

""" Design Variables ============================= """
""" ============================================== """

hfss["p"] = "3 mm"
hfss["pz"] = "10 mm"
hfss["t"] = "2 mm"
hfss["w"] = "0.2 mm"
hfss["h"] = "0.4 mm"


""" Object Color ================================= """
""" ============================================== """
sub_color = "(128 128 128)"

""" Create 3D Object ============================= """
""" ============================================== """

# Create airbox
air_box = hfss.modeler.create_box(
        position=["-p/2", "-p/2", "-pz/2"], 
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
)

hole = hfss.modeler.create_box(
    position=["-(p-w)/2", "-(p-w)/2", "t-h"], 
    size=["p-w", "p-w", "h"],
    color=sub_color, 
    name="Hole",
)

hfss.operator.subtract(blank_parts=substrate, tool_parts=hole)


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
    frequency="55GHz",
    max_passes=10,
)

hfss.analysis.frequency_sweep(
    sweep_name="Sweep",
    freq_range=("45GHz", "55GHz", "0.01GHz"),
    setup_name="Setup1"
)
