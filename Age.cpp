#include <iostream>
using namespace std;

int main()
{ 
	int age;
	cout << "Please enter age: ";
	cin >> age;
	
	while (age <= 0)	
	{
		if (age < 0)
		{
			cout << "Entered a negative number.\n";
		}
		else if (age == 0)
		{
			cout << "Not even born yet.\n";

		}
		cout << "Please enter age: ";
		cin >> age;
	}
cout << "You entered your age as: " << age << endl;
return 0;
}
