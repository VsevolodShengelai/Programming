#include <iostream>
#include <cpp_httplib/httplib.h>
#include <nlohmann/json.hpp> 
using namespace httplib;
using json = nlohmann::json;
using std::string;
using std::ifstream;
using std::ofstream;


/*int main() {
	const std::string config = "config";
	auto j3 = json::parse(u8R"(config)");
	std::cout << j3;
}*/