// make poopoo here <- fuck the one who wrote it <- you go fuck urself :3
#include <iostream>
#include <string>
#include <stdexcept>
#include <vector>
#include <map>
#include <fstream>
#include "Headers/vector3d.h"
#include "Headers/object.h"
#include "Headers/radiator.h"
#include "Headers/receiver.h"
#include "Headers/signal.h"
#include "Libs/json.hpp"

using JSON = nlohmann::json;


void simulate(const std::string &path) {
    // json unpacking
    std::ifstream f(path);
    if (!f.is_open()) {
        throw std::invalid_argument("Failed to open file!");
    }
    std::cout << "Successfully opened file." << std::endl;

    JSON data = JSON::parse(f);
    std::cout << data["RAD"]["E"].get<double>() << std::endl;
    // --------------

    Radiator rad{data["RAD"]["E"].get<double>(),
                 Vector3D{data["RAD"]["COORD"][0].get<double>(),
                          data["RAD"]["COORD"][1].get<double>(),
                          data["RAD"]["COORD"][2].get<double>()},
                 Vector3D{data["RAD"]["DIR"][0].get<double>(),
                          data["RAD"]["DIR"][1].get<double>(),
                          data["RAD"]["DIR"][2].get<double>()}
    };

    Object obj{Vector3D{data["OBJ"]["COORD"][0].get<double>(),
                        data["OBJ"]["COORD"][1].get<double>(),
                        data["OBJ"]["COORD"][2].get<double>()},
               data["OBJ"]["RADIUS"].get<double>()};

    Receiver rec{Vector3D{data["REC"]["COORD"][0].get<double>(),
                          data["REC"]["COORD"][1].get<double>(),
                          data["REC"]["COORD"][2].get<double>()},
                 data["REC"]["CE"].get<double>()};

    std::vector<Signal> vector_of_signals{};

    rad.emit_signal(vector_of_signals);
    obj.reflect(vector_of_signals);
    rec.receive_signals(vector_of_signals);

    double distance = rec.distance();
    std::cout << "$RESULT$" << distance << std::endl; // ВСЕГДА ПИШИТЕ ENDL ИНАЧЕ Я ВАС НАЙДУ И ЗАДУШУ
}


int main(int argc, char *argv[]) // coords of obj, rad, rec
{
//    std::cout << argc << "\n";
//    for (int i = 0; i < argc; ++i) {
//    }
//    std::cout << "\n";

    if (argc != 2) {
        throw std::invalid_argument("Expected 2, got " + std::to_string(argc) + " args!");
    }

    simulate(argv[1]);
    return 0;
}