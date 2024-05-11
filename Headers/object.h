#pragma once


#include <vector>


class Vector3D;
class Object;
class Receiver;
class Signal;


double distance(Object& object, Receiver& receiver);


class Object
{
    public:
        Object(Vector3D coordinates_, double radius_, double refractive_index_, Vector3D speed_vector_);

        void set_effective_reflection_surface(Receiver& receiver);
        //integration of object's position
        void update_position(double dt);
        double sigma() { return effective_reflection_surface; }
        friend double distance(Object& object, Receiver& receiver);
        friend Vector3D dir_to_obj(Object& object, Receiver& receiver);
        Vector3D coordinates();

    private:
        Vector3D val_coordinates;
        double refractive_index;
        double effective_reflection_surface;
        double radius;
        Vector3D speed_vector;
};