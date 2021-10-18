import { User } from "@models/user.model";

import api from "../api.helper";

const endpoint = "users";

export class UsersService {
  static async getUsers(): Promise<User[]> {
    const users = await api.get<User[]>(endpoint);
    return users;
  }
}
