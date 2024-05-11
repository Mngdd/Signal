#pragma once


#include <vector>


class Vector3D;
class Object;
class Receiver;
class Signal;



//New method - integration of object's position (интегрирование положения объекта, т.е. функция, которая обновляет его положение)
//x(t+delta_t) = x(t) + vx*delta_t
//y(t+delta_t) = y(t) + vy*delta_t
//z(t+delta_t) = z(t) + vz*delta_t


double distance(Object& object, Receiver& receiver);


class Object
{
    public:
        Object(Vector3D coordinates_, double radius_, double refractive_index_, Vector3D speed_vector_);

        void set_effective_reflection_surface(Receiver& receiver);
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