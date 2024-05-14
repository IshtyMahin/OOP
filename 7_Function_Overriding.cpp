#include<bits/stdc++.h>
using namespace std;

class Person{
    public:
    int age;
    string name;
    Person(string name,int age){
        this->age=age;
        this->name=name;
    }
    void print(){
        cout << name << endl;
        cout<<age << endl;
    }
};

class Academic{
    public:
        float cgpa;
        Academic(float cgpa){
            this->cgpa=cgpa;
        }
        void print(){
            cout<<cgpa<<endl;
        }
};

class Student: public Person, public Academic{
    public:
    int id;
    Student(string name,int age,int id,float cgpa):Person(name,age),Academic(cgpa){
        this->id=id;
    }

    //  here print function override the base class print function
    void print(){
        Person::print();
        cout<<id<<endl;
        Academic::print();
    }
};
int main(){
    Student student("Ishitaq", 22, 2001011012,3.84);

    student.print();
}