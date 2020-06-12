Startingpoint
  add starting point to traversal
  while traversal not empty
    get connected rooms
    add connected rooms to path
    while path not empty
      pick random vert from path
      pop that dir from path
      go to that room
      add to visited
        get connected rooms - previous room
        if connected rooms in visited
          go back
        else
          pick random room from connected
          add to path
          add to visited
          set as current room