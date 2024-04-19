#include "../Headers/vector3d.h"
#include "../Headers/object.h"
#include "../Headers/signal.h"


Signal::Signal(Vector3D coordinates_, Vector3D starting_direction_vector_, double energy_) :
            coordinates{coordinates_}, direction_vector{starting_direction_vector_}, energy{energy_}, passed_time{0},
            wave_length{(speed_of_light*plank_constant)/energy} {}

void Signal::change_direction(Object& obj)
{
    passed_time += ((obj.coordinates() - coordinates).abs())/speed_of_light;
    coordinates = obj.coordinates();
    direction_vector.reverse();
}