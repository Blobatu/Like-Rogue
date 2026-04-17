import random as r
from . import props_interaction as prop_int


chest = {

    "sprite":"[]",
    "interaction": prop_int.chest
    


}
barrel = {
    "sprite":"()",
    "interaction": prop_int.barrel


}
door = {
    "sprite":"||",
    "interaction": prop_int.door

}
spike_trap = {
    
    "sprite":"△",
    "interaction": prop_int.spike_trap,
}
void = {
    "sprite":" ",
    "interaction": prop_int.void,
}
props = {

    "[]":chest,
    "()":barrel,
    "||":door,
    "△":spike_trap,
    " ":void,



}