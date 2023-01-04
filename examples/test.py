# import library
from pyansoft import HFSS

hfss = HFSS(
    project_name="HFDDasa",
    design_name="hjdsh1",
    solution_type="DrivenModal",
)

hfss["va"] = "2 mm"
hfss["$a"] = "2 mm"
hfss["b"] = "2 mm"

a = hfss.modeler.create_rectangle([1, 1, 1], [2, 3])
b = hfss.modeler.create_circle([1, 2, 2], 1)
print(dir(a))
hfss["$aa"] = "2 mm"
hfss["bss"] = "2 mm"
