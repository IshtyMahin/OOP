#include<bits/stdc++.h>
using namespace std;

class Person{
    public:
        string name;
        int age;
        Person(string name, int age){
            this->name = name;
            this->age = age;
        }
};

class Student: public Person{
    public:
    int rollno;
    Student(string name,int age, int rollno):Person(name,age){
        this->rollno = rollno;
    }

};
class UniversityStudent: public Student{
   public:
       string major;

       UniversityStudent(string name,int age,int rollno,string major):
       Student(name,age,rollno){
        this->major = major;
       }

    void display(){
        cout<<"Name: "<<name<<endl;
        cout<<"Age: "<<age<<endl;
        cout<<"Rollno: "<<rollno<<endl;
        cout<<"Major: "<<major<<endl;
    }
};
int main(){
    UniversityStudent s1("Ishtiaq",23,12,"CSE");
    s1.display();

}