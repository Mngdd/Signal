#include "vector3d.h"
#include "object.h"
#include "signal.h"


Object::Object(Vector3D coordinates, double radius_, double refractive_index_, double effective_reflection_surface_) :
    val_coordinates{coordinates}, radius{radius_}, refractive_index{refractive_index_}, effective_reflection_surface{effective_reflection_surface_} {}

Vector3D Object::coordinates() { return val_coordinates; }

void Object::reflect(std::vector<Signal>& v_sign)
{
    for(int i = v_sign.size() - 1; i >= 0; i--)
    {
        if(!can_collide(val_coordinates - v_sign[i].coordinates, v_sign[i].direction_vector))
            v_sign.erase(v_sign.begin() + i, v_sign.begin() + i + 1);
        else
            v_sign[i].change_direction(*this);
    }
}