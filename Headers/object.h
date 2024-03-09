#pragma once


#include <vector>


class Vector3D;
class Signal;



//New method - integration of object's position (интегрирование положения объекта, т.е. функция, которая обновляет его положение)
//x(t+delta_t) = x(t) + vx*delta_t
//y(t+delta_t) = y(t) + vy*delta_t
//z(t+delta_t) = z(t) + vz*delta_t



class Object
{
    public:
        Object(Vector3D coordinates_, double radius_, double refractive_index_);
        void reflect(std::vector<Signal>& v_sign);
        Vector3D coordinates();

    private:
        Vector3D val_coordinates;
        double refractive_index;
        double effective_reflection_surface; //in the next realization it will depend on the radius
        double radius;
};