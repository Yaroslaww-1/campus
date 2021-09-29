import { setInterval } from "timers";

import { User } from "@models/user.model";

export class UsersService {
  static getUsers(): Promise<User[]> {
    const userList = [
      {
        id: "1",
        name: "Nazarii Striletskyi",
        role: "student",
        status: "online",
      },
      {
        id: "2",
        name: "Yaroslav Borodaienko",
        role: "student",
        status: "online",
      },
      { id: "3", name: "Clown", role: "lecturer", status: "offline" },
      { id: "4", name: "Circus", role: "admin", status: "offline" },
    ];
    return new Promise(resolve => {
      setInterval(() => {
        resolve(userList);
      }, 1000);
    });
  }
}
