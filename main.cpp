// make poopoo here <- fuck the one who wrote it <- you go fuck urself :3
#include <iostream>
#include <string>
#include <stdexcept>
#include <vector>
#include <fstream>
#include "Headers/vector3d.h"
#include "Headers/object.h"
#include "Headers/radiator.h"
#include "Headers/receiver.h"
#include "Headers/signal.h"
#include "Libs/json.hpp"

using JSON = nlohmann::json;

double speed_calculation(Radiator &radiator, Object &object, Receiver &receiver, double dt) {
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

    return (std::pow(l1 * l1 + l3 * l3 - 2 * l2 * l2, 0.5)) / (dt * pow(2, 0.5));
}

void simulate(const std::string &path, const std::string &export_path = "$ABORT$",
              const int number_of_measurements = 100) {
    // json unpacking
    std::ifstream f(path);
    if (!f.is_open()) {
        throw std::invalid_argument("Failed to open file!");
    }
    std::cout << "Successfully opened file." << std::endl;

    JSON data = JSON::parse(f);
    std::cout << data["RAD"]["E"].get<double>() << std::endl;
    // --------------
    double L = 1;
    Radiator rad{data["RAD"]["E"].get<double>(),
                 Vector3D{data["RAD"]["COORD"][0].get<double>(),
                          data["RAD"]["COORD"][1].get<double>(),
                          data["RAD"]["COORD"][2].get<double>()},
                 Vector3D{data["RAD"]["DIR"][0].get<double>(),
                          data["RAD"]["DIR"][1].get<double>(),
                          data["RAD"]["DIR"][2].get<double>()},
                 L,
                 data["RAD"]["AMP"].get<double>()
    };

    Object obj{Vector3D{data["OBJ"]["COORD"][0].get<double>(),
                        data["OBJ"]["COORD"][1].get<double>(),
                        data["OBJ"]["COORD"][2].get<double>()},
               data["OBJ"]["RADIUS"].get<double>(),
               data["OBJ"]["REF_IND"].get<double>(),
               Vector3D{data["OBJ"]["VEL"][0].get<double>(),
                        data["OBJ"]["VEL"][1].get<double>(),
                        data["OBJ"]["VEL"][2].get<double>()}};

    Receiver rec{Vector3D{data["REC"]["COORD"][0].get<double>(),
                          data["REC"]["COORD"][1].get<double>(),
                          data["REC"]["COORD"][2].get<double>()},
                 data["REC"]["CE"].get<double>()};

    std::vector<Signal> vector_of_signals{};

    obj.set_effective_reflection_surface(rec);
    rad.emit_signal(rec, obj);

    std::cout << ' ' <<
              // rec.received_power << ' ' <<
              // rec.L << ' ' <<
              rec.sigma << ' ';
    // rec.wave_length << ' ' <<
    // rec.amplification_coefficient << '\n';

    // double distance = rec.distance();

    double delta_t = data["DELTA_TIME"].get<double>();

    double distance = rec.distance_using_power();
    double speed = speed_calculation(rad, obj,
                                     rec, delta_t);

    std::cout << "$RESULT$" << distance << "$RESULT$" << speed <<
              "$RESULT$" << rec.sigma << "$RESULT$" << rec.wave_length <<
              "$RESULT$" << L << std::endl;
    // ВСЕГДА ПИШИТЕ ENDL И РАЗДЕЛЯЙТЕ ВВОД СПЕЦТЕКСТОМ ИНАЧЕ Я ВАС НАЙДУ И ЗАДУШУ
    if (export_path != "$ABORT$") {
        std::ofstream outfile(export_path);
        outfile << "==========FILE_FOR_RECEIVED_MEASUREMENTS==========" << std::endl << std::endl;

        for (int i = 1; i <= number_of_measurements; i++) {
            distance = rec.distance_using_power();
            speed = speed_calculation(rad, obj, rec, delta_t);
            outfile << "MEASUREMENT NUMBER " << i << ":\n";
            outfile << "DISTANCE = " << distance << '\n';
            outfile << "SPEED = " << speed << '\n' << std::endl;
        }
    }

}


int main(int argc, char *argv[]) // coords of obj, rad, rec
{
    if (argc == 2) {
        simulate(argv[1]);
    } else if (argc == 4) {
        simulate(argv[1], argv[2], atoi(argv[3]));
    } else {
        throw std::invalid_argument("Expected 2 or 4, got " + std::to_string(argc) + " args!");
    }
    return 0;
}