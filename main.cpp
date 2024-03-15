// make poopoo here <- fuck the one who wrote it <- you go fuck urself :3
#include <iostream>
#include <string>
#include <stdexcept>
#include <vector>
#include "Headers/vector3d.h"
#include "Headers/object.h"
#include "Headers/radiator.h"
#include "Headers/receiver.h"
#include "Headers/signal.h"


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


void simulate(double e=0, Vector3D rad_coord={0, 1, 0}, Vector3D rad_dir={0, 1, 0}, double L = 1,
              double amplification_coefficient = 1, Vector3D obj_coord={0, 5, 0}, double radius = 1, double refractive_index = 0,
              Vector3D obj_speed_vector={1, 1, 1}, Vector3D rec_coord={0, 1, 0}, double ce = 0, double dt = 1)
{
    Radiator rad{e, rad_coord, rad_dir, L, amplification_coefficient};
    Object obj{obj_coord, radius, refractive_index, obj_speed_vector};
    Receiver rec{rec_coord, ce};

    std::vector<Signal> vector_of_signals{};

    // rad.emit_signal(vector_of_signals);
    // obj.reflect(vector_of_signals);
    // rec.receive_signals(vector_of_signals);

    rad.emit_signal(rec, obj);

    // double distance = rec.distance();

    double distance = rec.distance_using_power();
    double speed = speed_calculation(rad, obj, rec, dt);

    std::cout << distance << std::endl; // ВСЕГДА ПИШИТЕ ENDL ИНАЧЕ Я ВАС НАЙДУ И ЗАДУШУ
    std::cout << speed << std::endl;
}


int main(int argc, char** argv) // coords of obj, rad, rec
{
//    std::cout << argc << "\n";
//    for (int i = 0; i < argc; ++i) {
//    }
//    std::cout << "\n";

    if (argc != 16) {
        throw std::invalid_argument("Expected 16, got " + std::to_string(argc) + " args!");
    }
    std::vector<double> tmp;
    for (int i = 1; i < argc; ++i) {
        tmp.push_back(std::stod(argv[i]));
    }
    simulate(tmp[0], {tmp[1], tmp[2], tmp[3]}, {tmp[4], tmp[5], tmp[6]}, 1, 1,
             {tmp[7], tmp[8], tmp[9]}, tmp[10], 0, {1, 1, 1},
             {tmp[11], tmp[12], tmp[13]}, tmp[14], 1);
    return 0;
}