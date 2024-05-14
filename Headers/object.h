#pragma once


#include <vector>


class Vector3D;
class Object;
class Receiver;
class Signal;


// function to calculate initial distance between object and radiolocation station
double distance(Object& object, Receiver& receiver);

// Object - model class for object, which coordinates RLS is trying to predict
class Object
{
    public:
        Object(Vector3D coordinates_, double radius_, double refractive_index_, Vector3D speed_vector_);

        // calculate effective reflection surface using a formula
        void set_effective_reflection_surface(Receiver& receiver);

        // integration of object's position
        void update_position(double dt);

        // getter for private value
        double sigma() { return effective_reflection_surface; }

        // function to calculate initial distance between object and radiolocation station
        friend double distance(Object& object, Receiver& receiver);

        // function to calculate initial direction vector to object
        friend Vector3D dir_to_obj(Object& object, Receiver& receiver);

        // getter for private value
        Vector3D coordinates();

    private:
        Vector3D val_coordinates;
        double refractive_index;
        double effective_reflection_surface;
        double radius;
        Vector3D speed_vector;
};