#include "vector3d.h"
#include "signal.h"
#include "receiver.h"


Receiver::Receiver(Vector3D coordinates_, double critical_energy_, double L_) :
    coordinates{coordinates_}, critical_energy{critical_energy_}, delay_sum{0},
    average_delay{0}, current_energy{0}, received_signals_count{0}, dist{0}, L{L_} {}

double Receiver::distance() { return dist; }

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