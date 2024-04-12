#include "../Headers/vector3d.h"
#include "../Headers/signal.h"
#include "../Headers/receiver.h"
#include "../Headers/radiator.h"
#include "../Headers/object.h"
#include "../Headers/muffler.h"
#include <iostream>

Receiver::Receiver(Vector3D coordinates_, double critical_energy_) :
    coordinates{coordinates_}, critical_energy{critical_energy_}, delay_sum{0}, average_delay{0},
    current_energy{0}, received_signals_count{0}, dist{0} {}

double Receiver::distance() { return dist; }

double Receiver::distance_using_power(Muffler& muffler)
{
    muffler.noise_mc(received_power);
    double Pt_div_Pr = radiated_power/received_power;
    return std::pow(Pt_div_Pr*((std::pow(amplification_coefficient, 2)*sigma*std::pow(wave_length,2))/(64*pow(PI,3)*L)),0.25);
}

double Receiver::distance_using_power()
{
    double Pt_div_Pr = radiated_power/received_power;
    return std::pow(Pt_div_Pr*((std::pow(amplification_coefficient, 2)*sigma*std::pow(wave_length,2))/(64*pow(PI,3)*L)),0.25);
}

Vector3D Receiver::coordinates_using_power(Vector3D direction_vector, Muffler& muffler)
{
    Vector3D unit_vector = direction_vector/direction_vector.abs();
    return coordinates + unit_vector*distance_using_power(muffler);
}

std::pair<Vector3D, Vector3D> Receiver::coordinates_with_mse(Vector3D direction_vector, Muffler& muffler)
{
    Vector3D unit_vector = direction_vector/direction_vector.abs();

    std::vector<double> abscisses;
    std::vector<double> ordinates;
    std::vector<double> applicates;

    for(int i = 0; i < 52; i++)
    {
        Vector3D coordinate = coordinates + unit_vector*distance_using_power(muffler);
        abscisses.push_back(coordinate.x);
        ordinates.push_back(coordinate.y);
        applicates.push_back(coordinate.z); 
    }

    std::pair<Vector3D, Vector3D> answer = {{0, 0, 0}, {0, 0, 0}};

    answer.first.x = mse(abscisses).first;
    answer.second.x = mse(abscisses).second;

    answer.first.y = mse(abscisses).first;
    answer.second.y = mse(abscisses).second;

    answer.first.z = mse(abscisses).first;
    answer.second.z = mse(abscisses).second;

    return answer;
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

void Receiver::receive_signals(double radiated_power_, double received_power_, double L_,
                             double wave_length_, double sigma_, double amplification_coefficient_)
{
    radiated_power = radiated_power_;
    received_power = received_power_;
    L = L_;
    wave_length = wave_length_;
    sigma = sigma_;
    amplification_coefficient = amplification_coefficient_;
}

std::pair<double, double> Receiver::mse(std::vector<double> arr)
{
    double mean = 0.0;
    for(auto c : arr) mean += c;
    mean /= arr.size();

    double sumSquaredDiff = 0;

    for (size_t i = 0; i < arr.size(); ++i) 
        sumSquaredDiff += std::pow(arr[i] - mean, 2);

    return {mean, std::pow((sumSquaredDiff / arr.size()) , 0.5)};
}

std::pair<double, double> Receiver::mnk(std::vector<double> time, std::vector<double> coord)
{
    int n = time.size();
    double sumX = 0.0, sumY = 0.0, sumXY = 0.0, sumX2 = 0.0;

    for(int i = 0; i < n; i++) {
        sumX += time[i];
        sumY += coord[i];
        sumXY += time[i] * coord[i];
        sumX2 += time[i] * coord[i];
    }

    double k = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
    double b = (sumY - k * sumX) / n;

    return std::make_pair(k, b);
}

double Receiver::speed_calculation(Radiator& rad, Object& object, Muffler& muffler, double dt)
{
    double l1, l2, l3;
    rad.emit_signal(*this, object);
    l1 = distance_using_power();
    object.update_position(dt);
    rad.emit_signal(*this, object);
    l2 = distance_using_power();
    object.update_position(dt);
    rad.emit_signal(*this, object);
    l3 = distance_using_power();
    object.update_position(dt);

    double speed = (std::pow(std::abs(l1*l1 + l3*l3 - 2*l2*l2), 0.5))/dt*pow(0.5,0.5);
    muffler.noise_mc(speed);
    return speed;
}

