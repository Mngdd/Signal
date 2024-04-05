#include "../Headers/vector3d.h"
#include "../Headers/signal.h"
#include "../Headers/receiver.h"
#include "../Headers/radiator.h"
#include "../Headers/object.h"
#include "../Headers/maffler.h"


/*
double speed_calculation(Radiator& radiator, Object& object, Receiver& receiver, double dt)
{
    double l1, l2, l3;
    radiator.emit_signal(receiver, object);
    l1 = receiver.distance_using_power();
    object.update_position(dt);
    radiator.emit_signal(receiver, object);
    l2 = receiver.distance_using_power();
    object.update_position(dt);
    radiator.emit_signal(receiver, object);
    l3 = receiver.distance_using_power();
    object.update_position(dt);

    return (std::pow(l1*l1 + l3*l3 - 2*l2*l2, 0.5))/dt*pow(2,0.5);
}
*/


Receiver::Receiver(Vector3D coordinates_, double critical_energy_) :
    coordinates{coordinates_}, critical_energy{critical_energy_}, delay_sum{0}, average_delay{0},
    current_energy{0}, received_signals_count{0}, dist{0} {}

double Receiver::distance() { return dist; }

double Receiver::distance_using_power()
{
    double Pt_div_Pr = radiated_power/received_power;
    //mafflerenok.noise_mc(Pt_div_Pr);
    return std::pow(Pt_div_Pr*((std::pow(amplification_coefficient, 2)*sigma*std::pow(wave_length,2))/(64*pow(PI,3)*L)),0.25);
}

void Receiver::receive_signals(std::vector<Signal>& v_sign)
{
    for(int i = v_sign.size()-1; i >= 0; i--)
    {
        if(can_collide(coordinates - v_sign[i].coordinates, v_sign[i].direction_vector))
        {
            delay_sum += v_sign[i].passed_time + ((coordinates - v_sign[i].coordinates).abs())/speed_of_light;
            received_signals_count++;
        }
        v_sign.pop_back();
    }
    if(received_signals_count == 0)
        dist = -1;
    else
        dist = delay_sum/received_signals_count*speed_of_light/2;
}


std::pair<double, double> Receiver::mse(std::vector<double> arr)
{
    double mean = 0.0;
    for(auto c : arr) mean += c;
    mean /= arr.size();

    double sumSquaredDiff = 0;

    for (int i = 0; i < arr.size(); ++i) 
        sumSquaredDiff += std::pow(arr[i] - mean, 2);

    return {std::pow((sumSquaredDiff / arr.size()) , 0.5) , mean};
}