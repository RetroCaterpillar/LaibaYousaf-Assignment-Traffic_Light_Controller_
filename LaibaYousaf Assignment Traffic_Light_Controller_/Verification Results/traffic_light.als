abstract sig State {}
one sig Red, Green, Yellow extends State {}

sig Light {
    current: one State
}

pred validTransitions(current: State, next: State) {
    (current = Red and next = Green) or
    (current = Green and next = Yellow) or
    (current = Yellow and next = Red)
}

run {
    some l1, l2: Light | validTransitions[l1.current, l2.current]
} for 3
