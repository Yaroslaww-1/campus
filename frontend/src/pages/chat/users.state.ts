import { runInAction, makeAutoObservable } from "mobx";
import { UsersService } from "@api/services/users.service";

import { FetchStatus } from "@common/enums/fetch-status.enum";
import { User } from "@models/user.model";

export class UsersState {
  users: User[] = [];
  state = FetchStatus.PENDING;

  constructor() {
    makeAutoObservable(this);
  }

  async fetchUsers() {
    this.users = [];
    this.state = FetchStatus.PENDING;
    try {
      const users = await UsersService.getUsers();
      runInAction(() => {
        this.users = users;
        this.state = FetchStatus.DONE;
      });
    } catch (e) {
      runInAction(() => {
        this.state = FetchStatus.ERROR;
      });
    }
  }
}

export const usersState = new UsersState();
