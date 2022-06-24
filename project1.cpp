#include "project1.h"

void map(int map_size, int treasure_location_x, int treasure_location_y){

  for(int i=1; i<map_size; i++){
    cout << i << " ";

    for(int j=1; j<=map_size-1; j++){
      if(j==treasure_location_y && i==treasure_location_x){
        cout << "X ";

      }else if(i<map_size &j<map_size){
        cout << "- ";

      }else if(i==map_size){
        cout << j << " ";
      }
    }
    cout << endl;
  }
  cout << "  ";
  for (int i=1; i<map_size; i++){
    cout << i << " ";
  }
  return;
}



int options(int selection, int &treasure_location_x, int &treasure_location_y){

  switch(selection){

    case 1:
      cout << "\nEnter the coordinates of the treasure: ";
      cin >> treasure_location_x >> treasure_location_y;
      cout << "\nIn the options: " << treasure_location_x << "," << treasure_location_y << ".\n";
      return treasure_location_x, treasure_location_y;

    case 2:
      char direction;
      int spaces;

      cout << "Which direction would you like to move, and how many steps? "
        "\n\nEnter (N/S/E/W) or (5 to move 5 steps in that direction)" << endl;
      cin >> direction >> spaces;

      if(direction =='N' || direction =='n'){
        treasure_location_x-=spaces;    //decrease x by 1
        cout << "\nIn case 2: " << treasure_location_x << "," << treasure_location_y << ".\n";
        return treasure_location_x;
        break;

      }else if(direction =='S' || direction =='s'){
        treasure_location_x+=spaces;    //increase y by 1
        cout << "\nIn case 2: " << treasure_location_x << "," << treasure_location_y << ".\n";
        return treasure_location_x;
        break;

      }else if(direction =='E' || direction =='e'){
        treasure_location_y+=spaces;    //increase y by 1
        cout << "\nIn case 2: " << treasure_location_x << "," << treasure_location_y << ".\n";
        return treasure_location_y;
        break;

      }else if(direction =='W'|| direction =='w'){
        treasure_location_y-=spaces;    //decrease y by 1
        cout << "\nIn case 2: " << treasure_location_x << "," << treasure_location_y << ".\n";
        return treasure_location_y;
        break;
      }
      break;

  }
  return selection;
}

bool win(int x, int y, bool winning){
  if( x && y == 5){
    cout << "YOU'VE FOUND THE TREASURE!! ";
    winning = true;
    winning +=1;
    return true;
  }else{
    return false;
  }
}
