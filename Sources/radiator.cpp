#include "../Headers/vector3d.h"
#include "../Headers/signal.h"
#include "../Headers/radiator.h"


Radiator::Radiator(double energy_, Vector3D coordinates_, Vector3D direction_vector_) :
    energy{energy_}, coordinates{coordinates_}, direction_vector{direction_vector_} {}

void Radiator::emit_signal(std::vector<Signal>& signal_vector)
{
    signal_vector.emplace_back(coordinates, direction_vector, energy);
}