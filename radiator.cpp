#include "vector3d.h"
#include "signal.h"
#include "radiator.h"


Radiator::Radiator(double energy_, Vector3D coordinates_, Vector3D direction_vector_) :
    energy{energy_}, coordinates{coordinates_}, direction_vector{direction_vector_} wave_length{(speed_of_light*plank_constant)/energy} {}

void Radiator::emit_signal(std::vector<Signal>& signal_vector)
{
    signal_vector.emplace_back(coordinates, direction_vector, energy);
}