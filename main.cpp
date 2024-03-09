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


void simulate(double e=0, Vector3D rad_coord={0, 1, 0}, Vector3D rad_dir={0, 1, 0},
              Vector3D obj_coord={0, 5, 0}, double radius = 1,
              Vector3D rec_coord={0, 1, 0}, double ce = 0)
{
    Radiator rad{e, rad_coord, rad_dir};
    Object obj{obj_coord, radius};
    Receiver rec{rec_coord, ce};

    std::vector<Signal> vector_of_signals{};

    rad.emit_signal(vector_of_signals);
    obj.reflect(vector_of_signals);
    rec.receive_signals(vector_of_signals);

    double distance = rec.distance();

    std::cout << distance << std::endl; // ВСЕГДА ПИШИТЕ ENDL ИНАЧЕ Я ВАС НАЙДУ И ЗАДУШУ
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
    simulate(tmp[0], {tmp[1], tmp[2], tmp[3]}, {tmp[4], tmp[5], tmp[6]},
             {tmp[7], tmp[8], tmp[9]}, tmp[10],
             {tmp[11], tmp[12], tmp[13]}, tmp[14]);
    return 0;
}