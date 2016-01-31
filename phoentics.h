#ifndef PHOENTICS_H
#define PHOENTICS_H 
#include <string>
#include <unordered_map>

class phoentics{
	public:
		phoentics(int size);
		~phoentics();
		void loadDictionary(std::string &input);
		void createFile(std::string &input, std::string &output);
	private:
		std::unordered_map<std::string, std::string> * dictionary;
		std::string removeWhite(std::string &trunc);
		void upperCase(std::string &original);
};
#endif
