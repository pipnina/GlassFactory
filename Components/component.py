class Component:


    #x_pos = 0
    #y_pos = 0
    #z_pos = 0
    #x_rot = 0
    #y_rot = 0

    # Lens, Baffle, Prism, Camera, Focuser, Light, Group
    #part_type = "Lens"
    #part_name = "New Lens"
    #parent: "Component"

    properties ={
        "x_pos": 0,
        "y_pos": 0,
        "z_pos": 0,
        "x_rot": 0,
        "y_rot": 0,
        "part_type": "VOID",
        "part_name": "Unnamed Void",
        "parent": ["Component"]
    }

    def __init__(self, x: float, y: float, z: float, xr: float, yr: float, prt_typ: str, prt_name: str, parent: "Component"):
        self.properties["x_pos"] = x
        self.properties["y_pos"] = y
        self.properties["z_pos"] = z
        self.properties["x_rot"] = xr
        self.properties["y_rot"] = yr
        self.properties["part_type"] = prt_typ
        self.properties["part_name"] = prt_name
        self.properties["parent"] = parent

        #self.x_pos = x
        #self.y_pos = y
        #self.z_pos = z
        #self.x_rot = xr
        #self.y_rot = yr
        #self.part_type = pt
        #self.part_name = pn
        #self.parent = prent

