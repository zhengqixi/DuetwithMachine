#include "phoentics.h"
#include <string>
#include <iostream>

using namespace std;

int main(){
	string dict, input;
	cout << "Enter the name of the dictionary" << endl;
	cin >> dict;
	cout << "Enter name of your EPIC POETRY" << endl;
	cin >> input;
	phoentics load(150000);
	load.loadDictionary(dict);
	string output = "out.txt";
	load.createFile(input, output);
	return 0;
}
