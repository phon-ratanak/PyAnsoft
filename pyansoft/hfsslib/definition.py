from typing import List


class Definition:
    """A class for creating 1D, 2D, and 3D models."""

    def __init__(self, oDesktop) -> None:
        self.oDesktop = oDesktop
        self.oProject = self.oDesktop.GetActiveProject()
        self.oDefinitionManager = self.oProject.GetDefinitionManager()

    def clone_material(self):
        # print(dir(self.oDefinitionManager))
        self.clone_material.CloneMaterial()
    # def add_material(
    #     self,
    #     material_name: str = "new_material",
    #     permittivity: float = 1,
    #     permeability: float = 1,
    #     conductivity: float=	58000000,
    #     thermal_conductivity: float = 400,
    #     mass_density: float = 8933,
    #     specific_heat: float = 385,
    #     youngs_modulus: float= 120000000000,
    #     poissons_ratio: float = 0.38,
    #     thermal_expansion_coeffcient: float = 1.77e-005
    #     ):

    #     parameters = [
    #         f"NAME:{material_name}",
    #         "CoordinateSystemType:=", "Cartesian",
    #         [
    #             "NAME:AttachedData"
    #         ],
    #         [
    #             "NAME:ModifierData"
    #         ],
    #         "permittivity:="	, f"{permittivity}",
    #         "permeability:="	, f"{permeability}",
    #         "conductivity:="	, f"{conductivity}",
    #         "thermal_conductivity:=", f"{thermal_conductivity}",
    #         "mass_density:="	, f"{mass_density}",
    #         "specific_heat:="	, f"{specific_heat}",
    #         "youngs_modulus:="	, f"{youngs_modulus}",
    #         "poissons_ratio:="	, f"{poissons_ratio}",
    #         "thermal_expansion_coeffcient:=", f"{thermal_expansion_coeffcient}"
    #     ]

    #     [
	# 	"NAME:Material3",
	# 	"CoordinateSystemType:=", "Cartesian",
	# 	[
	# 		"NAME:AttachedData"
	# 	],
	# 	[
	# 		"NAME:ModifierData"
	# 	],
	# 	"permittivity:="	, "2",
	# 	"permeability:="	, "2",
	# 	"conductivity:="	, "2",
	# 	"dielectric_loss_tangent:=", "1",
	# 	"magnetic_loss_tangent:=", "1",
	# 	"saturation_mag:="	, "1tesla",
	# 	"lande_g_factor:="	, "1",
	# 	"delta_H:="		, "1A_per_meter",
	# 	"mass_density:="	, "1",
	# 	"delta_H_freq:="	, "1GHz"
	# ]

    #     return self.oDefinitionManager.AddMaterial(parameters)