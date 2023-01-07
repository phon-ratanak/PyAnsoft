import sys

sys.path.append("../pyansoft")

# import library
from pyansoft import HFSS

hfss = HFSS(
    project_name="PeriodicStructure",
    design_name="UnitCell",
)

""" Design Variables ====================================== """

hfss["p"] = "7.5 mm"
hfss["pz"] = "30 mm"
hfss["t"] = "1 mm"

""" Create Object ========================================== """

air_box = hfss.modeler.create_box(
    position=["-p/2", "-p/2", "-pz/2"],
    size=["p", "p", "pz +t"],
    unit="",
    name="AirBox",
    transparency=0.8,
)

substrate = hfss.modeler.create_box(
    position=["-p/2", "-p/2", "0"], size=["p", "p", "t"], unit="", name="Substrate"
)
ground = hfss.modeler.create_rectangle(
    position=["-p/2", "-p/2", "0"], size=["p", "p"], unit="", name="Ground"
)

hfss.boundary.assign_perfect_E([ground], bc_name="PerfE")

# ground1 = hfss.modeler.create_rectangle(
#     position=["-p/2", "-p/4", "t"],
#     size=["p", "p/2"],
#     unit="",
#     name="Ground1"
# )
#
# v = hfss.operator.get_vertex_id_from_face(84)
# p0 = hfss.operator.get_vertex_position(v[0])
# p1 = hfss.operator.get_vertex_position(v[1])
# p2 = hfss.operator.get_vertex_position(v[2])
# p3 = hfss.operator.get_vertex_position(v[3])
#
# c0 = hfss.operator.get_center_point(p0, p1)
# c1 = hfss.operator.get_center_point(p2, p3)
#
# hfss.boundary.assign_lumped_RLC(
#     [ground1],
#     start_point=c0,
#     stop_point=c1,
#     rlc_name="Diode",
#     R_value="1ohm",
# )
""" Periodic Boundary and Floquet Port ===================== """
face_id = hfss.operator.get_face_id(air_box)

# Master1
vertex_m1 = hfss.operator.get_vertex_id_from_face(face_id[2])
origin_m1 = hfss.operator.get_vertex_position(vertex_m1[1])
u_pos_m1 = hfss.operator.get_vertex_position(vertex_m1[2])

hfss.boundary.master(
    origin=origin_m1, u_pos=u_pos_m1, name="Master1", reverse_v=True, face_id=face_id[2]
)

# Master2
vertex_m2 = hfss.operator.get_vertex_id_from_face(face_id[3])
origin_m2 = hfss.operator.get_vertex_position(vertex_m2[1])
u_pos_m2 = hfss.operator.get_vertex_position(vertex_m2[2])

hfss.boundary.master(
    origin=origin_m2, u_pos=u_pos_m2, name="Master2", reverse_v=True, face_id=face_id[3]
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
    face_id=face_id[4],
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
    face_id=face_id[5],
)

# Floquet Port1
vertex_p1 = hfss.operator.get_vertex_id_from_face(face_id[0])
A_vector = [
    hfss.operator.get_vertex_position(vertex_p1[3]),
    hfss.operator.get_vertex_position(vertex_p1[0]),
]
B_vector = [
    hfss.operator.get_vertex_position(vertex_p1[3]),
    hfss.operator.get_vertex_position(vertex_p1[2]),
]
hfss.excitation.floquet_port(
    A_vector=A_vector,
    B_vector=B_vector,
    name="FloquetPort1",
    deembed="pz/2",
    face_id=face_id[0],
)

# Floquet Port2
vertex_p1 = hfss.operator.get_vertex_id_from_face(face_id[1])
A_vector = [
    hfss.operator.get_vertex_position(vertex_p1[2]),
    hfss.operator.get_vertex_position(vertex_p1[1]),
]
B_vector = [
    hfss.operator.get_vertex_position(vertex_p1[2]),
    hfss.operator.get_vertex_position(vertex_p1[3]),
]
hfss.excitation.floquet_port(
    A_vector=A_vector,
    B_vector=B_vector,
    name="FloquetPort2",
    deembed="pz/2",
    face_id=face_id[1],
)

# Setup Analysis
hfss.analysis.solution_setup(
    solution_name="Setup1",
    frequency="10GHz",
    max_passes=10,
)

hfss.analysis.frequency_sweep(
    sweep_name="Sweep", freq_range=("5GHz", "15GHz", "0.01GHz"), setup_name="Setup1"
)
