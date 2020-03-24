#include "mbed.h"

DigitalOut myled(LED1);


int main() {
    while(1) {
        myled = !myled; // LED is ON
        wait(0.8); // 200 ms
    }
}