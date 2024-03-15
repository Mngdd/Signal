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

    // rad.emit_signal(vector_of_signals);
    // obj.reflect(vector_of_signals);
    // rec.receive_signals(vector_of_signals);

    rad.emit_signal(rec, obj);

    // double distance = rec.distance();

    double distance = rec.distance_using_power();
    double speed = speed_calculation(rad, obj,
                                     rec, data["DELTA_TIME"].get<double>());

    std::cout << "$RESULT$" << distance << speed << "$RESULT$" << std::endl; // ВСЕГДА ПИШИТЕ ENDL ИНАЧЕ Я ВАС НАЙДУ И ЗАДУШУ
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