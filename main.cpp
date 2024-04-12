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
#include "Headers/muffler.h"
#include "Libs/json.hpp"

using JSON = nlohmann::json;

void simulate(const std::string &path, const std::string &export_path = "$ABORT$",
              const int number_of_measurements = 100) {
    // json unpacking
    std::ifstream f(path);
    if (!f.is_open()) {
        throw std::invalid_argument("Failed to open file!");
    }
    std::cout << "Successfully opened file." << std::endl;

    JSON data = JSON::parse(f);
    std::cout << data["RL"]["E"].get<double>() << std::endl;
    // --------------
    double L = 1;
    Radiator rad{data["RL"]["E"].get<double>(),
                 Vector3D{data["RL"]["COORD"][0].get<double>(),
                          data["RL"]["COORD"][1].get<double>(),
                          data["RL"]["COORD"][2].get<double>()},
                 Vector3D{data["RL"]["DIR"][0].get<double>(),
                          data["RL"]["DIR"][1].get<double>(),
                          data["RL"]["DIR"][2].get<double>()},
                 L,
                 data["RL"]["AMP"].get<double>()
    };

    Object obj{Vector3D{data["OBJ"]["COORD"][0].get<double>(),
                        data["OBJ"]["COORD"][1].get<double>(),
                        data["OBJ"]["COORD"][2].get<double>()},
               data["OBJ"]["RADIUS"].get<double>(),
               data["OBJ"]["REF_IND"].get<double>(),
               Vector3D{data["OBJ"]["VEL"][0].get<double>(),
                        data["OBJ"]["VEL"][1].get<double>(),
                        data["OBJ"]["VEL"][2].get<double>()}};

    Receiver rec{Vector3D{data["RL"]["COORD"][0].get<double>(),
                          data["RL"]["COORD"][1].get<double>(),
                          data["RL"]["COORD"][2].get<double>()},
                 data["RL"]["CE"].get<double>()};

    Muffler muf{data["DISTORTION_PERCENT"].get<double>()};


    obj.set_effective_reflection_surface(rec);
    rad.emit_signal(rec, obj);

    double delta_t = data["DELTA_TIME"].get<double>();

    double muffled_distance = rec.distance_using_power(muf);
    Vector3D dir_to_obj_vector = dir_to_obj(obj, rec);
    // Vector3D obj_coords = rec.coordinates_using_poweir_to_obj_vector, muf);
    std::pair<Vector3D, Vector3D> obj_coords = rec.coordinates_with_mse(dir_to_obj_vector, muf);
    double speed = rec.speed_calculation(rad, obj, muf, delta_t);

    std::cout << "$RESULT$" << muffled_distance << "$RESULT$" << speed <<
              "$RESULT$" << rec.get_sigma() << "$RESULT$" << rec.get_wave_length() <<
              "$RESULT$" << L <<
              "$RESULT$" << obj_coords.first.x << "$RESULT$" << obj_coords.first.y <<
              "$RESULT$" << obj_coords.first.z <<std::endl;
    // ВСЕГДА ПИШИТЕ ENDL И РАЗДЕЛЯЙТЕ ВВОД СПЕЦТЕКСТОМ ИНАЧЕ Я ВАС НАЙДУ И ЗАДУШУ
    if (export_path != "$ABORT$") {
        std::ofstream outfile(export_path);
        outfile << "==========FILE_FOR_RECEIVED_MEASUREMENTS==========" << std::endl << std::endl;

        for (int i = 1; i <= number_of_measurements; i++) {
            obj.set_effective_reflection_surface(rec);
            rad.emit_signal(rec, obj);

            muffled_distance = rec.distance_using_power(muf);
            speed = rec.speed_calculation(rad, obj, muf, delta_t);

            outfile << "MEASUREMENT NUMBER " << i << ":\n";
            outfile << "DISTANCE = " << muffled_distance << '\n';
            outfile << "SPEED = " << speed << '\n' << std::endl;
        }
    }
}


int main(int argc, char *argv[]) {
    if (argc == 2) {
        simulate(argv[1]);
    } else if (argc == 4) {
        simulate(argv[1], argv[2], atoi(argv[3]));
    } else {
        throw std::invalid_argument("Expected 2 or 4, got " + std::to_string(argc) + " args!");
    }
    return 0;
}