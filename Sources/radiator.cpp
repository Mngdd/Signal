#include "../Headers/vector3d.h"
#include "../Headers/receiver.h"
#include "../Headers/radiator.h"
#include "../Headers/object.h"
#include <iostream>


Radiator::Radiator(double energy_, Vector3D coordinates_, double L_, double amplification_coefficient_) :
    base_energy{energy_}, current_energy{energy_}, coordinates{coordinates_},
    wave_length{(speed_of_light*plank_constant)/energy_}, L{L_},
    amplification_coefficient{amplification_coefficient_} {}

void Radiator::emit_signal(Receiver& receiver, Object& object)
{
    double R = distance(object, receiver);

    double member_1 = (current_energy*current_energy*amplification_coefficient)/(4*PI*R*R);
    double member_2 = (object.sigma())/(4*PI*R*R);
    double member_3 = (amplification_coefficient*wave_length*wave_length)/(4*PI);
    double member_4 = 1/L;

    double received_power = member_1*member_2*member_3*member_4;

    receiver.receive_signals(current_energy*current_energy, received_power, L, wave_length, object.sigma(), amplification_coefficient);

    double increase = distribution/number_of_measurements/100;
    current_energy += increase*base_energy;
    wave_length = (speed_of_light*plank_constant)/current_energy;
}

void Radiator::reset_energy()
{
    current_energy = base_energy;
    wave_length = (speed_of_light*plank_constant)/current_energy;
}