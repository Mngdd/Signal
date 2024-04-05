#include "../Headers/vector3d.h"
#include "../Headers/object.h"
#include "../Headers/signal.h"
#include "../Headers/receiver.h"
#include <iostream>


Object::Object(Vector3D coordinates, double radius_, double refractive_index_, Vector3D speed_vector_) :
    val_coordinates{coordinates}, radius{radius_}, refractive_index{refractive_index_},
    speed_vector{speed_vector_} {}

Vector3D Object::coordinates() { return val_coordinates; }

void Object::set_effective_reflection_surface(Receiver& receiver)
{
    double R = distance(*this, receiver);
    effective_reflection_surface = PI*radius*std::pow(4*R*R-radius*radius, 0.5);
}

void Object::update_position(double dt)
{
    val_coordinates.x += speed_vector.x*dt;
    val_coordinates.y += speed_vector.y*dt;
    val_coordinates.z += speed_vector.z*dt;
}

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

double distance(Object& object, Receiver& receiver)
{
    return (object.val_coordinates - receiver.coordinates).abs();
}
