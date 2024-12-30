#include <stdio.h>

typedef enum { RED, GREEN, YELLOW } State;

State next_state(State current) {
    switch (current) {
        case RED: return GREEN;
        case GREEN: return YELLOW;
        case YELLOW: return RED;
    }
}

int main() {
    State current = RED;
    State next = next_state(current);

    // Symbolic execution starts here
    printf("Current State: %d, Next State: %d\n", current, next);

    return 0;
}
