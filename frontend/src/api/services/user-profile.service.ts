import { User } from "@models/user.model";

import api from "../api.helper";

const endpoint = "users";

export class UserProfileService {
  static async getUser(id: string): Promise<User> {
    const user = await api.get<User>(`${endpoint}/${id}/`);
    return user;
  }
}
