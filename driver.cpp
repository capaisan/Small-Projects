#include "project1.h"

int main(){

  int map_size, treasure_location_x, treasure_location_y;
  int selection=1;
  bool winning=0;


  cout << "Enter a map size: ";
  cin >> map_size;

  cout << "\nEnter the coordinates of the treasure: ";
  cin >> treasure_location_x >> treasure_location_y;

  while (( treasure_location_x >=map_size || treasure_location_y >= map_size ) || ( treasure_location_x < 1 || treasure_location_y < 1)){
    cout << "Invalid input. Please try again.\n";
    cout << "\nEnter the coordinates of the treasure: ";
    cin >> treasure_location_x >> treasure_location_y;
  }

  while(selection>0 && selection<3 && winning == 0){

    cout << "\nTreasure map\n" <<  endl;

    map(map_size, treasure_location_x, treasure_location_y);

    cout << "\n\n1) Update treasure coordinates (row/column)\n";
    cout << "2) Shift X (N S E W)\n";
    cout << "3) Exit Program\n";
    cout << "\nSelect: ";
    cin >> selection;

    options(selection, treasure_location_x, treasure_location_y);
    cout << "\nYour coordinates: " << treasure_location_x << "," << treasure_location_y << ".\n";

    win(treasure_location_x, treasure_location_y, winning);


  }
  cout << "\nExiting program.\n";
  return 0;

}
