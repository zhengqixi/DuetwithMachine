#include "phoentics.h"
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <cctype>

using namespace std;

phoentics::phoentics (int size){
	dictionary = new unordered_map<string, string>(size);
}

phoentics::~phoentics (){
	delete dictionary;
}

void phoentics::loadDictionary(string &name){
	ifstream input(name.c_str());
	string line;
	string word;
	string phoentics;
	while(!input.eof()){
		getline(input, line);
		if (line.find('(') != -1){
			continue;
		}
		int pos;
		int pos1 = line.find_first_of(32); 
		int pos2 = line.find_first_of(9);
		if (pos1 == -1){
			pos = pos2;
		} else if (pos2 == -1){
			pos = pos1;
		} else {
			pos = (pos1 > pos2) ? pos2 : pos1;
		}
		word = line.substr(0, pos);
		phoentics = line.substr(pos, line.size());
		word = removeWhite(word);
		(*dictionary)[word] = phoentics;
	}
	return;
}

void phoentics::createFile(string &input, string &output){
	ifstream poem(input.c_str());
	ofstream music(output.c_str());
	string line;
	while(!poem.eof()){
		getline(poem, line);
		upperCase(line);
		stringstream ss;
		ss << line;
		while(!ss.eof()){
			string word;
			ss >> word;
			unordered_map<string,string>::const_iterator get = dictionary->find(word);
			if (get == dictionary->end())
				continue;
			music << get->second << " ";
		}
		music << endl;	
	}	
	return;
}

string phoentics::removeWhite(string &trunc){
	int a,b;
	for (a = 0; a < trunc.size(); ++a){
		if ((trunc[a] <= 90 && trunc[a] >= 65) || (trunc[a] <= 48 && trunc[a] >= 57))
			break;
	}
	for (b = trunc.size()-1; b > a; --b){
		if ((trunc[a] <= 90 && trunc[a] >= 65) || (trunc[a] <= 48 && trunc[a] >= 57))
			break;
	}
	return trunc.substr(a, b-a+1);
}

void phoentics::upperCase(string &original){
	for (int i = 0; i < original.size(); ++i){
		original[i] = toupper(original[i]);
		if (!((original[i] >= 65 && original[i] <= 90) || original[i] == 39))
			original[i] = ' ';
	}
	return;
}

