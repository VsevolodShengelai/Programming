#include <iostream>
#include <cpp_httplib/httplib.h>
#include <nlohmann/json.hpp> 
using namespace httplib;
using json = nlohmann::json;
using std::string;
using std::ifstream;
using std::ofstream;

// В этой функции формируем ответ сервера на запрос
void gen_response(const Request& req, Response& res) {
	string Answer = "None";
	if (req.has_param("login") && req.has_param("password") && req.has_param("config"))
	{
		const std::string login = req.get_param_value("login");
		//std::cout << login;
		const std::string password = req.get_param_value("password");
		//std::cout << password;
		const std::string config = req.get_param_value("config");
		std::cout << config;

		//json jconfig = json::parse(req.get_param_value("config"));
		//std::cout << jconfig;
		
		std::ifstream i("users.json");
		json j;
		i >> j;

		bool In_list = 0;

		for (auto& x : j["users"].items())
		{
			std::cout << "key: " << x.key() << '\n';
			if (x.key() == login)
			{
				In_list = 1;
			}
		}
		//std::cout << In_list;
		if (!In_list) {
			j["users"][login] = { {"password", password},{"scores", 0}, {"config", config} };

	    //std::cout << j;

		std::ofstream o("users.json");
		o << std::setw(4) << j << std::endl;

		std::cout << In_list;
		if (In_list == 1) Answer = u8R"(NO)";
		else Answer = u8R"(Yes)";
		}
	}
	std::cout << Answer;
	res.set_content(Answer, "text/plain");
}

// В этой функции формируем ответ сервера на запрос
void gen_response_enter(const Request& req, Response& res) {
	std::string data = "None";
	if (req.has_param("login") && req.has_param("password"))
	{
		const std::string login = req.get_param_value("login");
		//std::cout << login;
		const std::string password = req.get_param_value("password");
		//std::cout << password;

		std::ifstream i("users.json");
		json j;
		i >> j;

		bool In_list = 0;

		for (auto& x : j["users"].items())
		{
			std::cout << "key: " << x.key() << '\n';
			if (x.key() == login && j["users"][x.key()]["password"] == password)
			{
				data = j["users"][x.key()]["config"];
			}
		}
		//std::cout << In_list;
	}
	std::cout << data;
	res.set_content(data, "text/plain");
}

int main() {
	//setlocale(LC_ALL, "Russian");

	Server svr;                    // Создаём сервер (пока-что не запущен)
	svr.Get("/", gen_response);    // Вызвать функцию gen_response если кто-то обратиться к корню "сайта"
	svr.Get("/enter", gen_response_enter);
	std::cout << "Start server... OK\n";
	svr.listen("localhost", 1234); // Запускаем сервер на localhost и порту 1234
}