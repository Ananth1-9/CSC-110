def sphere_to_surface_area(radius):
    """Calculate the surface area of a sphere given its radius."""
    surface_area = 4 * 3.1415 * radius**2
    return surface_area

def sphere_to_volume(radius):
    """Calculate the volume of a sphere given its radius."""
    volume = sphere_to_surface_area(radius) * radius / 3
    return volume

print(round(sphere_to_volume(.75),2))

print(round(sphere_to_surface_area(.75),2))