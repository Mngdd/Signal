// make poopoo here <- fuck the one who wrote it
#include <vector>
#include <stdexcept>

constexpr double speed_of_light = 299792458; // meters per second

class Object;

class Vector3D
{
    public:
        Vector3D() : x{0}, y{0}, z{0} {}
        Vector3D(double x_, double y_, double z_) : x{x_}, y{y_}, z{z_} {}
        void reverse() {x = -x; y = -y; z = -z;}

        double x;
        double y;
        double z;
};

Vector3D operator+(Vector3D v1, Vector3D v2)
{
    return {v1.x + v2.x, v1.y + v2.y, v1.z + v2.z};
}

Vector3D operator-(Vector3D v)
{
    return {-v.x, -v.y, -v.z};
}

Vector3D operator-(Vector3D v1, Vector3D v2)
{
    return v1 + (-v2);
}

bool can_collide(Vector3D v1, Vector3D v2)
{
    if((v1.x == 0) && (v1.y == 0) && (v1.z == 0))
        throw std::runtime_error("object and RLS are at the same place");
    else if((v2.x == 0) && (v2.y == 0) && (v2.z == 0))
        throw std::runtime_error("signal has a null-vector direction");

    return (((v1.x == v2.x && v1.x == 0) || ((v1.x/v2.x == v1.y/v2.y) && (v1.x/v2.x > 0))) &&
            ((v1.y == v2.y && v1.y == 0) || ((v1.y/v2.y == v1.z/v2.z) && (v1.y/v2.y > 0))));
}

class Signal
{
    public:
        Signal(Vector3D coordinates_, Vector3D starting_direction_vector_, double energy_) :
            coordinates{coordinates_}, direction_vector{starting_direction_vector_}, energy{energy_}, passed_time{0} {}

        void change_direction(Object& obj)
        {

            coordinates.reverse();
        }

        Vector3D coordinates;
        Vector3D direction_vector;
        double passed_time;
        double energy;
};

class Object
{
    public:
        Object(Vector3D coordinates_, double radius_) : coordinates{coordinates_}, radius{radius_} {}
        void reflect(std::vector<Signal>& v_sign)
        {
            for(int i = v_sign.size() - 1; i >= 0; i--)
            {
                if(!can_collide(coordinates - v_sign[i].coordinates, v_sign[i].direction_vector))
                    v_sign.erase(v_sign.begin() + i, v_sign.begin() + i + 1);
                else
                {
                    v_sign[i].change_direction(*this);
                }
            }
        }

    private:
        Vector3D coordinates;
        double radius;
};

class Radiator
{
    public:
        Radiator(double energy_, Vector3D coordinates_, Vector3D direction_vector_) : energy{energy_}, coordinates{coordinates_},
                                                                                      direction_vector{direction_vector_} {}
        void emit_signal(std::vector<Signal>& signal_vector)
        {
            signal_vector.emplace_back(coordinates, direction_vector, energy);
        }

    private:
        double energy;
        Vector3D coordinates;
        Vector3D direction_vector;
};

class Receiver
{
    public:
        Receiver(Vector3D coordinates_, double critical_energy_) : coordinates{coordinates_}, critical_energy{critical_energy_} {}
    private:
        Vector3D coordinates;
        double current_energy;
        double critical_energy;
        double average_delay;
};

int main()
{
    return 0;
}