import math
class MagicOperation:
    def __add__(self,other):
        if not isinstance(other,(Cube,Sphere)):
            raise ValueError("Type does not match")
        return self.volume_in_m() + other.volume_in_m()
    
    def __sub__(self,other):
        if not isinstance(other,(Cube,Sphere)):
            raise ValueError("Type does not match")
        return self.volume_in_m() - other.volume_in_m()
    
    def volume_in_m(self) -> float:
        if self._unit == 'cm':
            return self._volume /1_000_000
        return self._volume
    
class Cube(MagicOperation):
    def __init__(self,side:float,unit:str):
        if side < 0 or unit not in ('cm','m'):
            raise ValueError("The values are invalid")
        self._side = side
        self._unit = unit
        self._volume = side ** 3
    
    def info(self) -> str:
        return (f"Cube: side={self._side:.2f} {self._unit}, "
                f"volume={self._volume:.2f} {self._unit}3")

class Sphere(MagicOperation):
    def __init__(self,radius:float,unit:str):
        if radius < 0 or unit not in ('cm','m'):
            raise ValueError("The values are invalid")
        self._radius = radius
        self._unit = unit
        self._volume = (4/3) * math.pi * (radius ** 3)
        
    def info(self) -> str:
        return (f"Sphere: radius={self._radius:.2f} {self._unit}, "
                f"volume={self._volume:.2f} {self._unit}3")

class Cubes:
    def __init__(self):
        self._cubes = []
    
    def get_cubes(self) -> list:
        return self._cubes
    
    def add_cube(self,cube:Cube):
        self._cubes.append(cube)
    
    def cubes_info(self) -> str:
        result = "Cubes:\n"
        if not self._cubes:  
            result += "No cubes available"
        else:
            lines = []
            for i, cube in enumerate(self._cubes, start=1):
                lines.append(f"{i}. {cube.info()}")
            result += "\n".join(lines)
        return result
    
class Spheres:
    def __init__(self):
        self._spheres = []
        
    def get_spheres(self) -> list:
        return self._spheres
    
    def add_sphere(self,sphere:Sphere):
        self._spheres.append(sphere)
    
    def spheres_info(self) -> str:
        result = "Spheres:\n"
        if not self._spheres:
            result += "No spheres available"
        else:
            lines = []
            for i, sphere in enumerate(self._spheres, start=1):
                lines.append(f"{i}. {sphere.info()}")
            result += "\n".join(lines)
        return result
    
class Shapes:
    def __init__(self,cube_shapes:Cubes,sphere_shapes:Spheres):
        self._cube_shapes = cube_shapes
        self._sphere_shapes = sphere_shapes
        
    def all_shapes_info(self) -> str:
        # reuse cubes_info() and spheres_info()
        result = self._cube_shapes.cubes_info()
        result += "\n"
        result += self._sphere_shapes.spheres_info()
        result += f"\nTotal volume: {self.total_volume_m():.2f} m3"
        result += f" / {self.total_volume_cm():.2f} cm3"
        return result
    
    def total_volume_m(self) -> float:
        total = 0.0
        for cube in self._cube_shapes.get_cubes():
            total += cube.volume_in_m()
        for sphere in self._sphere_shapes.get_spheres():
            total += sphere.volume_in_m()
        return total
    
    def total_volume_cm(self) -> float:
        return self.total_volume_m() * 1_000_000
    
    
cubes = Cubes()
cubes.add_cube(Cube(3, 'cm'))
cubes.add_cube(Cube(2, 'm'))

spheres = Spheres()
spheres.add_sphere(Sphere(5, 'cm'))

shapes = Shapes(cubes, spheres)
print(shapes.all_shapes_info())
