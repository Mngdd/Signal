#include "../Headers/vector3d.h"
#include "../Headers/receiver.h"
#include "../Headers/radiator.h"
#include "../Headers/object.h"
#include "../Headers/muffler.h"
#include <iostream>

Receiver::Receiver(Vector3D coordinates_, double critical_energy_) :
    coordinates{coordinates_}, critical_energy{critical_energy_}, current_energy{0} {}


double Receiver::distance_using_power(Radiator& radiator, Object& object, Muffler& muffler)
{
    radiator.emit_signal(*this, object);
    muffler.noise_mc(received_power);
    double Pt_div_Pr = radiated_power/received_power;
    return std::pow(Pt_div_Pr*((std::pow(amplification_coefficient, 2)*sigma*std::pow(wave_length,2))/(64*pow(PI,3)*L)),0.25);
}

Vector3D Receiver::coordinates_using_power(Radiator& radiator, Object& object, Vector3D direction_vector, Muffler& muffler)
{
    Vector3D unit_vector = direction_vector/direction_vector.abs();
    return coordinates + unit_vector*distance_using_power(radiator, object, muffler);
}

std::pair<Vector3D, Vector3D> Receiver::coordinates_with_mse(Radiator& radiator, Object& object, Vector3D direction_vector, Muffler& muffler)
{
    Vector3D unit_vector = direction_vector/direction_vector.abs();

    std::vector<double> abscisses;
    std::vector<double> ordinates;
    std::vector<double> applicates;

    for(int i = 0; i < number_of_measurements; i++)
    {
        Vector3D coordinate = coordinates + unit_vector*distance_using_power(radiator, object, muffler);
        abscisses.push_back(coordinate.x);
        ordinates.push_back(coordinate.y);
        applicates.push_back(coordinate.z); 
    }

    std::pair<Vector3D, Vector3D> answer = {{0, 0, 0}, {0, 0, 0}};

    answer.first.x = mse(abscisses).first;
    answer.second.x = mse(abscisses).second;

    answer.first.y = mse(ordinates).first;
    answer.second.y = mse(ordinates).second;

    answer.first.z = mse(applicates).first;
    answer.second.z = mse(applicates).second;

    radiator.reset_energy();

    return answer;
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
        sumX2 += time[i] * time[i];
    }
 
    double avrX = sumX / n;
    double avrY = sumY / n;
    double avrXY = sumXY / n;
    double avrX2 = sumX2 / n;

    double k = (avrXY - avrX * avrY) / (avrX2 - avrX * avrX);
    double b = (avrY - k * avrX);

    return std::make_pair(k, b);
}

Vector3D Receiver::speed_vector_with_mse(Radiator& rad, Object& object, Muffler& muffler, Vector3D direction_vector, double dt)
{
    std::vector<double> abscisses;
    std::vector<double> ordinates;
    std::vector<double> applicates;

    std::vector<double> time_vector;

    for(int i = 1; i <= speed_measurements_amount; i++)
    {

        time_vector.push_back(i*dt);

        rad.emit_signal(*this, object);
        Vector3D coord = coordinates_with_mse(rad, object, direction_vector, muffler).first;

        abscisses.push_back(coord.x);
        ordinates.push_back(coord.y);
        applicates.push_back(coord.z);

        object.update_position(dt);
    }

    Vector3D speed_vector;

    speed_vector.x = mnk(time_vector, abscisses).first;
    speed_vector.y = mnk(time_vector, ordinates).first;
    speed_vector.z = mnk(time_vector, applicates).first;

    return speed_vector;
}
