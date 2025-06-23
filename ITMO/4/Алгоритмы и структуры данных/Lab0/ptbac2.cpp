#include<iostream>
#include<cmath>
using namespace std;

int sloveEquation(float a, float b, float c, float& x1, float& x2) {
    float delta = b*b - 4*a*c;
    cout << " delta = " << delta << endl;
    cout << endl;

    if (delta > 0) {
        double sqpr_delta = sqrt(delta);
        x1 = (-b + sqpr_delta) / (2 * a);
        x2 = (-b - sqpr_delta) / (2 * a);
        cout << "Квадратное уравнение имеет два различных решения! " << endl;
        cout << " x1 = " << x1 << "\t" << " x2 = " << x2;
        return 0;
    } else if (delta == 0) {
        float x;
        x = -b / (2 * a);
        cout << "Уравнение имеет двойное решение ! " << endl;
        cout << "x = " << x;
        return 0;
    } else { 
        cout << "нет решения ";
        return 0;
    }
}

int main() {
    float a, b, c, x1, x2;
    cout << "Введите коэффициенты уравнения :" << endl;
    cout << " a= "; cin >> a;
    cout << " b= "; cin >> b;
    cout << " c= "; cin >> c;
    cout << a << "x^2 + " << b << "x + " << c << " = 0" << endl;

    if (a != 0) {
        sloveEquation(a, b, c, x1, x2);
    } else {
        if (b == 0) {
            if (c == 0) {
                cout << "x - любое";
            } else {
                cout << "нет решения";
            }
        } else {
            float x1 = -c / b;
            cout << "x1 = " << x1;
        }
    }

    return 0;
}
