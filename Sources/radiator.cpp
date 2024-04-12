#include "../Headers/vector3d.h"
#include "../Headers/signal.h"
#include "../Headers/receiver.h"
#include "../Headers/radiator.h"
#include "../Headers/object.h"
#include <iostream>


Radiator::Radiator(double energy_, Vector3D coordinates_, Vector3D direction_vector_, double L_, double amplification_coefficient_) :
    energy{energy_}, coordinates{coordinates_}, direction_vector{direction_vector_},
    wave_length{(speed_of_light*plank_constant)/energy}, L{L_}, amplification_coefficient{amplification_coefficient_} {}

void Radiator::emit_signal(std::vector<Signal>& signal_vector)
{
    signal_vector.emplace_back(coordinates, direction_vector, energy);
}

void Radiator::emit_signal(Receiver& receiver, Object& object)
{
    double R = distance(object, receiver);
    double member_1 = (energy*amplification_coefficient)/(4*PI*R*R);
    double member_2 = (object.sigma())/(4*PI*R*R);
    double member_3 = (amplification_coefficient*wave_length*wave_length)/(4*PI);
    double member_4 = 1/L;

    double received_power = member_1*member_2*member_3*member_4;
    
    receiver.receive_signals(energy, received_power, L, wave_length, object.sigma(), amplification_coefficient);
}